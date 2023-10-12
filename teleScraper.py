import pandas as pd
from telethon.sync import TelegramClient

name = NAME 
api_id = ID
api_hash = HASH

channels = [] # add chat links here

i = 0
for chat in channels:
    i += 1
    data = [] # stores all our data in the format SENDER_ID, MSG

    with TelegramClient(name, api_id, api_hash) as client:
        for message in client.iter_messages(chat):
            data.append([message.sender_id, message.text, message.id, message.get_sender()])


    df = pd.DataFrame(data, columns=['SENDER', 'MESSAGE', 'ID', 'NAME']) # creates a new dataframe


    df.to_csv(f'chat{i}.csv', encoding='utf-8') # save to a CSV file
