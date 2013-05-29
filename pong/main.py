import random

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock


class PongGame(Widget):

    ball = ObjectProperty(None)

    def update(self, dt):
        self.ball.move()


class PongBall(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)

    velocity = ReferenceListProperty(velocity_x, velocity_y)

    def serve(self):
        self.velocity = Vector(4, 0).rotate(random.randint(0, 360))
        self.center = self.parent.center

    def move(self):
        self.pos = Vector(*self.velocity) + self.pos
        if self.x < 0 or self.right > self.parent.width:
            self.velocity_x = -self.velocity_x
        if self.y < 0 or self.top > self.parent.height:
            self.velocity_y = -self.velocity_y


class PongApp(App):

    def build(self):
        game = PongGame()
        Clock.schedule_interval(game.update, 1.0/60.0)
        game.ball.serve()
        return game

if __name__ == '__main__':
    PongApp().run()
