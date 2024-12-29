import boto3
import chromadb
from chromadb.utils.embedding_functions import AmazonBedrockEmbeddingFunction

def get_collection(path, collection_name):
    session = boto3.Session()
    embedding_function = AmazonBedrockEmbeddingFunction(session=session, model_name="amazon.titan-embed-text-v2:0")
    
    client = chromadb.PersistentClient(path=path)
    collection = client.get_collection(collection_name, embedding_function=embedding_function)
    
    return collection

def get_vector_search_results(collection, question):
    
    results = collection.query(
        query_texts=[question],
        n_results=4
    )
    
    return results

def get_personalized_recommendation(question, description):
    session = boto3.Session()
    bedrock = session.client(service_name='bedrock-runtime')
    
    message = {
        "role": "user",
        "content": [
            { "text": f"<service_description>{description}</service_description>" },
            { "text": "Based on the service description above, please summarize how it addresses the following requirements:" },
            { "text": f"<requirements>{question}</requirements>" }
        ]
    }
    
    response = bedrock.converse(
        modelId="anthropic.claude-3-sonnet-20240229-v1:0",
        messages=[message],
        inferenceConfig={
            "maxTokens": 2000,
            "temperature": 0,
            "topP": 0.9,
            "stopSequences": []
        },
    )
    
    return response['output']['message']['content'][0]['text']

def get_similarity_search_results(question):

    session = boto3.Session()
    bedrock = session.client(service_name='bedrock-runtime')
    
    collection = get_collection("../../data/chroma", "services_collection")
    
    search_results = get_vector_search_results(collection, question)
    
    num_results = len(search_results['documents'][0])
    
    results_list = []
    
    for i in range(num_results):
        personalized_recommendation = get_personalized_recommendation(question, search_results['documents'][0][i])
        
        results_list.append({
            'original': search_results['documents'][0][i],
            'summary': personalized_recommendation,
            'name': search_results['metadatas'][0][i]['name'],
            'url': search_results['metadatas'][0][i]['url'],
        })
    
    return results_list

