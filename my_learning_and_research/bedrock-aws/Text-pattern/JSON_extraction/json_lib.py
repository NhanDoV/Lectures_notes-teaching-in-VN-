import boto3

def get_tools():
    tools = [
        {
            "toolSpec": {
                "name": "summarize_email",
                "description": "Summarize email content.",
                "inputSchema": {
                    "json": {
                        "type": "object",
                        "properties": {
                            "summary": {
                                "type": "string",
                                "description": "A brief one-line or two-line summary of the email."
                            },
                            "escalate_complaint": {
                                "type": "boolean",
                                "description": "Indicates if this email is serious enough to be immediately escalated for further review."
                            },
                            "level_of_concern": {
                                "type": "integer",
                                "description": "Rate the level of concern for the above content on a scale from 1-10",
                                "minimum": 1,
                                "maximum": 10
                            },
                            "overall_sentiment": {
                                "type": "string",
                                "description": "The sender's overall sentiment.",
                                "enum": ["Positive", "Neutral", "Negative"]
                            },
                            "supporting_business_unit": {
                                "type": "string",
                                "description": "The internal business unit that this email should be routed to.",
                                "enum": ["Sales", "Operations", "Customer Service", "Fund Management"]
                            },
                            "customer_names": {
                                "type": "array",
                                "description": "An array of customer names mentioned in the email.",
                                "items": { "type": "string" }
                            },
                            "sentiment_towards_employees": {
                                "type": "array",
                                "items": {
                                    "type": "object",
                                    "properties": {
                                        "employee_name": {
                                            "type": "string",
                                            "description": "The employee's name."
                                        },
                                        "sentiment": {
                                            "type": "string",
                                            "description": "The sender's sentiment towards the employee.",
                                            "enum": ["Positive", "Neutral", "Negative"]
                                        }
                                    }
                                }
                            }
                        },
                        "required": [
                            "summary",
                            "escalate_complaint",
                            "overall_sentiment",
                            "supporting_business_unit",
                            "level_of_concern",
                            "customer_names",
                            "sentiment_towards_employees"
                        ]
                    }
                }
            }
        }
    ]

    return tools

def get_json_response(input_content): #text-to-text client function

    session = boto3.Session()
    bedrock = session.client(service_name='bedrock-runtime')
    
    tool_list = get_tools()
    
    message = {
        "role": "user",
        "content": [
            { "text": f"<content>{input_content}</content>" },
            { "text": "Please use the summarize_email tool to generate the email summary JSON based on the content within the <content> tags." }
        ],
    }
    
    response = bedrock.converse(
        modelId="anthropic.claude-3-sonnet-20240229-v1:0",
        messages=[message],
        inferenceConfig={
            "maxTokens": 2000,
            "temperature": 0
        },
        toolConfig={
            "tools": tool_list,
            "toolChoice": {
                "tool": {
                    "name": "summarize_email"
                }
            }
        }
    )
    
    
    response_message = response['output']['message']
    response_content_blocks = response_message['content']
    content_block = next((block for block in response_content_blocks if 'toolUse' in block), None)
    tool_use_block = content_block['toolUse']
    tool_result_dict = tool_use_block['input']
    
    return tool_result_dict