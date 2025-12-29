from bsky_bot.schedule import Schedule


class PremiumFriday:
    def build_message(self) -> str | None:
        if Schedule.is_premium_friday():
            return "(Botだよ) 皆さん今日は月末金曜です。プレミアムフライデー、覚えていますか？ 仕事を早く切り上げて、ゆっくり過ごしましょう！"
        return None
