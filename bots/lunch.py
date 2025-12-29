from bsky_bot.schedule import Schedule


class Lunch:
    def build_message(self) -> str | None:
        if Schedule.is_weekend() or Schedule.is_holiday():
            return "(Botだよ) 今日のランチは何を食おうかなー"
        return None
