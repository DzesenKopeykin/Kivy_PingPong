from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty
from kivy.vector import Vector


class PongGame(Widget):
    pass


class PongApp(App):
    def build(self):
        return PongGame()


if __name__ == '__main__':
    PongApp().run()


class PongBall(Widget):

    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)

    velosity = ReferenceListProperty(velosity_x, velosity_y)

    def move(self):
        self.pos = Vector(*self.velocity) + self.pos