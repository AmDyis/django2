import datetime as dt
from pytz import timezone


class GetTime():
    def __init__(self, tz):
        self.tz = tz

    def print_name(self):
        zone = dt.datetime.now(timezone(self.tz))
        print(zone.strftime("%d-%m-%Y %H:%M:%S"))

