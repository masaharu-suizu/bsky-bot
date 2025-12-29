from datetime import date, timedelta

import jpholiday


class Schedule:
    @classmethod
    def _today(cls) -> date:
        return date.today()

    @classmethod
    def is_weekend(cls) -> bool:
        return cls._today().weekday() >= 5

    @classmethod
    def is_holiday(cls) -> bool:
        return jpholiday.is_holiday(cls._today())

    @classmethod
    def is_business_day(cls) -> bool:
        return not cls.is_weekend() and not cls.is_holiday()

    @classmethod
    def is_premium_friday(cls) -> bool:
        today = cls._today()

        if today.weekday() != 4:
            return False

        if not cls.is_business_day():
            return False

        next_week = today + timedelta(days=7)
        return today.month != next_week.month
