import itertools
import boto3
import chromadb
from chromadb.utils.embedding_functions import AmazonBedrockEmbeddingFunction

MAX_MESSAGES = 20

class ChatMessage(): #create a class that can store image and text messages
    def __init__(self, role, text):
        self.role = role
        self.text = text

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

def get_tools():
    tools = [
        {
            "toolSpec": {
                "name": "get_amazon_bedrock_information",
                "description": "Retrieve information about Amazon Bedrock, a managed service for hosting generative AI models.",
                "inputSchema": {
                    "json": {
                        "type": "object",
                        "properties": {
                            "query": {
                                "type": "string",
                                "description": "The retrieval-augmented generation query used to look up information in a repository of FAQs about Amazon Bedrock."
                            }
                        },
                        "required": [
                            "query"
                        ]
                    }
                }
            }
        }
    ]

    return tools

def convert_chat_messages_to_converse_api(chat_messages):
    messages = []
    
    for chat_msg in chat_messages:
        messages.append({
            "role": chat_msg.role,
            "content": [
                {
                    "text": chat_msg.text
                }
            ]
        })
            
    return messages

def process_tool(response_message, messages, bedrock, tool_list):
    
    messages.append(response_message)
    
    response_content_blocks = response_message['content']

    follow_up_content_blocks = []
    
    for content_block in response_content_blocks:
        if 'toolUse' in content_block:
            tool_use_block = content_block['toolUse']
            
            if tool_use_block['name'] == 'get_amazon_bedrock_information':
                
                collection = get_collection("../../data/chroma", "bedrock_faqs_collection")
                
                query = tool_use_block['input']['query']
                
                print("----QUERY:----")
                print(query)
                
                search_results = get_vector_search_results(collection, query)
    
                flattened_results_list = list(itertools.chain(*search_results['documents'])) #flatten the list of lists returned by chromadb
                
                rag_content = "\n\n".join(flattened_results_list)
                
                print("----RAG CONTENT----")
                print(rag_content)
                
                follow_up_content_blocks.append({
                    "toolResult": {
                        "toolUseId": tool_use_block['toolUseId'],
                        "content": [
                            { "text": rag_content }
                        ]
                    }
                })
                
                
    if len(follow_up_content_blocks) > 0:
        
        follow_up_message = {
            "role": "user",
            "content": follow_up_content_blocks,
        }
    
        messages.append(follow_up_message)
        
        response = bedrock.converse(
            modelId="anthropic.claude-3-sonnet-20240229-v1:0",
            messages=messages,
            inferenceConfig={
                "maxTokens": 2000,
                "temperature": 0,
                "topP": 0.9,
                "stopSequences": []
            },
            toolConfig={
                "tools": tool_list
            }
        )
        
    
        return True, response['output']['message']['content'][0]['text'] #tool used, response
        
    else:
        return False, None #tool not used, no response


def chat_with_model(message_history, new_text=None):
    session = boto3.Session()
    bedrock = session.client(service_name='bedrock-runtime') #creates a Bedrock client
    
    tool_list = get_tools()
    
    new_text_message = ChatMessage('user', text=new_text)
    message_history.append(new_text_message)
    
    number_of_messages = len(message_history)
    
    if number_of_messages > MAX_MESSAGES:
        del message_history[0 : (number_of_messages - MAX_MESSAGES) * 2] #make sure we remove both the user and assistant responses
    
    messages = convert_chat_messages_to_converse_api(message_history)
    
    response = bedrock.converse(
        modelId="anthropic.claude-3-sonnet-20240229-v1:0",
        messages=messages,
        inferenceConfig={
            "maxTokens": 2000,
            "temperature": 0,
            "topP": 0.9,
            "stopSequences": []
        },
        toolConfig={
            "tools": tool_list
        }
    )
    
    response_message = response['output']['message']
    
    tool_used, output = process_tool(response_message, messages, bedrock, tool_list)
    
    if not tool_used: #just use the original non-RAG result if no tool was needed
        output = response['output']['message']['content'][0]['text']
    
    
    print("----FINAL RESPONSE----")
    print(output)
    
    response_chat_message = ChatMessage('assistant', output)
    
    message_history.append(response_chat_message)
    
    return