from skylee.sample_config import Config


class Development(Config):
    OWNER_ID =  1387988065 # my telegram ID
    OWNER_USERNAME = "OtakuDxD"  # my telegram username
    API_KEY = "1570223191:AAHJYX8VIbfLJMxlgLKdtaNGqrtVwIdWsV4"  # my api key, as provided by the botfather
    SQLALCHEMY_DATABASE_URI = 'postgres://vjelwrjqcvupwb:1f7e8a7957d4f217bc20f09f7a811b61a4ecabe028e317008894f000fecb4735@ec2-3-231-194-96.compute-1.amazonaws.com:5432/d9jjcovipa4dji'  # sample db credentials
    MESSAGE_DUMP = '-1001191458830' # some group chat that your bot is a member of
    USE_MESSAGE_DUMP = True
    SUDO_USERS = []  # List of id's for users which have sudo access to the bot.
    LOAD = []
    NO_LOAD = []
    TELETHON_HASH = "1c2c4f9d372bdb22958807b17bc33966" # for purge stuffs
    TELETHON_ID = "1798019"
