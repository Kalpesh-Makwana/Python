class Clock:
    def __init__(self, hour, minute):
        self.hour = (hour + (minute // 60)) % 24
        self.minute = minute % 60

    def __repr__(self):
        return ("{hour:02d}:{minute:02d}".format(hour=self.hour, minute=self.minute))

    def __eq__(self, other):
        return self.hour == other.hour and self.minute == other.minute

    def __add__(self, minutes):
        new_hour = (self.hour + ((self.minute+minutes) // 60)) % 24
        new_minute = (self.minute + minutes) % 60
        return Clock(new_hour, new_minute)

    def __sub__(self, minutes):
        return self.__add__(-1*minutes)
