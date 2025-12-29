import jpholiday

from bsky_bot.schedule import Schedule


class Holiday:
    def build_message(self) -> str | None:
        today        = Schedule._today()
        holiday_name = jpholiday.is_holiday_name(today)

        if holiday_name:
            return f"今日は祝日「{holiday_name}」です。ゆっくり過ごしましょう！"
        return None
