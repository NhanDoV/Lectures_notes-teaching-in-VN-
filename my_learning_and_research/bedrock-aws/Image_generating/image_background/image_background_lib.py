import boto3
import json
import base64
from io import BytesIO
from random import randint

#get a BytesIO object from file bytes
def get_bytesio_from_bytes(image_bytes):
    image_io = BytesIO(image_bytes)
    return image_io

#get a base64-encoded string from file bytes
def get_base64_from_bytes(image_bytes):
    resized_io = get_bytesio_from_bytes(image_bytes)
    img_str = base64.b64encode(resized_io.getvalue()).decode("utf-8")
    return img_str

#load the bytes from a file on disk
def get_bytes_from_file(file_path):
    with open(file_path, "rb") as image_file:
        file_bytes = image_file.read()
    return file_bytes

#get the stringified request body for the InvokeModel API call
def get_titan_image_background_replacement_request_body(prompt, image_bytes, mask_prompt, negative_prompt=None, outpainting_mode="DEFAULT"):
    
    input_image_base64 = get_base64_from_bytes(image_bytes)
    body = { #create the JSON payload to pass to the InvokeModel API
        "taskType": "OUTPAINTING",
        "outPaintingParams": {
            "image": input_image_base64,
            "text": prompt,  # Description of the background to generate
            "maskPrompt": mask_prompt,  # The element(s) to keep
            "outPaintingMode": outpainting_mode,  # "DEFAULT" softens the mask. "PRECISE" keeps it sharp.
        },
        "imageGenerationConfig": {
            "numberOfImages": 1,  # Number of variations to generate
            "quality": "premium",  # Allowed values are "standard" and "premium"
            "height": 512,
            "width": 512,
            "cfgScale": 8.0,
            "seed": randint(0, 100000),  # Use a random seed
        },
    }
    
    if negative_prompt:
        body['outPaintingParams']['negativeText'] = negative_prompt
    
    return json.dumps(body)

#get a BytesIO object from the Titan Image Generator response
def get_titan_response_image(response):

    response = json.loads(response.get('body').read())
    images = response.get('images')
    image_data = base64.b64decode(images[0])

    return BytesIO(image_data)

#generate an image using Amazon Titan Image Generator
def get_image_from_model(prompt_content, image_bytes, mask_prompt=None, negative_prompt=None, outpainting_mode="DEFAULT"):
    session = boto3.Session()
    bedrock = session.client(service_name='bedrock-runtime') #creates a Bedrock client
    body = get_titan_image_background_replacement_request_body(prompt_content, 
                                                               image_bytes, 
                                                               mask_prompt=mask_prompt, 
                                                               negative_prompt=negative_prompt, 
                                                               outpainting_mode=outpainting_mode) #mask prompt "objects to keep" prompt text "description of background to add"
    response = bedrock.invoke_model(body=body, 
                                    modelId="amazon.titan-image-generator-v1", 
                                    contentType="application/json", accept="application/json")
    output = get_titan_response_image(response)
    
    return output
