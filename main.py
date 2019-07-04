import os
import shutil
from telethon import TelegramClient, events, sync
from telethon.tl.types import InputMessagesFilterDocument


api_id = 000_000
api_hash = "00000000000000000000000000000000"

client = TelegramClient("session_name", api_id, api_hash)
client.start()

dialogs = client.get_dialogs()
for i, dialog in enumerate(dialogs):
    if dialog.name:
        print(f"{i+1}. {dialog.name}")
    else:
        print(f"{i+1}. Deleted Account | ID={dialog.entity.id}")

while True:
    try:
        selected_dialog = int(input("Please enter dialog number: "))
        if not (1 <= selected_dialog <= len(dialogs)):
            raise ValueError
        break
    except ValueError:
        print("Entered value is incorrect. Please try again...")

dialog = dialogs[selected_dialog - 1]

directory_name = dialog.name if dialog.name else dialog.entity.id

if not os.path.exists(directory_name):
    os.makedirs(directory_name)
else:
    shutil.rmtree(directory_name)
    os.makedirs(directory_name)

print(f"\n{'👾' * 40}")
at_least_one_media_file_present = False
entity = dialog.entity
for message in client.iter_messages(entity, filter=InputMessagesFilterDocument):
    at_least_one_media_file_present = True
    print(f"\n⬇️  Downloading {message.file.name[:65]}")
    message.download_media(directory_name)

if at_least_one_media_file_present:
    print(f"\n✅ Successfully saved all media to `{directory_name}` folder.")
else:
    print(f"\n❌ Could not find any media files.")
