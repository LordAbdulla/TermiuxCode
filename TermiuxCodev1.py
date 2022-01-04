from telethon.sync import TelegramClient
from telethon.sessions import StringSession


print("---------------------------")
APP_ID = int(input("Enter Your APP ID : "))
API_HASH = input("Enter Your API HASH : ")
with TelegramClient(StringSession(), APP_ID, API_HASH) as client:
  session_str = client.session.save()
  if client.is_bot():
      user_name = input(" Enter Your Username : ")
      msg = client.send_message(user_name, session_str)
  else:
    msg = client.send_message("me", session_str)
  msg.reply(" Here Is Your TerMiux Code \n t.me/DewTools ")
  print(" TerMuix Code Has Been Sent To Your Savedmessages ✅ . ")
 


#Telegram : @DewTools
#Inst : @hr8k
#Github : github.com/LordAbdulla
