import os
import MySQLdb
from dotenv import load_dotenv
import pandas as pd

# Load environment variables from .env file
load_dotenv()

# Create the connection object
connection = MySQLdb.connect(
    host=os.environ.get("HOST", "localhost"),
    user=os.environ.get("USER", "root"),
    passwd=os.environ.get("PASSWORD", "Nikita#23032001"),
    db=os.environ.get("DATABASE", "engdata"),
    ssl_mode='DISABLED'  # Disable SSL certificate validation
)

# Create cursor and use it to execute SQL command
cursor = connection.cursor()
cursor.execute("SELECT @@version")
version = cursor.fetchone()

if version:
    print('Running version: ', version)
else:
    print('Not connected.')


# cursor = connection.cursor()
# counter = 56
# df = pd.read_excel("C:\chatbot nic\data_con_rasa\engdata.xlsx")
# for index, row in df.iterrows():
# 	id = "A" + str(counter)
# 	chatbot_responses= row ['chatbot_responses']
# 	intent_group_name= row ['intent_group_name']
# 	counter +=1
# 	sql_text = "insert into engdata.chatbot values ( '" + id + "' , '" + chatbot_responses + "', '" + intent_group_name +"')"
# 	print(sql_text )
# 	cursor.execute(sql_text)
# 	connection.commit()