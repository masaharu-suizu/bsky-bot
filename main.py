from atproto import Client
import datetime
import os

def emoji():
    day_of_week = datetime.date.today().weekday()

    if day_of_week == 0:    # Monday
        return "🍛"
    elif day_of_week == 1:  # Tuesday
        return "🍜"
    elif day_of_week == 2:  # Wednesday
        return "🍣"
    elif day_of_week == 3:  # Thursday
        return "🍔"
    elif day_of_week == 4:  # Friday
        return "🍕"
    elif day_of_week == 5:  # Saturday
        return "🌭"
    elif day_of_week == 6:  # Sunday
        return "🍱"


def main():
    handle = os.environ["BSKY_HANDLE"]
    app_password = os.environ["BSKY_APP_PASSWORD"]

    client = Client()
    client.login(handle, app_password)
    client.send_post("(Botです) 今日のランチは何を食おうかなー" + emoji())

if __name__ == "__main__":
    main()
