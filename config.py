#(©)CodeXBotz




import os
from os import environ
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")  

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "20071888"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "1c4cb9d94b23282abd9ae2a87a521b53")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002262633803"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "8108281129"))

#Port
PORT = os.environ.get("PORT", "3380")

#Database
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://ZeroTwo:aloksingh@zerotwo.3q3ij.mongodb.net/?retryWrites=true&w=majority")
JOIN_REQS_DB = environ.get("JOIN_REQS_DB", DB_URI)
DB_NAME = os.environ.get("DATABASE_NAME", "ZeroTwo")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1002304179911"))
FORCE_SUB_CHANNEL2 = int(os.environ.get("FORCE_SUB_CHANNEL2", "-1002250272000"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "<b>𝙷𝚎𝚕𝚕𝚘 {first}\n\n𝙸 𝙲𝚊𝚗 𝚂𝚝𝚘𝚛𝚎 𝙿𝚛𝚒𝚟𝚊𝚝𝚎 𝙵𝚒𝚕𝚎𝚜 𝚒𝚗 𝚂𝚙𝚎𝚌𝚒𝚏𝚒𝚎𝚍 𝙲𝚑𝚊𝚗𝚗𝚎𝚕 𝚊𝚗𝚍 𝚘𝚝𝚑𝚎𝚛 𝚞𝚜𝚎𝚛𝚜 𝚌𝚊𝚗 𝚊𝚌𝚌𝚎𝚜𝚜 𝙿𝚛𝚒𝚟𝚊𝚝𝚎 𝙵𝚒𝚕𝚎𝚜 𝙵𝚛𝚘𝚖 𝚊 𝚂𝚙𝚎𝚌𝚒𝚊𝚕 𝙻𝚒𝚗𝚔....!\n\n𝙿𝚘𝚠𝚎𝚛𝚎𝚍 𝙱𝚢 @Team_Originals 🔥</b>.")
try:
    ADMINS=[5082638362]
    for x in (os.environ.get("ADMINS", "7092511418").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "<b>𝚂𝚘𝚛𝚛𝚢 𝙳𝚞𝚍𝚎 𝚈𝚘𝚞 𝙽𝚎𝚎𝚍 𝚃𝚘 𝙹𝚘𝚒𝚗 𝚃𝚑𝚎𝚜𝚎 𝙲𝚑𝚊𝚗𝚗𝚎𝚕𝚜</b>\n\n<b>𝚂𝚘 𝙿𝚕𝚎𝚊𝚜𝚎 𝙲𝚕𝚒𝚌𝚔 𝙱𝚕𝚘𝚠 𝚃𝚘 𝙹𝚘𝚒𝚗 𝙲𝚑𝚊𝚗𝚗𝚎𝚕 🔥</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "True") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "❌ 𝙿𝚕𝚎𝚊𝚜𝚎 𝙰𝚟𝚘𝚒𝚍 𝙳𝚒𝚛𝚎𝚌𝚝 𝙼𝚎𝚜𝚜𝚊𝚐𝚎𝚜. 𝙸'𝚖 𝚆𝚘𝚛𝚔𝚒𝚗𝚐 𝙵𝚘𝚛 𝙾𝚗𝚕𝚢  @Team_Originals"

ADMINS.append(OWNER_ID)
ADMINS.append(6446763201)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
   
