import random

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock


class PongGame(Widget):

    ball = ObjectProperty(None)
    paddle1 = ObjectProperty(None)
    paddle2 = ObjectProperty(None)

    def update(self, dt):
        self.ball.move()

        self.paddle1.bounce_ball(self.ball)
        self.paddle2.bounce_ball(self.ball)

        if self.ball.y < 0 or self.ball.top > self.height:
            self.ball.velocity_y = -self.ball.velocity_y

        if self.ball.x < 0 or self.ball.right > self.width:
            if self.ball.x < 0:
                self.paddle2.score += 1
            else:
                self.paddle1.score += 1
            self.ball.serve()

    def on_touch_move(self, touch):
        if touch.x < self.width / 3:
            self.paddle1.center_y = touch.y
        if touch.x > self.width - self.width / 3:
            self.paddle2.center_y = touch.y

class PongBall(Widget):

    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)

    velocity = ReferenceListProperty(velocity_x, velocity_y)

    def serve(self):
        self.velocity = Vector(4, 0).rotate(random.randint(0, 360))
        self.center = self.parent.center
        if abs(self.velocity_y) > 4 * abs(self.velocity_x):
            # boring!
            self.serve()

    def move(self):
        self.pos = Vector(*self.velocity) + self.pos


class PongPaddle(Widget):

    score = NumericProperty(0)

    def bounce_ball(self, ball):
        if self.collide_widget(ball):
            vx, vy = ball.velocity
            offset = (ball.center_y - self.center_y) / (self.height / 2)
            ball.velocity = 1.1 * Vector(- vx, vy) + Vector(0, offset)


class PongApp(App):

    def build(self):
        game = PongGame()
        Clock.schedule_interval(game.update, 1.0/60.0)
        game.ball.serve()
        return game

if __name__ == '__main__':
    PongApp().run()
