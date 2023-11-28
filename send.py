# Import telethon library
from telethon import TelegramClient, events, sync
# Import time library
import time

# Define api id and api hash
api_id = 29011275 # Enter your api id here
api_hash = 'a717b047f25fbe4b4659c1f47fb98b83'  # Enter your api hash here

# Create a Telegram client object
client = TelegramClient('af', api_id, api_hash)

# Connect to Telegram servers
client.connect()

# Start an infinite loop
while True:
    try:
        # Loop through all the dialogs (chats) of the client
        for dialog in client.iter_dialogs():
            # Check if the dialog is a group chat
            if dialog.is_group:
                # Get the chat id and title of the group
                chat_id = dialog.id
                chat_title = dialog.title
                # Send the message (عه) to the group
                try:
                	client.send_message(chat_id, 'بی‌‌و فیلم گزاشتم💜')
                	print(f'Message sent to {chat_title}')
                	time.sleep(2)
                except:
                	print("rid")
        # Wait for 15 seconds before repeating the loop
        time.sleep(20)
    except Exception as e:
        print(f"An error occurred: {e}")
