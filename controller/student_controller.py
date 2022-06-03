class StudentController:
    def __init__(self):
        self.model = None

    def find_student_by_average_mark(self, average_mark: int):
        self.model.find_student_by_average_mark(average_mark)

    def find_student_by_mark_and_subject(self, mark: int, subject: str):
        self.model.find_student_by_mark_and_subject(mark, subject)

    def find_student_by_group(self, group_number: str):
        self.model.find_student_by_group(group_number)

    def delete_student_by_average_mark(self, average_mark: int):
        self.model.delete_student_by_average_mark(average_mark)

    def delete_student_by_mark_and_subject(self, mark: int, subject: str):
        self.model.delete_student_by_mark_and_subject(mark, subject)

    def delete_student_by_group(self, group_number: str):
        self.model.delete_student_by_group(group_number)
