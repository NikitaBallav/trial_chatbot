from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import pandas as pd
import random
import os
import MySQLdb
from dotenv import load_dotenv
import pandas as pd

# Load environment variables from .env file
load_dotenv()

# Create the connection object
conn = MySQLdb.connect(
    host=os.environ.get("HOST", "localhost"),
    user=os.environ.get("USER", "root"),
    passwd=os.environ.get("PASSWORD", "XXXXXX032001"),
    db=os.environ.get("DATABASE", "database_name"),
    ssl_mode='DISABLED'  # Disable SSL certificate validation
)

class action_greet_db(Action):
    def name(self) -> Text:
        return "action_greet_db"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        query= "SELECT chatbot_responses FROM engdata.chatbot WHERE intent_group_name = 'greet'"
        responses_list= pd.read_sql_query(query, conn)

        random_response = random.choice(responses_list['chatbot_responses'])

        dispatcher.utter_message(text=random_response)

        return []


class action_goodbye_db(Action):
    def name(self) -> Text:
        return "action_goodbye_db"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        query= "SELECT chatbot_responses FROM engdata.chatbot WHERE intent_group_name = 'goodbye'"
        responses_list= pd.read_sql_query(query, conn)

        random_response = random.choice(responses_list['chatbot_responses'])

        dispatcher.utter_message(text=random_response)

        return []

class action_happy_db(Action):
    def name(self) -> Text:
        return "action_happy_db"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        query= "SELECT chatbot_responses FROM engdata.chatbot WHERE intent_group_name = 'happy'"
        responses_list= pd.read_sql_query(query, conn)

        random_response = random.choice(responses_list['chatbot_responses'])

        dispatcher.utter_message(text=random_response)

        return []

class action_sorry_db(Action):
    def name(self) -> Text:
        return "action_sorry_db"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        query= "SELECT chatbot_responses FROM engdata.chatbot WHERE intent_group_name = 'sad'"
        responses_list= pd.read_sql_query(query, conn)

        random_response = random.choice(responses_list['chatbot_responses'])

        dispatcher.utter_message(text=random_response)

        return []

class action_ans1_db(Action):
    def name(self) -> Text:
        return "action_ans1_db"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        query= "SELECT chatbot_responses FROM engdata.chatbot WHERE intent_group_name = 'q1'"
        responses_list= pd.read_sql_query(query, conn)

        random_response = random.choice(responses_list['chatbot_responses'])

        dispatcher.utter_message(text=random_response)

        return []

class action_ans2_db(Action):
    def name(self) -> Text:
        return "action_ans2_db"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        query= "SELECT chatbot_responses FROM engdata.chatbot WHERE intent_group_name = 'q2'"
        responses_list= pd.read_sql_query(query, conn)

        random_response = random.choice(responses_list['chatbot_responses'])

        dispatcher.utter_message(text=random_response)

        return []

class action_ans3_db(Action):
    def name(self) -> Text:
        return "action_ans3_db"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        query= "SELECT chatbot_responses FROM engdata.chatbot WHERE intent_group_name = 'q3'"
        responses_list= pd.read_sql_query(query, conn)

        random_response = random.choice(responses_list['chatbot_responses'])

        dispatcher.utter_message(text=random_response)

        return []

class action_ans4_db(Action):
    def name(self) -> Text:
        return "action_ans4_db"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        query= "SELECT chatbot_responses FROM engdata.chatbot WHERE intent_group_name = 'q4'"
        responses_list= pd.read_sql_query(query, conn)

        random_response = random.choice(responses_list['chatbot_responses'])

        dispatcher.utter_message(text=random_response)

        return []

class action_ans5_db(Action):
    def name(self) -> Text:
        return "action_ans5_db"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        query= "SELECT chatbot_responses FROM engdata.chatbot WHERE intent_group_name = 'q5'"
        responses_list= pd.read_sql_query(query, conn)

        random_response = random.choice(responses_list['chatbot_responses'])

        dispatcher.utter_message(text=random_response)

        return []

class action_ans6_db(Action):
    def name(self) -> Text:
        return "action_ans6_db"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        query= "SELECT chatbot_responses FROM engdata.chatbot WHERE intent_group_name = 'q6'"
        responses_list= pd.read_sql_query(query, conn)

        random_response = random.choice(responses_list['chatbot_responses'])

        dispatcher.utter_message(text=random_response)

        return []

class action_ans7_db(Action):
    def name(self) -> Text:
        return "action_ans7_db"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        query= "SELECT chatbot_responses FROM engdata.chatbot WHERE intent_group_name = 'q7'"
        responses_list= pd.read_sql_query(query, conn)

        random_response = random.choice(responses_list['chatbot_responses'])

        dispatcher.utter_message(text=random_response)

        return []

class action_ans8_db(Action):
    def name(self) -> Text:
        return "action_ans8_db"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        query= "SELECT chatbot_responses FROM engdata.chatbot WHERE intent_group_name = 'q8'"
        responses_list= pd.read_sql_query(query, conn)

        random_response = random.choice(responses_list['chatbot_responses'])

        dispatcher.utter_message(text=random_response)

        return []

class action_ans9_db(Action):
    def name(self) -> Text:
        return "action_ans9_db"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        query= "SELECT chatbot_responses FROM engdata.chatbot WHERE intent_group_name = 'q9'"
        responses_list= pd.read_sql_query(query, conn)

        random_response = random.choice(responses_list['chatbot_responses'])

        dispatcher.utter_message(text=random_response)

        return []

class action_ans10_db(Action):
    def name(self) -> Text:
        return "action_ans10_db"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        query= "SELECT chatbot_responses FROM engdata.chatbot WHERE intent_group_name = 'q10'"
        responses_list= pd.read_sql_query(query, conn)

        random_response = random.choice(responses_list['chatbot_responses'])

        dispatcher.utter_message(text=random_response)

        return []

class action_ans11_db(Action):
    def name(self) -> Text:
        return "action_ans11_db"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        query= "SELECT chatbot_responses FROM engdata.chatbot WHERE intent_group_name = 'q11'"
        responses_list= pd.read_sql_query(query, conn)

        random_response = random.choice(responses_list['chatbot_responses'])

        dispatcher.utter_message(text=random_response)

        return []

class action_ans12_db(Action):
    def name(self) -> Text:
        return "action_ans12_db"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        query= "SELECT chatbot_responses FROM engdata.chatbot WHERE intent_group_name = 'q12'"
        responses_list= pd.read_sql_query(query, conn)

        random_response = random.choice(responses_list['chatbot_responses'])

        dispatcher.utter_message(text=random_response)

        return []

class action_ans13_db(Action):
    def name(self) -> Text:
        return "action_ans13_db"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        query= "SELECT chatbot_responses FROM engdata.chatbot WHERE intent_group_name = 'q13'"
        responses_list= pd.read_sql_query(query, conn)

        random_response = random.choice(responses_list['chatbot_responses'])

        dispatcher.utter_message(text=random_response)

        return []

class action_ans14_db(Action):
    def name(self) -> Text:
        return "action_ans14_db"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        query= "SELECT chatbot_responses FROM engdata.chatbot WHERE intent_group_name = 'q14'"
        responses_list= pd.read_sql_query(query, conn)

        random_response = random.choice(responses_list['chatbot_responses'])

        dispatcher.utter_message(text=random_response)

        return []

class action_ans15_db(Action):
    def name(self) -> Text:
        return "action_ans15_db"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        query= "SELECT chatbot_responses FROM engdata.chatbot WHERE intent_group_name = 'q15'"
        responses_list= pd.read_sql_query(query, conn)

        random_response = random.choice(responses_list['chatbot_responses'])

        dispatcher.utter_message(text=random_response)

        return []

class action_ans16_db(Action):
    def name(self) -> Text:
        return "action_ans16_db"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        query= "SELECT chatbot_responses FROM engdata.chatbot WHERE intent_group_name = 'q16'"
        responses_list= pd.read_sql_query(query, conn)

        random_response = random.choice(responses_list['chatbot_responses'])

        dispatcher.utter_message(text=random_response)

        return []

class action_ans17_db(Action):
    def name(self) -> Text:
        return "action_ans17_db"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        query= "SELECT chatbot_responses FROM engdata.chatbot WHERE intent_group_name = 'q17'"
        responses_list= pd.read_sql_query(query, conn)

        random_response = random.choice(responses_list['chatbot_responses'])

        dispatcher.utter_message(text=random_response)

        return []

class action_ans18_db(Action):
    def name(self) -> Text:
        return "action_ans18_db"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        query= "SELECT chatbot_responses FROM engdata.chatbot WHERE intent_group_name = 'q18'"
        responses_list= pd.read_sql_query(query, conn)

        random_response = random.choice(responses_list['chatbot_responses'])

        dispatcher.utter_message(text=random_response)

        return []

class action_ans19_db(Action):
    def name(self) -> Text:
        return "action_ans19_db"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        query= "SELECT chatbot_responses FROM engdata.chatbot WHERE intent_group_name = 'q19'"
        responses_list= pd.read_sql_query(query, conn)

        random_response = random.choice(responses_list['chatbot_responses'])

        dispatcher.utter_message(text=random_response)

        return []

class action_ans20_db(Action):
    def name(self) -> Text:
        return "action_ans20_db"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        query= "SELECT chatbot_responses FROM engdata.chatbot WHERE intent_group_name = 'q20'"
        responses_list= pd.read_sql_query(query, conn)

        random_response = random.choice(responses_list['chatbot_responses'])

        dispatcher.utter_message(text=random_response)

        return []

class action_ans21_db(Action):
    def name(self) -> Text:
        return "action_ans21_db"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        query= "SELECT chatbot_responses FROM engdata.chatbot WHERE intent_group_name = 'q21'"
        responses_list= pd.read_sql_query(query, conn)

        random_response = random.choice(responses_list['chatbot_responses'])

        dispatcher.utter_message(text=random_response)

        return []

class action_ans22_db(Action):
    def name(self) -> Text:
        return "action_ans22_db"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        query= "SELECT chatbot_responses FROM engdata.chatbot WHERE intent_group_name = 'q22'"
        responses_list= pd.read_sql_query(query, conn)

        random_response = random.choice(responses_list['chatbot_responses'])

        dispatcher.utter_message(text=random_response)

        return []

class action_ans23_db(Action):
    def name(self) -> Text:
        return "action_ans23_db"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        query= "SELECT chatbot_responses FROM engdata.chatbot WHERE intent_group_name = 'q23'"
        responses_list= pd.read_sql_query(query, conn)

        random_response = random.choice(responses_list['chatbot_responses'])

        dispatcher.utter_message(text=random_response)

        return []

class action_ans24_db(Action):
    def name(self) -> Text:
        return "action_ans24_db"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        query= "SELECT chatbot_responses FROM engdata.chatbot WHERE intent_group_name = 'q24'"
        responses_list= pd.read_sql_query(query, conn)

        random_response = random.choice(responses_list['chatbot_responses'])

        dispatcher.utter_message(text=random_response)

        return []

class action_ans25_db(Action):
    def name(self) -> Text:
        return "action_ans25_db"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        query= "SELECT chatbot_responses FROM engdata.chatbot WHERE intent_group_name = 'q25'"
        responses_list= pd.read_sql_query(query, conn)

        random_response = random.choice(responses_list['chatbot_responses'])

        dispatcher.utter_message(text=random_response)

        return []

class action_ans26_db(Action):
    def name(self) -> Text:
        return "action_ans26_db"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        query= "SELECT chatbot_responses FROM engdata.chatbot WHERE intent_group_name = 'q26'"
        responses_list= pd.read_sql_query(query, conn)

        random_response = random.choice(responses_list['chatbot_responses'])

        dispatcher.utter_message(text=random_response)

        return []

class action_ans27_db(Action):
    def name(self) -> Text:
        return "action_ans27_db"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        query= "SELECT chatbot_responses FROM engdata.chatbot WHERE intent_group_name = 'q27'"
        responses_list= pd.read_sql_query(query, conn)

        random_response = random.choice(responses_list['chatbot_responses'])

        dispatcher.utter_message(text=random_response)

        return []

class action_ans28_db(Action):
    def name(self) -> Text:
        return "action_ans28_db"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        query= "SELECT chatbot_responses FROM engdata.chatbot WHERE intent_group_name = 'q28'"
        responses_list= pd.read_sql_query(query, conn)

        random_response = random.choice(responses_list['chatbot_responses'])

        dispatcher.utter_message(text=random_response)

        return []

class action_ans29_db(Action):
    def name(self) -> Text:
        return "action_ans29_db"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        query= "SELECT chatbot_responses FROM engdata.chatbot WHERE intent_group_name = 'q29'"
        responses_list= pd.read_sql_query(query, conn)

        random_response = random.choice(responses_list['chatbot_responses'])

        dispatcher.utter_message(text=random_response)

        return []

class action_ans30_db(Action):
    def name(self) -> Text:
        return "action_ans30_db"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        query= "SELECT chatbot_responses FROM engdata.chatbot WHERE intent_group_name = 'q30'"
        responses_list= pd.read_sql_query(query, conn)

        random_response = random.choice(responses_list['chatbot_responses'])

        dispatcher.utter_message(text=random_response)

        return []

class action_ans31_db(Action):
    def name(self) -> Text:
        return "action_ans31_db"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        query= "SELECT chatbot_responses FROM engdata.chatbot WHERE intent_group_name = 'q31'"
        responses_list= pd.read_sql_query(query, conn)

        random_response = random.choice(responses_list['chatbot_responses'])

        dispatcher.utter_message(text=random_response)

        return []

class action_ans32_db(Action):
    def name(self) -> Text:
        return "action_ans32_db"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        query= "SELECT chatbot_responses FROM engdata.chatbot WHERE intent_group_name = 'q32'"
        responses_list= pd.read_sql_query(query, conn)

        random_response = random.choice(responses_list['chatbot_responses'])

        dispatcher.utter_message(text=random_response)

        return []

class action_ans33_db(Action):
    def name(self) -> Text:
        return "action_ans33_db"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        query= "SELECT chatbot_responses FROM engdata.chatbot WHERE intent_group_name = 'q33'"
        responses_list= pd.read_sql_query(query, conn)

        random_response = random.choice(responses_list['chatbot_responses'])

        dispatcher.utter_message(text=random_response)

        return []

class action_ans34_db(Action):
    def name(self) -> Text:
        return "action_ans34_db"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        query= "SELECT chatbot_responses FROM engdata.chatbot WHERE intent_group_name = 'q34'"
        responses_list= pd.read_sql_query(query, conn)

        random_response = random.choice(responses_list['chatbot_responses'])

        dispatcher.utter_message(text=random_response)

        return []

class action_ans35_db(Action):
    def name(self) -> Text:
        return "action_ans35_db"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        query= "SELECT chatbot_responses FROM engdata.chatbot WHERE intent_group_name = 'q35'"
        responses_list= pd.read_sql_query(query, conn)

        random_response = random.choice(responses_list['chatbot_responses'])

        dispatcher.utter_message(text=random_response)

        return []

class action_ans36_db(Action):
    def name(self) -> Text:
        return "action_ans36_db"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        query= "SELECT chatbot_responses FROM engdata.chatbot WHERE intent_group_name = 'q36'"
        responses_list= pd.read_sql_query(query, conn)

        random_response = random.choice(responses_list['chatbot_responses'])

        dispatcher.utter_message(text=random_response)

        return []

class action_ans37_db(Action):
    def name(self) -> Text:
        return "action_ans37_db"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        query= "SELECT chatbot_responses FROM engdata.chatbot WHERE intent_group_name = 'q37'"
        responses_list= pd.read_sql_query(query, conn)

        random_response = random.choice(responses_list['chatbot_responses'])

        dispatcher.utter_message(text=random_response)

        return []

class action_ans38_db(Action):
    def name(self) -> Text:
        return "action_ans38_db"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        query= "SELECT chatbot_responses FROM engdata.chatbot WHERE intent_group_name = 'q38'"
        responses_list= pd.read_sql_query(query, conn)

        random_response = random.choice(responses_list['chatbot_responses'])

        dispatcher.utter_message(text=random_response)

        return []

class action_ans39_db(Action):
    def name(self) -> Text:
        return "action_ans39_db"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        query= "SELECT chatbot_responses FROM engdata.chatbot WHERE intent_group_name = 'q39'"
        responses_list= pd.read_sql_query(query, conn)

        random_response = random.choice(responses_list['chatbot_responses'])

        dispatcher.utter_message(text=random_response)

        return []

class action_ans40_db(Action):
    def name(self) -> Text:
        return "action_ans40_db"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        query= "SELECT chatbot_responses FROM engdata.chatbot WHERE intent_group_name = 'q40'"
        responses_list= pd.read_sql_query(query, conn)

        random_response = random.choice(responses_list['chatbot_responses'])

        dispatcher.utter_message(text=random_response)

        return []

class action_ans41_db(Action):
    def name(self) -> Text:
        return "action_ans41_db"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        query= "SELECT chatbot_responses FROM engdata.chatbot WHERE intent_group_name = 'q41'"
        responses_list= pd.read_sql_query(query, conn)

        random_response = random.choice(responses_list['chatbot_responses'])

        dispatcher.utter_message(text=random_response)

        return []

class action_ans42_db(Action):
    def name(self) -> Text:
        return "action_ans42_db"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        query= "SELECT chatbot_responses FROM engdata.chatbot WHERE intent_group_name = 'q42'"
        responses_list= pd.read_sql_query(query, conn)

        random_response = random.choice(responses_list['chatbot_responses'])

        dispatcher.utter_message(text=random_response)

        return []

class action_ans43_db(Action):
    def name(self) -> Text:
        return "action_ans43_db"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        query= "SELECT chatbot_responses FROM engdata.chatbot WHERE intent_group_name = 'q43'"
        responses_list= pd.read_sql_query(query, conn)

        random_response = random.choice(responses_list['chatbot_responses'])

        dispatcher.utter_message(text=random_response)

        return []

class action_ans44_db(Action):
    def name(self) -> Text:
        return "action_ans44_db"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        query= "SELECT chatbot_responses FROM engdata.chatbot WHERE intent_group_name = 'q44'"
        responses_list= pd.read_sql_query(query, conn)

        random_response = random.choice(responses_list['chatbot_responses'])

        dispatcher.utter_message(text=random_response)

        return []

class action_ans45_db(Action):
    def name(self) -> Text:
        return "action_ans45_db"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        query= "SELECT chatbot_responses FROM engdata.chatbot WHERE intent_group_name = 'q45'"
        responses_list= pd.read_sql_query(query, conn)

        random_response = random.choice(responses_list['chatbot_responses'])

        dispatcher.utter_message(text=random_response)

        return []

class action_ans46_db(Action):
    def name(self) -> Text:
        return "action_ans46_db"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        query= "SELECT chatbot_responses FROM engdata.chatbot WHERE intent_group_name = 'q46'"
        responses_list= pd.read_sql_query(query, conn)

        random_response = random.choice(responses_list['chatbot_responses'])

        dispatcher.utter_message(text=random_response)

        return []

class action_ans47_db(Action):
    def name(self) -> Text:
        return "action_ans47_db"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        query= "SELECT chatbot_responses FROM engdata.chatbot WHERE intent_group_name = 'q47'"
        responses_list= pd.read_sql_query(query, conn)

        random_response = random.choice(responses_list['chatbot_responses'])

        dispatcher.utter_message(text=random_response)

        return []

class action_ans48_db(Action):
    def name(self) -> Text:
        return "action_ans48_db"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        query= "SELECT chatbot_responses FROM engdata.chatbot WHERE intent_group_name = 'q48'"
        responses_list= pd.read_sql_query(query, conn)

        random_response = random.choice(responses_list['chatbot_responses'])

        dispatcher.utter_message(text=random_response)

        return []

class action_ans49_db(Action):
    def name(self) -> Text:
        return "action_ans49_db"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        query= "SELECT chatbot_responses FROM engdata.chatbot WHERE intent_group_name = 'q49'"
        responses_list= pd.read_sql_query(query, conn)

        random_response = random.choice(responses_list['chatbot_responses'])

        dispatcher.utter_message(text=random_response)

        return []

class action_ans50_db(Action):
    def name(self) -> Text:
        return "action_ans50_db"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        query= "SELECT chatbot_responses FROM engdata.chatbot WHERE intent_group_name = 'q50'"
        responses_list= pd.read_sql_query(query, conn)

        random_response = random.choice(responses_list['chatbot_responses'])

        dispatcher.utter_message(text=random_response)

        return []

class action_ans51_db(Action):
    def name(self) -> Text:
        return "action_ans51_db"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        query= "SELECT chatbot_responses FROM engdata.chatbot WHERE intent_group_name = 'q51'"
        responses_list= pd.read_sql_query(query, conn)

        random_response = random.choice(responses_list['chatbot_responses'])

        dispatcher.utter_message(text=random_response)

        return []

class action_ans52_db(Action):
    def name(self) -> Text:
        return "action_ans52_db"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        query= "SELECT chatbot_responses FROM engdata.chatbot WHERE intent_group_name = 'q52'"
        responses_list= pd.read_sql_query(query, conn)

        random_response = random.choice(responses_list['chatbot_responses'])

        dispatcher.utter_message(text=random_response)

        return []

class action_ans53_db(Action):
    def name(self) -> Text:
        return "action_ans53_db"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        query= "SELECT chatbot_responses FROM engdata.chatbot WHERE intent_group_name = 'q53'"
        responses_list= pd.read_sql_query(query, conn)

        random_response = random.choice(responses_list['chatbot_responses'])

        dispatcher.utter_message(text=random_response)

        return []

class action_ans54_db(Action):
    def name(self) -> Text:
        return "action_ans54_db"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        query= "SELECT chatbot_responses FROM engdata.chatbot WHERE intent_group_name = 'q54'"
        responses_list= pd.read_sql_query(query, conn)

        random_response = random.choice(responses_list['chatbot_responses'])

        dispatcher.utter_message(text=random_response)

        return []

class action_ans55_db(Action):
    def name(self) -> Text:
        return "action_ans55_db"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        query= "SELECT chatbot_responses FROM engdata.chatbot WHERE intent_group_name = 'q55'"
        responses_list= pd.read_sql_query(query, conn)

        random_response = random.choice(responses_list['chatbot_responses'])

        dispatcher.utter_message(text=random_response)

        return []

class action_ans56_db(Action):
    def name(self) -> Text:
        return "action_ans56_db"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        query= "SELECT chatbot_responses FROM engdata.chatbot WHERE intent_group_name = 'q56'"
        responses_list= pd.read_sql_query(query, conn)

        random_response = random.choice(responses_list['chatbot_responses'])

        dispatcher.utter_message(text=random_response)

        return []

class action_ans57_db(Action):
    def name(self) -> Text:
        return "action_ans57_db"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        query= "SELECT chatbot_responses FROM engdata.chatbot WHERE intent_group_name = 'q57'"
        responses_list= pd.read_sql_query(query, conn)

        random_response = random.choice(responses_list['chatbot_responses'])

        dispatcher.utter_message(text=random_response)

        return []

class action_ans58_db(Action):
    def name(self) -> Text:
        return "action_ans58_db"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        query= "SELECT chatbot_responses FROM engdata.chatbot WHERE intent_group_name = 'q58'"
        responses_list= pd.read_sql_query(query, conn)

        random_response = random.choice(responses_list['chatbot_responses'])

        dispatcher.utter_message(text=random_response)

        return []

class action_ans59_db(Action):
    def name(self) -> Text:
        return "action_ans59_db"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        query= "SELECT chatbot_responses FROM engdata.chatbot WHERE intent_group_name = 'q59'"
        responses_list= pd.read_sql_query(query, conn)

        random_response = random.choice(responses_list['chatbot_responses'])

        dispatcher.utter_message(text=random_response)

        return []

class action_ans60_db(Action):
    def name(self) -> Text:
        return "action_ans60_db"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        query= "SELECT chatbot_responses FROM engdata.chatbot WHERE intent_group_name = 'q60'"
        responses_list= pd.read_sql_query(query, conn)

        random_response = random.choice(responses_list['chatbot_responses'])

        dispatcher.utter_message(text=random_response)

        return []

class action_ans61_db(Action):
    def name(self) -> Text:
        return "action_ans61_db"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        query= "SELECT chatbot_responses FROM engdata.chatbot WHERE intent_group_name = 'q61'"
        responses_list= pd.read_sql_query(query, conn)

        random_response = random.choice(responses_list['chatbot_responses'])

        dispatcher.utter_message(text=random_response)

        return []

class action_ans62_db(Action):
    def name(self) -> Text:
        return "action_ans62_db"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        query= "SELECT chatbot_responses FROM engdata.chatbot WHERE intent_group_name = 'q62'"
        responses_list= pd.read_sql_query(query, conn)

        random_response = random.choice(responses_list['chatbot_responses'])

        dispatcher.utter_message(text=random_response)

        return []

class action_ans63_db(Action):
    def name(self) -> Text:
        return "action_ans63_db"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        query= "SELECT chatbot_responses FROM engdata.chatbot WHERE intent_group_name = 'q63'"
        responses_list= pd.read_sql_query(query, conn)

        random_response = random.choice(responses_list['chatbot_responses'])

        dispatcher.utter_message(text=random_response)

        return []

class action_ans64_db(Action):
    def name(self) -> Text:
        return "action_ans64_db"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        query= "SELECT chatbot_responses FROM engdata.chatbot WHERE intent_group_name = 'q64'"
        responses_list= pd.read_sql_query(query, conn)

        random_response = random.choice(responses_list['chatbot_responses'])

        dispatcher.utter_message(text=random_response)

        return []

class action_ans65_db(Action):
    def name(self) -> Text:
        return "action_ans65_db"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        query= "SELECT chatbot_responses FROM engdata.chatbot WHERE intent_group_name = 'q65'"
        responses_list= pd.read_sql_query(query, conn)

        random_response = random.choice(responses_list['chatbot_responses'])

        dispatcher.utter_message(text=random_response)

        return []

class action_ans66_db(Action):
    def name(self) -> Text:
        return "action_ans66_db"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        query= "SELECT chatbot_responses FROM engdata.chatbot WHERE intent_group_name = 'q66'"
        responses_list= pd.read_sql_query(query, conn)

        random_response = random.choice(responses_list['chatbot_responses'])

        dispatcher.utter_message(text=random_response)

        return []

class action_ans67_db(Action):
    def name(self) -> Text:
        return "action_ans67_db"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        query= "SELECT chatbot_responses FROM engdata.chatbot WHERE intent_group_name = 'q67'"
        responses_list= pd.read_sql_query(query, conn)

        random_response = random.choice(responses_list['chatbot_responses'])

        dispatcher.utter_message(text=random_response)

        return []

class action_ans68_db(Action):
    def name(self) -> Text:
        return "action_ans68_db"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        query= "SELECT chatbot_responses FROM engdata.chatbot WHERE intent_group_name = 'q68'"
        responses_list= pd.read_sql_query(query, conn)

        random_response = random.choice(responses_list['chatbot_responses'])

        dispatcher.utter_message(text=random_response)

        return []

class action_ans69_db(Action):
    def name(self) -> Text:
        return "action_ans69_db"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        query= "SELECT chatbot_responses FROM engdata.chatbot WHERE intent_group_name = 'q69'"
        responses_list= pd.read_sql_query(query, conn)

        random_response = random.choice(responses_list['chatbot_responses'])

        dispatcher.utter_message(text=random_response)

        return []

class action_ans70_db(Action):
    def name(self) -> Text:
        return "action_ans70_db"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        query= "SELECT chatbot_responses FROM engdata.chatbot WHERE intent_group_name = 'q70'"
        responses_list= pd.read_sql_query(query, conn)

        random_response = random.choice(responses_list['chatbot_responses'])

        dispatcher.utter_message(text=random_response)

        return []

class action_ans71_db(Action):
    def name(self) -> Text:
        return "action_ans71_db"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        query= "SELECT chatbot_responses FROM engdata.chatbot WHERE intent_group_name = 'q71'"
        responses_list= pd.read_sql_query(query, conn)

        random_response = random.choice(responses_list['chatbot_responses'])

        dispatcher.utter_message(text=random_response)

        return []

class action_ans72_db(Action):
    def name(self) -> Text:
        return "action_ans72_db"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        query= "SELECT chatbot_responses FROM engdata.chatbot WHERE intent_group_name = 'q72'"
        responses_list= pd.read_sql_query(query, conn)

        random_response = random.choice(responses_list['chatbot_responses'])

        dispatcher.utter_message(text=random_response)

        return []

class action_ans73_db(Action):
    def name(self) -> Text:
        return "action_ans73_db"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        query= "SELECT chatbot_responses FROM engdata.chatbot WHERE intent_group_name = 'q73'"
        responses_list= pd.read_sql_query(query, conn)

        random_response = random.choice(responses_list['chatbot_responses'])

        dispatcher.utter_message(text=random_response)

        return []

class action_ans74_db(Action):
    def name(self) -> Text:
        return "action_ans74_db"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        query= "SELECT chatbot_responses FROM engdata.chatbot WHERE intent_group_name = 'q74'"
        responses_list= pd.read_sql_query(query, conn)

        random_response = random.choice(responses_list['chatbot_responses'])

        dispatcher.utter_message(text=random_response)

        return []

class action_ans75_db(Action):
    def name(self) -> Text:
        return "action_ans75_db"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        query= "SELECT chatbot_responses FROM engdata.chatbot WHERE intent_group_name = 'q75'"
        responses_list= pd.read_sql_query(query, conn)

        random_response = random.choice(responses_list['chatbot_responses'])

        dispatcher.utter_message(text=random_response)

        return []

class action_ans76_db(Action):
    def name(self) -> Text:
        return "action_ans76_db"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        query= "SELECT chatbot_responses FROM engdata.chatbot WHERE intent_group_name = 'q76'"
        responses_list= pd.read_sql_query(query, conn)

        random_response = random.choice(responses_list['chatbot_responses'])

        dispatcher.utter_message(text=random_response)

        return []
