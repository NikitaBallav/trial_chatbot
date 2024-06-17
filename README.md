# trial_chatbot
### 1. Existing Background of the Application:

Generative models, especially transformer-based ones like ChatGPT, have demonstrated proficiency in generating diverse and contextually relevant responses. However, their reliability may be compromised when compared to retrieval-based approaches. A significant drawback of chatbots, in general, is their lack of research skills. They operate solely based on existing data and may generate fictitious information for unknown queries. Moreover, they struggle to retain information without continuous training, which can be resource-intensive.

### 2. Prerequisites:

Before using the chatbot, ensure the following prerequisites are met:

- Python environment is set up.
- Rasa is installed using the command: `pip install rasa`.
- Initialize Rasa project using: `rasa init`.
- with 'rasa init' the default rasa moodbot will get loaded in your open workspace.
- after loading the rasa moodbot modify the data folder as per your requirements.

### 3. Modification:

1. **Training Data:**
   - Customize the NLU (Natural Language Understanding) data in the `data/nlu.yml` file to include examples relevant to your domain.

2. **Responses:**
   - Modify the responses in the `domain.yml` file to tailor them to your specific legal domain.

3. **Custom Actions:**
   - If you have specific actions or functionalities, implement custom actions in the `actions.py` file.

5. **Do the necessary updation for the rest of the files as did in this repo**
6. **As mention in the action file about the SQL database:**
   - The responses for the queries in the nlu.yml file are saved in a personal sql database, the database has two columns "response" and "corresponding_intent_name".

4. **Training:**
   - After making changes, train the model using the command: `rasa train`.

5. **Testing:**
   - Test the chatbot with sample interactions to ensure it responds appropriately to your customized domain.

6. **Deployment:**
   - Deploy the chatbot in your preferred environment.

