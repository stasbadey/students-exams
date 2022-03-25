import xml.sax
from typing import Any

from controller.student_controller import StudentController
from handler.dom.delete_by_average_mark_dom_handler import DeleteByAverageMarkDomHandler
from handler.sax.find_student_by_average_mark_handler import FindAverageMarkHandler, FindByAverageMarkHandler
from handler.sax.find_student_by_mark_and_subject_handler import FindStudentExamsHandler, \
    FindStudentByMarkAndSubjectHandler
from handler.sax.find_student_by_number_of_group_handler import FindStudentByNumberOfGroupHandler
from handler.sax.find_student_id_by_number_of_group_handler import FindStudentIdByNumberOfGroupHandler


class StudentControllerImpl(StudentController):

    def __init__(self):
        pass

    def find_student_by_average_mark(self, average_mark: int):
        handler = FindAverageMarkHandler()

        self._open_sax_parser_connection(handler)

        self._count_avg_from_dict(handler.get_avgs(), average_mark)

    def find_student_by_mark_and_subject(self, mark: int, subject: str):
        handler = FindStudentExamsHandler(mark, subject)

        self._open_sax_parser_connection(handler)

        self._parse_students_exams_from_dict(handler.get_students_exams())

    def find_student_by_group(self, group_number: str):
        handler = FindStudentByNumberOfGroupHandler(group_number)

        self._open_sax_parser_connection(handler)

    def delete_student_by_average_mark(self, expected_avg_mark: int):
        handler = FindAverageMarkHandler()

        self._open_sax_parser_connection(handler)

        for student_id, avg_mark in handler.get_avgs().items():
            if next(iter(avg_mark)) == expected_avg_mark:
                dom_handler = DeleteByAverageMarkDomHandler(student_id)
                dom_handler.delete_student_by_student_id()

    def delete_student_by_mark_and_subject(self, mark: int, subject: str):
        handler = FindStudentExamsHandler(mark, subject)

        self._open_sax_parser_connection(handler)

        for student_id, exam_number in handler.get_students_exams().items():
            dom_handler = DeleteByAverageMarkDomHandler(student_id)
            dom_handler.delete_student_by_student_id()

    def delete_student_by_group(self, group_number: str):
        handler = FindStudentIdByNumberOfGroupHandler(group_number)

        self._open_sax_parser_connection(handler)

        for student_id in handler.get_student_id():
            dom_handler = DeleteByAverageMarkDomHandler(student_id)
            dom_handler.delete_student_by_student_id()

    @staticmethod
    def _count_avg_from_dict(avgs: dict, expected_avg_mark: int):
        parser = xml.sax.make_parser()

        parser.setFeature(xml.sax.handler.feature_namespaces, 0)

        for student_id, avg_mark in avgs.items():
            if next(iter(avg_mark)) == expected_avg_mark:
                parser.setContentHandler(FindByAverageMarkHandler(student_id))

                parser.parse("students.xml")

    @staticmethod
    def _parse_students_exams_from_dict(students_exams: dict):
        parser = xml.sax.make_parser()

        parser.setFeature(xml.sax.handler.feature_namespaces, 0)

        for student_id, exam_number in students_exams.items():
            parser.setContentHandler(FindStudentByMarkAndSubjectHandler(student_id, next(iter(exam_number))[0]))

            parser.parse("students.xml")

    @staticmethod
    def _open_sax_parser_connection(handler: Any):
        parser = xml.sax.make_parser()

        parser.setFeature(xml.sax.handler.feature_namespaces, 0)

        parser.setContentHandler(handler)

        parser.parse("students.xml")
