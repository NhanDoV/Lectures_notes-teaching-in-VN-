You may want to limit access to Amazon Bedrock models for various reasons, including enterprise-wide standards, model provider license terms, or cost concerns. Please see some example IAM policy statements below for how to block access to models.

You can learn more about the actions, resources, and condition keys for Amazon Bedrock here: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonbedrock.html 

## Allowing access to subscribe to models
Some Amazon Bedrock model require Marketplace subscriptions prior to use. These subscriptions are activated through the Amazon Bedrock Console’s Model access page. You can limit subscription options using a policy statement like the one below. This example only allows a user to subscribe to Anthropic Claude 3 Sonnet ("prod-6dw3qvchef7zy") and Cohere Command ("a61c46fe-1747-41aa-9af0-2e0ae8a9ce05"):
``` json
        {
            "Effect": "Allow",
            "Action": [
                "aws-marketplace:Subscribe"
            ],
            "Resource": "*",
            "Condition": {
                "ForAnyValue:StringEquals": {
                    "aws-marketplace:ProductId": [
                        "a61c46fe-1747-41aa-9af0-2e0ae8a9ce05",
                        "prod-6dw3qvchef7zy"
                    ]
                }
            }
        }
```
You can view a current list of Amazon Bedrock’s Marketplace product IDs here: https://docs.aws.amazon.com/bedrock/latest/userguide/model-access.html#model-access-permissions 

If the model isn’t included in the list of Marketplace product IDs, it may not require a Marketplace subscription prior to use.

## Allowing invocation of a subset of models
Because Bedrock frequently adds new models, it may be best to explicitly allow models. In the below example, Cohere’s Command V14 and all Anthropic models are enabled.
``` json
        {
            "Sid": "VisualEditor8",
            "Effect": "Allow",
            "Action": [
                "bedrock:InvokeModel",
                "bedrock:InvokeModelWithResponseStream"
            ],
            "Resource": [
                "arn:aws:bedrock:*::foundation-model/anthropic.*",
                "arn:aws:bedrock:*::foundation-model/cohere.command-text-v14"
            ]
        }
```
You can view a current list of Amazon Bedrock’s model IDs here: https://docs.aws.amazon.com/bedrock/latest/userguide/model-ids.html 

Learn more
You can see additional examples in the official Amazon Bedrock documentation: https://docs.aws.amazon.com/bedrock/latest/userguide/security_iam_id-based-policy-examples.html 
