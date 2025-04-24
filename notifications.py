import http.client, urllib
import os
from dotenv import load_dotenv

load_dotenv()
APP_TOKEN=os.getenv("APP_TOKEN")
USER_TOKEN=os.getenv("USER_TOKEN")

def notify(title, message):
    conn = http.client.HTTPSConnection("api.pushover.net:443")
    conn.request("POST", "/1/messages.json",
    urllib.parse.urlencode({
        "token": APP_TOKEN,
        "user": USER_TOKEN,
        "title":title,
        "message": message,
    }), { "Content-type": "application/x-www-form-urlencoded" })
    conn.getresponse()
