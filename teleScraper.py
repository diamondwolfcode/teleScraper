import pandas as pd
from telethon.sync import TelegramClient

name = NAME
api_id = ID # int
api_hash = HASH
chat = CHANNEL_LINK

data = [] # stores all our data in the format SENDER_ID, MSG


with TelegramClient(name, api_id, api_hash) as client:
    for message in client.iter_messages(chat):
        data.append([message.sender_id, message.text])


df = pd.DataFrame(data, columns=['SENDER', 'MESSAGE']) # creates a new dataframe


df.to_csv('test.csv', encoding='utf-8') # save to a CSV file
