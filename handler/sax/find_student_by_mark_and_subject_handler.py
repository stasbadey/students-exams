import copy
import logging
import xml.sax
import re
from typing import List

from model.entity.student import Student


class FindStudentExamsHandler(xml.sax.ContentHandler):
    def __init__(self, expected_mark: int, subject: str):
        self._id = ""
        self._current_data = ""
        self._schedule = ""
        self._mark = ""
        self._exam = ""
        self._exams = []
        self._students_exams = {}
        self._expected_mark = expected_mark
        self._subject = subject
        self.is_expected = False

    def startElement(self, tag, attributes):
        self._current_data = tag
        if tag == "studentId":
            self._id = attributes["id"]
        elif tag == "exam":
            self._exam = attributes["number"]

    def endElement(self, tag):
        if self._current_data == "schedule" and str(self._schedule) == self._subject:
            self.is_expected = True

        elif self._current_data == "mark":
            if re.fullmatch(r'^\s*$', self._mark) is None:
                if int(self._mark) == self._expected_mark and self.is_expected is True:
                    self._exams.append(self._exam)
                    self._students_exams[self._id] = {tuple(set(self._exams))}
                    self._exams = []
                    self.is_expected = False

    def characters(self, content):
        if self._current_data == "schedule":
            self._schedule = content
        elif self._current_data == "mark":
            self._mark = content

    def get_students_exams(self):
        return self._students_exams


class FindStudentByMarkAndSubjectHandler(xml.sax.ContentHandler):
    students: List[Student] = []

    def __init__(self, student_id: str, exam_number: str):
        self._id = ""
        self._current_data = ""
        self._surname = ""
        self._name = ""
        self._succession = ""
        self._student_id = student_id
        self._exam_number = exam_number
        self._is_expected = False
        self._student = Student()

    def startElement(self, tag, attributes):
        self._current_data = tag

        if tag == "studentId" and attributes["id"] == self._student_id:
            self._student.set_id(self._student_id)
            self._is_expected = True

    def endElement(self, tag):
        if self._is_expected is True:
            if self._current_data == "surname":
                self._student.set_surname(self._surname)
            elif self._current_data == "name":
                self._student.set_name(self._name)
            elif self._current_data == "succession":
                self._student.set_succession(self._succession)

                if self._student.get_name() == "":
                    logging.warning("Name field of id {} is empty!".format(self._student_id))
                elif self._student.get_surname() == "":
                    logging.warning("Surname field of id {} is empty!".format(self._student_id))
                elif self._student.get_succession() == "":
                    logging.warning("Succession field of id {} is empty!".format(self._student_id))

                student_copy = copy.copy(self._student)
                FindStudentByMarkAndSubjectHandler.students.append(student_copy)
                self._current_data = ""
                self._is_expected = False

    def characters(self, content):
        if self._current_data == "surname":
            self._surname = content
        elif self._current_data == "name":
            self._name = content
        elif self._current_data == "succession":
            self._succession = content
