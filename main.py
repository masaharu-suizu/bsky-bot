import os

from atproto import Client

from bots.holiday        import Holiday
from bots.lunch          import Lunch
from bots.premium_friday import PremiumFriday


def main() -> None:
    client = Client()
    client.login(
        os.environ["BSKY_HANDLE"],
        os.environ["BSKY_APP_PASSWORD"],
    )

    bot     = Holiday()
    message = bot.build_message()
    if message:
        client.send_post(message)
    else:
        print("No message to post today.")

    bot     = Lunch()
    message = bot.build_message()
    if message:
        client.send_post(message)
    else:
        print("No message to post today.")

    bot     = PremiumFriday()
    message = bot.build_message()
    if message:
        client.send_post(message)
    else:
        print("No message to post today.")


if __name__ == "__main__":
    main()
