class Timetable:
    def __init__(self,schedule: str):
        self._schedule = schedule

    def get_schedule(self) -> str:
        return self._schedule

    def set_schedule(self, schedule: str) -> None:
        self._schedule = schedule
