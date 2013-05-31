from kivy.app import App
from kivy.graphics import Color, Ellipse, Line
from kivy.uix.button import Button
from kivy.uix.widget import Widget

from random import random


class MyPaintWidget(Widget):

    def on_touch_down(self, touch):
        with self.canvas:
            Color(random(), 1., 1., mode='hsv')
            touch.ud['line'] = Line(points=(touch.x, touch.y), width=3.)

    def on_touch_move(self, touch):
        touch.ud['line'].points += [touch.x, touch.y]


class MyPaintApp(App):
    def build(self):
        parent = Widget()
        paint = MyPaintWidget()
        clear = Button(text="Clear")
        parent.add_widget(paint)
        parent.add_widget(clear)

        def clear_canvas(self):
            paint.canvas.clear()
        clear.bind(on_release=clear_canvas)

        return parent


if __name__ == '__main__':
    MyPaintApp().run()