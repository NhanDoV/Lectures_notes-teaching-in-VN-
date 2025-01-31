import boto3
def get_text_response(model, input_content, temperature, top_p, max_token_count):

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
            "maxTokens": max_token_count,
            "temperature": temperature,
            "topP": top_p,
        },
    )
    
    return response['output']['message']['content'][0]['text']