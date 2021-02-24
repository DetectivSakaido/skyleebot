from skylee.sample_config import Config


class Development(Config):
    OWNER_ID =  1387988065 # my telegram ID
    OWNER_USERNAME = "OtakuDxD"  # my telegram username
    API_KEY = "1570223191:AAHJYX8VIbfLJMxlgLKdtaNGqrtVwIdWsV4"  # my api key, as provided by the botfather
    SQLALCHEMY_DATABASE_URI = 'postgres://erjhtlua:x_R50Rh-usUHg2f97-1-JVOAvBFxclEn@ziggy.db.elephantsql.com:5432/erjhtlua'  # sample db credentials
    MESSAGE_DUMP = '-1001191458830' # some group chat that your bot is a member of
    USE_MESSAGE_DUMP = True
    SUDO_USERS = []  # List of id's for users which have sudo access to the bot.
    LOAD = []
    NO_LOAD = []
    TELETHON_HASH = "1c2c4f9d372bdb22958807b17bc33966" # for purge stuffs
    TELETHON_ID = "1798019"
    PORT = 8080
    WEBHOOK = False
    URL = None
    SPAMWATCH_API = "dAsbHWPfYv1Q2HoQSV6pm96Z_9vOZdHPCO34p0t7miR2O8tdPsCfr61NT8ZSssXJ"
    ALLOW_EXCL = True
    CERT_PATH = None
    CUSTOM_CMD = False
    WORKERS = 8
