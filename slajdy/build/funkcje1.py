import time
import turtle

ekran = turtle.Screen()
ekran.title("Snake, wynik: 0")
ekran.bgcolor("white")
ekran.setup(width=500, height=500)
ekran.tracer(0)


def dodaj_segment():
    segment = turtle.Turtle()
    segment.speed(2)
    segment.shape("square")
    segment.color("green")
    segment.penup()
    segment.goto(10, 140)
    return segment


dodaj_segment()
ekran.update()

breakpoint()
