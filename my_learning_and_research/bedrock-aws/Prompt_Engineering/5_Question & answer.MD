# Prompt exercises
You can use the copy buttons in the boxes below to automatically copy the prompt. Paste each prompt and submit one at a time into the prompt app.

## Question & answer without context
Large language models are trained from content collected at some point in the past. This could be as recently as a few months ago, or several years ago. So if something didn’t exist when the content was collected, the large language model won’t know about it. This might lead to a hallucinated (made-up) answer, or the model saying it doesn’t know.

            All models
            What are the key security and privacy features of Amazon Bedrock?

            How do we solve this problem? We need to provide the model with context to understand what we’re asking about.

## Question & answer with context
With context, we help the model access relevant information, so that it can correctly answer questions. This might be done with Retrieval Augmented Generation, or by directly stuffing a fixed set of information into the prompt, like below:

        All models
        {context}

        What are the key security and privacy features of Amazon Bedrock?

Let the model know it’s OK to not know the answer
You can also give the model an escape hatch, if it doesn’t know the answer:

            All models
            What is Amazon Grandstand? If you don't know the answer, simply say "I don't know":

Influencing the tone and content of the response

By default, a foundation model will communicate in a similar manner to the content it was trained on. This might average out to a response appropriate for an adult with a high-school level education. But what if you want to adjust the level to be more appropriate for a younger audience, or change the tone to be more friendly? You can influence the response by:

- Telling the model what its target audience is
- Giving the model a role to play when generating its response
- Encouraging the model to write its response in a certain way

## Write for a business audience
You can also set a constraint for how the model answers the question. Below, we ask the model to generate an answer appropriate for the target audience:

            All models
            {context}

            What is Amazon Bedrock? Explain using non-technical terms for a business audience:

## Write for a young audience
You can also use this technique to answer in an age-appropriate way:

            All models
            {context}

            What is Amazon Bedrock? Explain in terms a young child can understand:

## Role-playing
You can also influence the answer by giving the model a role to play:

            All models
            {context}

            You are a third-grade teacher. You patiently answer in terms that young children can understand. Answer the following question:

            What is Amazon Bedrock?

## Encouragement
You can also encourage the model to answer in the desired manner by telling it how good it is:

        All models
        {context}

        You are an amazing explainer of complex topics to young people. You are going to a great job answering the following question in terms a young child can understand!

        What is Amazon Bedrock?