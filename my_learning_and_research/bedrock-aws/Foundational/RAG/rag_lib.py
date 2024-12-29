import itertools
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

def get_rag_response(question):

    session = boto3.Session()
    bedrock = session.client(service_name='bedrock-runtime')
    
    collection = get_collection("../../data/chroma", "bedrock_faqs_collection")
    
    search_results = get_vector_search_results(collection, question)
    
    flattened_results_list = list(itertools.chain(*search_results['documents'])) #flatten the list of lists returned by chromadb
    
    rag_content = "\n\n".join(flattened_results_list)
    print(rag_content)
    
    message = {
        "role": "user",
        "content": [
            { "text": rag_content },
            { "text": "Based on the content above, please answer the following question:" },
            { "text": question }
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
    
    return response['output']['message']['content'][0]['text'], flattened_results_list