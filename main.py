import os
from atproto import Client

def main():
    handle = os.environ["BSKY_HANDLE"]
    app_password = os.environ["BSKY_APP_PASSWORD"]

    client = Client()
    client.login(handle, app_password)
    client.send_post("(これはPython SDKを使ったbotです。)\nHello world!")

if __name__ == "__main__":
    main()