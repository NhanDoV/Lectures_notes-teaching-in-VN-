import boto3
import json
import base64
from PIL import Image
from io import BytesIO
from random import randint

def get_bytesio_from_bytes(image_bytes):
    image_io = BytesIO(image_bytes)
    return image_io

def get_base64_from_bytes(image_bytes):
    resized_io = get_bytesio_from_bytes(image_bytes)
    img_str = base64.b64encode(resized_io.getvalue()).decode("utf-8")
    return img_str

def get_image_from_bytes(image_bytes):
    image_io = BytesIO(image_bytes)
    image = Image.open(image_io)
    return image
    

def get_png_base64(image):
    png_io = BytesIO()
    image.save(png_io, format="PNG")
    img_str = base64.b64encode(png_io.getvalue()).decode("utf-8")
    return img_str

#load the bytes from a file on disk
def get_bytes_from_file(file_path):
    with open(file_path, "rb") as image_file:
        file_bytes = image_file.read()
    return file_bytes

def get_titan_image_masking_request_body(prompt_content, image_bytes, painting_mode, masking_mode, mask_bytes, mask_prompt):
    
    original_image = get_image_from_bytes(image_bytes)
    target_width, target_height = original_image.size
    image_base64 = get_base64_from_bytes(image_bytes)
    mask_base64 = get_base64_from_bytes(mask_bytes)
    
    body = {
        "taskType": painting_mode,
        "imageGenerationConfig": {
            "numberOfImages": 1,  # Number of variations to generate
            "quality": "premium",  # Allowed values are "standard" and "premium"
            "height": target_height,
            "width": target_width,
            "cfgScale": 8.0,
            "seed": randint(0, 100000),  # Use a random seed
        },
    }
    
    params = {
        "image": image_base64,
        "text": prompt_content,  # What should be displayed in the final image
    }
    
    if masking_mode == 'Image':
        params['maskImage'] = mask_base64
    else:
        params['maskPrompt'] = mask_prompt
        
    
    if painting_mode == 'OUTPAINTING':
        params['outPaintingMode'] = 'DEFAULT'
        body['outPaintingParams'] = params
    else:
        body['inPaintingParams'] = params
    
    return json.dumps(body)
    
def get_titan_response_image(response):

    response = json.loads(response.get('body').read())
    images = response.get('images')
    image_data = base64.b64decode(images[0])

    return BytesIO(image_data)

def get_image_from_model(prompt_content, image_bytes, painting_mode, masking_mode, mask_bytes=None, mask_prompt=None):
    session = boto3.Session()
    bedrock = session.client(service_name='bedrock-runtime') #creates a Bedrock client
    body = get_titan_image_masking_request_body(prompt_content, image_bytes, painting_mode, masking_mode, mask_bytes, mask_prompt)
    response = bedrock.invoke_model(body=body, 
                                    modelId="amazon.titan-image-generator-v1", 
                                    contentType="application/json", accept="application/json")
    output = get_titan_response_image(response)
    
    return output