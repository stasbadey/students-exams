import os

os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'

from kivy.lang import Builder
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window

Window.fullscreen = 'auto'


class MainScreen(Screen):
    pass


class ChoiceScreen(Screen):
    pass


class ByAverageMarkScreen(Screen):
    def search_student(self):
        pass

    def delete_student(self):
        pass


class ByNumberOfGroupScreen(Screen):
    def search_student(self):
        pass

    def delete_student(self):
        pass


class ByMarkAndSubjectScreen(Screen):
    def search_student(self):
        pass

    def delete_student(self):
        pass


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("UI.kv")


class StudentsExamsApp(App):
    def build(self):
        return kv


if __name__ == "__main__":
    StudentsExamsApp().run()
