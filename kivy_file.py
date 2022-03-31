import os

os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'

from kivy.lang import Builder
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from controller.impl.student_controller_impl import StudentControllerImpl

Window.fullscreen = 'auto'


class MainScreen(Screen):
    pass


class ChoiceScreen(Screen):
    pass


class ByAverageMarkScreen(Screen):

    def search_student(self):
        if len(self.input.text) == 0:
            self.label_check.text = '''you didn't enter anything, please try again'''
            self.label_check.text = 'Invalid number entered, please try again'
            self.clear()
        else:
            if int(self.input.text) < 0 or int(self.input.text) > 10:
                self.label_check.text = 'Invalid number entered, please try again'
                self.clear()
            else:
                self.label_check.text = ''
                student_controller = StudentControllerImpl()
                self.label_av.text = student_controller.find_student_by_average_mark(int(self.input.text))

    def delete_student(self):
        if len(self.input.text) == 0:
            self.label_check.text = '''you didn't enter anything, please try again'''
            self.clear()
        if self.input.text.isdigit() is False:
            self.label_check.text = 'Invalid number entered, please try again'
            self.clear()
        else:
            if int(self.input.text) < 0 or int(self.input.text) > 10:
                self.label_check.text = 'Invalid number entered, please try again'
                self.clear()
            else:
                self.label_check.text = ''
                student_controller = StudentControllerImpl()
                self.label_av.text = student_controller.delete_student_by_average_mark(int(self.input.text))

    def clear(self):
        self.label_av.text = ""
        self.input.text = ""
        self.label_check.text = ""


class ByNumberOfGroupScreen(Screen):
    def search_student(self):
        if len(self.input.text) == 0:
            self.label_check.text = '''you didn't enter anything, please try again'''
            self.clear()
        if self.input.text.isdigit() is False:
            self.label_check.text = 'Invalid number entered, please try again'
            self.clear()
        else:
            if len(self.input.text) != 6:
                self.label_check.text = 'Invalid data entered, please try again'
                self.clear()
            else:
                self.label_check.text = ''
                student_controller = StudentControllerImpl()
                self.label_av.text = student_controller.find_student_by_group(self.input.text)

    def delete_student(self):
        if len(self.input.text) == 0:
            self.label_check.text = '''you didn't enter anything, please try again'''
            self.clear()
        if self.input.text.isdigit() is False:
            self.label_check.text = 'Invalid number entered, please try again'
            self.clear()
        else:
            if len(self.input.text) != 6:
                self.label_check.text = 'Invalid data entered, please try again'
                self.clear()
            else:
                self.label_check.text = ''
                student_controller = StudentControllerImpl()
                self.label_av.text = student_controller.delete_student_by_group(self.input.text)

    def clear(self):
        self.label_av.text = ""
        self.input.text = ""
        self.label_check.text = ""


class ByMarkAndSubjectScreen(Screen):
    def search_student(self):
        if len(self.input_mark.text) == 0 or len(self.input_subject.text) == 0:
            self.label_check.text = '''you didn't enter anything, please try again'''
            self.clear()
        if self.input_mark.text.isdigit() is False:
            self.label_check.text = 'Invalid number entered, please try again'
            self.clear()
        if self.input_subject.text.isdigit() is True:
            self.label_check.text = 'Invalid number entered, please try again'
            self.clear()

        if len(self.input_mark.text) != 0 or len(self.input_subject.text) != 0 \
                or self.input_mark.text.isdigit() is True or self.input_subject.text.isdigit() is True:
            if int(self.input_mark.text) < 0 or int(self.input_mark.text) > 10:
                self.label_check.text = 'Invalid number entered, please try again'
                self.clear()
            else:
                self.label_check.text = ''
                student_controller = StudentControllerImpl()
                self.label_av.text = student_controller.find_student_by_mark_and_subject(int(self.input_mark.text),
                                                                             self.input_subject.text)

    def delete_student(self):
        if len(self.input_mark.text) == 0 or len(self.input_subject.text) == 0:
            self.label_check.text = '''you didn't enter anything, please try again'''
            self.clear()
        if self.input_mark.text.isdigit() is False:
            self.label_check.text = 'Invalid number entered, please try again'
            self.clear()
        if self.input_subject.text.isdigit() is True:
            self.label_check.text = 'Invalid number entered, please try again'
            self.clear()

        if len(self.input_mark.text) != 0 or len(self.input_subject.text) != 0 \
                or self.input_mark.text.isdigit() is True or self.input_subject.text.isdigit() is True:
            if int(self.input_mark.text) < 0 or int(self.input_mark.text) > 10:
                self.label_check.text = 'Invalid number entered, please try again'
                self.clear()
            else:
                student_controller = StudentControllerImpl()
                self.label_av.text = student_controller.delete_student_by_mark_and_subject(int(self.input_mark.text),
                                                                                         self.input_subject.text)

    def clear(self):
        self.label_av.text = ""
        self.input_mark.text = ""
        self.input_subject.text = ""
        self.label_check.text = ""


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("UI.kv")


class StudentsExamsApp(App):
    def build(self):
        return kv


if __name__ == "__main__":
    StudentsExamsApp().run()
