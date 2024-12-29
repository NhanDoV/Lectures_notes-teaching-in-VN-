import sys
import boto3

def get_text_response(model, input_content):

    session = boto3.Session()
    bedrock = session.client(service_name='bedrock-runtime')
    
    message = {
        "role": "user",
        "content": [ { "text": input_content } ]
    }
    
    response = bedrock.converse(
        modelId=model,
        messages=[message],
        inferenceConfig={
            "maxTokens": 2000,
            "temperature": 0,
            "topP": 0.9,
            "stopSequences": []
        },
    )
    
    return response['output']['message']['content'][0]['text']
    
response = get_text_response(sys.argv[1], sys.argv[2])
print(response)