from telethon.sessions import StringSession
from telethon.sync import TelegramClient
api_id = input("Enter Your APP ID: \n")
api_hash = input("Enter Your API HASH : \n")
with TelegramClient(StringSession(), api_id, api_hash) as client:
    print("Check your Telegram Saved Messages ! ")
    session_string = client.session.save()
    saved_messages_template = """
<code>STRING_SESSION</code>: <code>{}</code>
⚠️ <i> Join Us: @DewTools ! </i>""".format(session_string)
    client.send_message("me", saved_messages_template, parse_mode="html")
    
