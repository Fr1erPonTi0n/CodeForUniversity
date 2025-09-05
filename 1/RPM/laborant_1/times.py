class Seconds:
    def __init__(self, seconds):
        self._seconds = seconds

    def __str__(self):
        return f'{self._seconds} сек.'

    def __int__(self):
        return self._seconds


class Minutes:
    def __init__(self, minutes):
        self._minutes = minutes

    def __str__(self):
        return f'{self._minutes} мин.'

    def __int__(self):
        return self._minutes


class Hours:
    def __init__(self, hours):
        self._hours = hours

    def __str__(self):
        return f'{self._hours} ч.'

    def __int__(self):
        return {self._hours}


class Time(Seconds, Minutes, Hours):
    def __init__(self, hours=0, minutes=0, seconds=0):
        Seconds.__init__(self, seconds)
        Minutes.__init__(self, minutes)
        Hours.__init__(self, hours)

    def __str__(self):
        return f"{self._hours} ч. {self._minutes} мин. {self._seconds} сек."

    def __add__(self, other):
        total_seconds = self.total_seconds() + other.total_seconds()
        return Time.from_seconds(total_seconds)

    def __sub__(self, other):
        total_seconds = self.total_seconds() - other.total_seconds()
        return Time.from_seconds(max(total_seconds, 0))

    def __eq__(self, other):
        return self.total_seconds() == other.total_seconds()

    @classmethod
    def from_seconds(cls, total_seconds):
        hours = total_seconds // 3600
        total_seconds %= 3600
        minutes = total_seconds // 60
        seconds = total_seconds % 60
        return cls(hours, minutes, seconds)

    def total_seconds(self):
        return self._hours * 3600 + self._minutes * 60 + self._seconds
