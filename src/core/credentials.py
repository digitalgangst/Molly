from os import getenv
from dotenv import load_dotenv

load_dotenv()


def getCredentials():
    return {
        "botToken": getenv("BOTTOKEN",""),
        "database": getenv("DATABASE_NAME","molly.db"),
    }

def getToken():
    return getCredentials().get("botToken")

def getDatabaseName():
    return getCredentials().get("database")
