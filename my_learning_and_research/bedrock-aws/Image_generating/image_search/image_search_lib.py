import itertools
import boto3
import json
import base64
import chromadb
from io import BytesIO

#calls Bedrock to get a vector from either an image, text, or both
def get_multimodal_vector(input_image_base64=None, input_text=None):
    
    session = boto3.Session()
    bedrock = session.client(service_name='bedrock-runtime') #creates a Bedrock client    
    request_body = {}
    
    if input_text:
        request_body["inputText"] = input_text
        
    if input_image_base64:
        request_body["inputImage"] = input_image_base64
    
    body = json.dumps(request_body)
    
    response = bedrock.invoke_model(
    	body=body, 
    	modelId="amazon.titan-embed-image-v1", 
    	accept="application/json", 
    	contentType="application/json"
    )
    
    response_body = json.loads(response.get('body').read())    
    embedding = response_body.get("embedding")
    
    return embedding

def get_collection(path, collection_name):

    client = chromadb.PersistentClient(path=path)
    collection = client.get_collection(collection_name)
    
    return collection

def get_vector_search_results(collection, query_embedding):
    
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=4
    )
    
    return results


#get a base64-encoded string from file bytes
def get_base64_from_bytes(image_bytes):
    
    image_io = BytesIO(image_bytes)
    
    image_base64 = base64.b64encode(image_io.getvalue()).decode("utf-8")
    
    return image_base64


#get a list of images based on the provided search term and/or search image
def get_similarity_search_results(search_term=None, search_image=None):
    
    search_image_base64 = (get_base64_from_bytes(search_image) if search_image else None)
    query_embedding = get_multimodal_vector(input_text=search_term, input_image_base64=search_image_base64)    
    collection = get_collection("../../data/chroma", "images_collection")    
    search_results = get_vector_search_results(collection, query_embedding)    
    flattened_results_list = list(itertools.chain(*search_results['documents'])) #flatten the list of lists returned by chromadb        
    results_images = []
    
    for res in flattened_results_list: #load images into list
        
        with open(res, "rb") as f: 
            img = BytesIO(f.read())
        
        results_images.append(img)
    
    
    return results_images

