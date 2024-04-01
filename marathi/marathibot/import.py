import pandas as pd
import mysql.connector
connection = mysql.connector.connect(host="localhost:3306", user="root", password="Nikita#23032001", database="marathi")
cursor = connection.cursor()
counter = 0
df = pd.read_excel("C:\chatbot nic\marathibot\maratable.xlsx")
for index, row in df.iterrows():
	chatbot_response_id = "c" + str(counter)
	chatbot_responses= row ['chatbot_responses']
	intent_group_name= row ['intent_group_name']
	counter +=1
	sql_text = "insert into marathi.maradata values ( '" + chatbot_response_id + "' , '" + chatbot_responses + "', '" + intent_group_name +"')"
	print(sql_text )
	cursor.execute(sql_text)
	connection.commit()