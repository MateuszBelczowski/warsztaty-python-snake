import time
import turtle

ekran = turtle.Screen()
ekran.title("Snake, wynik: 0")
ekran.bgcolor("white")
ekran.setup(width=500, height=500)
ekran.tracer(0)


def dodaj_segment(x, y):
    segment = turtle.Turtle()
    segment.speed(2)
    segment.shape("square")
    segment.color("green")
    segment.penup()
    segment.goto(x, y)
    return segment


for x in range(200):
    dodaj_segment(x*2, 0)
    ekran.update()
    time.sleep(0.1)

