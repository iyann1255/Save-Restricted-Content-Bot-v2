# devgagan
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

# VPS --- FILL COOKIES 🍪 in """ ... """ 

INST_COOKIES = """
# wtite up here insta cookies
"""

YTUB_COOKIES = """
# write here yt cookies
"""

API_ID = int(getenv("API_ID", "22887706"))
API_HASH = getenv("API_HASH", "12942934ede59eba847a4126775a1b14")
BOT_TOKEN = getenv("BOT_TOKEN", "7809211217:AAHsZnrJ3eaMMQQ-isSBs-eNEmuRR1joZp8")
OWNER_ID = list(map(int, getenv("OWNER_ID", "7733711905").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://aseppp:aseppp@cluster0.bocyf5q.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "-1002886040495")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1003050895677"))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "0"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "5000"))
WEBSITE_URL = getenv("WEBSITE_URL", "upshrink.com")
AD_API = getenv("AD_API", "52b4a2cf4687d81e7d3f8f2b7bc2943f618e78cb")
STRING = getenv("STRING", None)
YT_COOKIES = getenv("YT_COOKIES", YTUB_COOKIES)
DEFAULT_SESSION = getenv("DEFAUL_SESSION", None)  # added old method of invite link joining
INSTA_COOKIES = getenv("INSTA_COOKIES", INST_COOKIES)
