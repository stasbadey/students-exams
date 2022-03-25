from abc import ABC, abstractmethod


class StudentController(ABC):
    @abstractmethod
    def find_student_by_average_mark(self, average_mark: int):
        pass

    @abstractmethod
    def find_student_by_mark_and_subject(self, mark: int, subject: str):
        pass

    @abstractmethod
    def find_student_by_group(self, group_number: str):
        pass

    @abstractmethod
    def delete_student_by_average_mark(self, average_mark: int):
        pass

    @abstractmethod
    def delete_student_by_mark_and_subject(self, mark: int, subject: str):
        pass

    @abstractmethod
    def delete_student_by_group(self, group_number: str):
        pass
