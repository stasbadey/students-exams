from Timetable import Timetable


class Exam:
    def __init__(self, number: int, timetable: Timetable, mark: int):
        self._number = number
        self._timetable = timetable
        self._mark = mark

    def get_number(self) -> int:
        return self._number

    def set_number(self, number: int) -> None:
        self._number = number

    def get_timetable(self) -> Timetable:
        return self._timetable

    def set_timetable(self, timetable: Timetable) -> None:
        self._timetable = timetable

    def get_mark(self) -> int:
        return self._mark

    def set_mark(self, mark: int) -> None:
        self._mark = mark

