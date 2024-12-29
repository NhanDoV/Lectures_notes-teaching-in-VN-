Final product:

![alt text](images/image_6_01.png)

# Lab introduction
In this lab, we will test some prompt attack scenarios with a basic Streamlit app.

Prompt attacks can include:

- Attempting to get around an LLM’s safeguards (jailbreaking)
- Tricking the model into fulfilling a malicious request (prompt injection)

Prompt attack filters require the use of input tagging at invocation time to correctly differentiate developer instructions from user-provided content. You can learn more about input tagging in the Invoking models with guardrails lab.

### Note
You can view the source code for this lab under the workshop/completed/guardrails folder, in the following files:

                create_attack_guardrail.py
                guardrails_app.py
                guardrails_lib.py

## Defining prompt attack policies
See below for the relevant parameters of the create_guardrail method. You can see the full documentation for the create_guardrail method here: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/client/create_guardrail.html 

## Prompt attack filters
Prompt attack filters are defined using the contentPolicyConfig parameter. In this section, you define how to handle toxic content. For each category, you define how strong the filter is applied for both incoming prompts from the user and outgoing responses from the model. The PROMPT_ATTACK type is how we configure prompt attack protection. See below for the request syntax definition.
```python
contentPolicyConfig={
    'filtersConfig': [
        {
            'type': 'SEXUAL'|'VIOLENCE'|'HATE'|'INSULTS'|'MISCONDUCT'|'PROMPT_ATTACK',
            'inputStrength': 'NONE'|'LOW'|'MEDIUM'|'HIGH',
            'outputStrength': 'NONE'|'LOW'|'MEDIUM'|'HIGH'
        },
    ]
},
```
In our demo guardrail, we configure the content filters like below. Prompt attack filters are only applied on the prompt, so the outputStrength for PROMPT_ATTACK must be "NONE". 
```python
contentPolicyConfig={
    'filtersConfig': [
        {"type": "PROMPT_ATTACK", "inputStrength": "HIGH", "outputStrength": "NONE"},
    ]
},
```

## Create the guardrail
Select the bash terminal in AWS Cloud9 and change directory.
``` bash
cd ~/environment/workshop/labs/guardrails
``` 
Run the create guardrails script.
``` python
python ~/environment/workshop/completed/guardrails/create_attack_guardrail.py
```
This should save the newly created guardrail ID to the appropriate setting in the local INI file.

The guardrail is now ready to be used by the guardrail testing app.

## Test the guardrail
Run the streamlit command from the terminal.
```python
streamlit run guardrails_app.py --server.port 8080 prompt_attack_guardrail_id
```
Ignore the Network URL and External URL links displayed by the Streamlit command. Instead, we will use AWS Cloud9's preview feature.

In AWS Cloud9, select Preview -> Preview Running Application.

![alt text](images/image_6_02.png)

You should see a web page like below:
![alt text](images/image_6_03.png)

Try the following prompts. You can review the guardrail action and trace details in the right-hand column of the app.
![alt text](images/image_6_04.png)

Close the preview tab in AWS Cloud9. Return to the terminal and press Control-C to exit the application.
