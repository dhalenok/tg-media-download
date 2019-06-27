from telethon import TelegramClient, events, sync
from telethon.tl.types import InputMessagesFilterDocument


api_id = 195718 
api_hash = "02845ea2c8388e7be68c8f41fe607be3" 

client = TelegramClient('session_name', api_id, api_hash)
client.start()

dialogs = client.get_dialogs()
for i, dialog in enumerate(dialogs):
    print(dialog)
    if dialog.name:
        print(f"{i+1}. {dialog.name}")
    else:
        print(f"{i+1}. Deleted Account | ID={dialog.entity.id}")

while (True):
    try:
        selected_dialog = int(input("Please enter dialog number: "))
        if not (1 <= selected_dialog <= len(dialogs)):
            raise ValueError 
        break
    except ValueError:
        print("Entered value is incorrect. Please try again...")

entity = dialog.entity
for message in client.iter_messages(entity, filter=InputMessagesFilterDocument):
    print(message)

