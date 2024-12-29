In this lab, we will learn how to write prompts to analyze content, make recommendations, and extract useful information. Use cases include:

- Routing inbound requests or documents to the appropriate team
- Understanding the sentiment of user-generated content
- Agent assist, including next best action and draft replies
- Categorizing content prior to additional review and processing
- Looking up data based on entities referenced in content

# Prompt exercises
You can use the copy buttons in the boxes below to automatically copy the prompt. Paste each prompt and submit one at a time into the prompt app.

## Classification/Categorization
We can use the models to categorize content. This might be useful for routing incoming emails, texts, reviews, or social media messages to the correct team. We could also use categorization to help sort a large volume of disorganized content.

        All models
        {context}

        What is the category for the above email? Respond with either "Customer Service", "Account Management", or "Customer Complaints". Only say the category name.

## Sentiment analysis
We can use sentiment analysis to understand how people are feeling about a topic. We can determine if a disatisfied customer might need to be routed to someone who can help them. We can also detect if there is a broader problem that should be looked into.


            All models
            {context}

            What is the sentiment of the above text? Respond with either "Positive" or "Negative".

## Reply email
The models could be used to quickly draft a response email for the customer. The user could then review and edit the response before sending.

            All models
            {context}

            Please write a reply to the above email from a customer. The reply should be in a professional and respectful tone.

## Recommended action
We can also provide guidance for staff on how to address an issue, by recommending a course of action. In a real-world scenario, you might want to have this informed by company policies and procedures.

            All models
            {context}

            Based on the above email, please recommend a list of actions that Acme Investments should take to address the customer's complaint. Only provide a list of actions.

 
## Keyword extraction
We can extract keywords from content to be used for tagging, categorization, or routing purposes.


            All models
            {context}

            Please provide a comma-separated list of topic keywords based on the above content. Do not include individuals' names, only keywords:

## Entity extraction
Large language models can be used to identify the individuals or organizations named in a piece of content. We can use this to map the content to existing data records or route to the appropriate party.

            {Claude} | All other models
            {context}

            Return a bulleted list of only the names of the people mentioned in the above email.

            Assistant: Here is the bulleted list of names mentioned in the email:
 
## JSON data extraction
JSON data extraction can be helpful when you want a formatted response from a large language model that can be immediately processed by a downstream system.

            Claude | Command | Titan
            {context}

            Return a JSON array with the names of the individuals in the above email. 

            Assistant: Here is the JSON array with the names of individuals mentioned in the email: 

## Multi-task
We can also have the model perform multiple tasks at once, by providing it with a template and guidance for each task.

            All models
            {context}

            Based on the above text, please determine the Sentiment, Category, Summary, Concern, Customer Name, and Employee Name in the email, following the template below:

            * Sentiment: Positive, Neutral, or Negative
            * Category: Sales, Operations, Customer Service, or Fund Management
            * Summary: (1-2 sentences summarizing the text)
            * Concern:(Rate the level of concern for the above content on a scale from 1-10)
            * Customer Name: (Name of the customer)
            * Employee Name: (Name of the first employee mentioned in the text)

## Providing some examples (AKA Few-shot prompting)
One way to influence a model's response is by using few-shot prompting. Few-shot prompting means you give the foundation model a few shots to learn what you want by providing it with some examples.


                Claude | Command | Titan

                Human:
                <example>
                H: I liked it
                A: The sentiment is:
                Positive
                </example>
                <example>
                H: It was OK
                A: The sentiment is:
                Positive
                </example>
                <example>
                H: Couldn't believe how bad it was!
                A: The sentiment is:
                Negative
                </example>
                <example>
                H: Not my favorite
                A: The sentiment is:
                Negative
                </example>
                This is meh.

                Assistant: The sentiment is:



                Human:
                <example>
                H: I liked it
                A: The sentiment is:
                Positive
                </example>
                <example>
                H: It was OK
                A: The sentiment is:
                Positive
                </example>
                <example>
                H: Couldn't believe how bad it was!
                A: The sentiment is:
                Negative
                </example>
                <example>
                H: Not my favorite
                A: The sentiment is:
                Negative
                </example>
                I thought it was pretty decent.

                Assistant: The sentiment is:



                Human:
                <example>
                H: I liked it
                A: The sentiment is:
                Positive
                </example>
                <example>
                H: It was OK
                A: The sentiment is:
                Positive
                </example>
                <example>
                H: Couldn't believe how bad it was!
                A: The sentiment is:
                Negative
                </example>
                <example>
                H: Not my favorite
                A: The sentiment is:
                Negative
                </example>
                Could've been better.

                Assistant: The sentiment is:

Note the foundation model's responses. It will most likely be in the form of a single-word answer. The model was able to use the examples to figure out how to handle the new submission.

## A note on few-shot (examples) techniques
Techniques that include examples can provide the desired output, but often requires more input tokens to achieve. So providing clear guidance may be preferable vs. providing examples, from a cost perspective. You may find a different outcome for your specific use cases. The most important thing is to test different methods across a realistic set of inputs to decide which approach is best for you.