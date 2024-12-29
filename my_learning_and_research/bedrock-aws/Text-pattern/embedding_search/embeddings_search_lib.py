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

def get_similarity_search_results(question):

    session = boto3.Session()
    bedrock = session.client(service_name='bedrock-runtime')
    
    collection = get_collection("../../data/chroma", "bedrock_faqs_collection")
    
    search_results = get_vector_search_results(collection, question)
    
    flattened_results_list = list(itertools.chain(*search_results['documents'])) #flatten the list of lists returned by chromadb
    
    return flattened_results_list
