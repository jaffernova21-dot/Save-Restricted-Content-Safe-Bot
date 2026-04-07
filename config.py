# safe_repo
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", ""))
API_HASH = getenv("API_HASH", "")
BOT_TOKEN = getenv("BOT_TOKEN", "8797495324:AAENpS3j6hgwPxE-7faf0twfTLhiT8-ZrAc")
OWNER_ID = list(map(int, getenv("OWNER_ID", "8281644724").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://restrictedjaffer:jaffer@321@cluster0.ham0imb.mongodb.net/?appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1003527826734"))
