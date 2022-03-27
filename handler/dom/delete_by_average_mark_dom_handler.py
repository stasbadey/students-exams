from xml.dom import minidom


class DeleteByAverageMarkDomHandler:

    def __init__(self, student_id: str):
        self._student_id = student_id

    def delete_student_by_student_id(self) -> bool:

        xml = minidom.parse('students.xml')
        group = xml.documentElement

        try:
            students = group.getElementsByTagName('studentId')

            for student in students:
                if str(student.getAttribute('id')) == str(self._student_id):
                    student.parentNode.removeChild(student)

                    xml.writexml(open('students.xml', 'w'))

                    return True
        except Exception:
            return False
