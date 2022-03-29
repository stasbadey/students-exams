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
        student_controller = StudentControllerImpl()
        self.label_av.text = student_controller.find_student_by_average_mark(int(self.input.text))

    def delete_student(self):
        student_controller = StudentControllerImpl()
        self.label_av.text = student_controller.delete_student_by_average_mark(int(self.input.text))


class ByNumberOfGroupScreen(Screen):
    def search_student(self):
        student_controller = StudentControllerImpl()
        self.label_av.text = student_controller.find_student_by_group(self.input.text)

    def delete_student(self):
        student_controller = StudentControllerImpl()
        self.label_av.text = student_controller.delete_student_by_group(self.input.text)


class ByMarkAndSubjectScreen(Screen):
    def search_student(self):
        student_controller = StudentControllerImpl()
        self.label_av.text = student_controller.find_student_by_mark_and_subject(int(self.input_mark.text),
                                                                                 self.input_subject.text)

    def delete_student(self):
        student_controller = StudentControllerImpl()
        self.label_av.text = student_controller.delete_student_by_mark_and_subject(int(self.input_mark.text),
                                                                                 self.input_subject.text)


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("UI.kv")


class StudentsExamsApp(App):
    def build(self):
        return kv


if __name__ == "__main__":
    StudentsExamsApp().run()
