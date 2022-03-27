import xml.sax


class FindStudentIdByNumberOfGroupHandler(xml.sax.ContentHandler):
    student_id: int = 0

    def __init__(self, group_number: str):
        self._current_data = ""
        self._number_of_group = ""
        self._students_group = {}
        self._group_number = group_number

    def startElement(self, tag, attributes):
        self._current_data = tag

        if tag == "studentId":
            FindStudentIdByNumberOfGroupHandler.student_id = int(attributes["id"])

        if tag == "group" and attributes["number"] == self._group_number:
            self._students_group[FindStudentIdByNumberOfGroupHandler.student_id] = {self._group_number}

    def endElement(self, tag):
        pass

    def characters(self, content):
        pass

    def get_student_id(self):
        return list(self._students_group)
