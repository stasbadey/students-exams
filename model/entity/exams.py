class Exam:
    def __init__(self, subject: str, mark: int):
        self._subject = subject
        self._mark = mark

    def get_subject(self) -> str:
        return self._subject

    def set_subject(self, subject: str) -> None:
        self._subject = subject

    def get_mark(self) -> int:
        return self._mark

    def set_mark(self, mark: int) -> None:
        self._mark = mark
