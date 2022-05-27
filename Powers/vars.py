from os import getcwd


from prettyconf import Configuration
from prettyconf.loaders import EnvFile, Environment

env_file = f"{getcwd()}/.env"
config = Configuration(loaders=[Environment(), EnvFile(filename=env_file)])



class Config:
    """Config class for variables."""

    LOGGER = True
    BOT_TOKEN = config("BOT_TOKEN", default=None)
    API_ID = int(config("API_ID", default=None))
    API_HASH = config("API_HASH", default=None)
    OWNER_ID = int(config("OWNER_ID", default=1344569458))
    MESSAGE_DUMP = int(config("MESSAGE_DUMP", default=-100))
    DEV_USERS = [int(i) for i in config("DEV_USERS", default="1432756163 1344569458 1355478165 1789859817 1777340882").split(" ")]
    SUDO_USERS = [int(i) for i in config("SUDO_USERS", default="1432756163 1344569458 1355478165 1789859817 1777340882").split(" ")]
    WHITELIST_USERS = [int(i) for i in config("WHITELIST_USERS", default="1432756163 1344569458 1355478165 1789859817 1777340882").split(" ")]
    DB_URI = config("DB_URI", default="")
    DB_NAME = config("DB_NAME", default="gojo_satarou")
    NO_LOAD = config("NO_LOAD", default="").split()
    PREFIX_HANDLER = config("PREFIX_HANDLER", default="/").split()
    SUPPORT_GROUP = config("SUPPORT_GROUP", default="gojo_update")
    SUPPORT_CHANNEL = config("SUPPORT_CHANNEL", default="gojo_updates")
    VERSION = config("VERSION", default="v2.0")
    WORKERS = int(config("WORKERS", default=16))
    BOT_USERNAME = ""
    BOT_ID = ""
    BOT_NAME = ""


class Development:
    """Development class for variables."""

    # Fill in these vars if you want to use Traditional method of deploying
    LOGGER = True
    BOT_TOKEN = "5189246830:AAEVwFNM_4jtpYSrAw0ntw8oFfXJy0kYNsY"
    API_ID = 12388301  # Your APP_ID from Telegram
    API_HASH = "f08f8caff5aac56229e9f02bd67e48ea"  # Your APP_HASH from Telegram
    OWNER_ID = 1943696216  # Your telegram user id
    MESSAGE_DUMP = -1001706596784  # Your Private Group ID for logs
    DEV_USERS = [1943696216]
    SUDO_USERS = [1943696216]
    WHITELIST_USERS = [1943696216]
    DB_URI = "mongodb+srv://vcbot:vcbot@cluster0.dnn8y.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
    DB_NAME = "vcbot"
    NO_LOAD = []
    PREFIX_HANDLER = ["!", "/"]
    SUPPORT_GROUP = "perahinsg"
    SUPPORT_CHANNEL = "summer_sux"
    VERSION = "VERSION"
    WORKERS = 8

