from typing import List

from Exams import Exam


class Group:
    def __init__(self, number: str, exams: List[Exam]):
        self._number = number
        self._exams = exams

    def get_number(self) -> str:
        return self._number

    def set_number(self, number: str) -> None:
        self._number = number

    def get_exams(self) -> List[Exam]:
        return self._exams

    def set_exams(self, exams: List[Exam]) -> None:
        self._exams = exams


