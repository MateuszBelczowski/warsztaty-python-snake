import time
import turtle

ROZMIAR_PLANSZY = 600
LICZBA_SEGMENTOW_POCZATKOWYCH = 2
SZEROKOSC_ELEMENTU = 20

SEGMENTY = []


def dodaj_segment(x, y, na_koniec=True):
    segment = turtle.Turtle()
    segment.speed(2)
    segment.shape("square")
    segment.color("green")
    segment.penup()
    segment.goto(x, y)
    global SEGMENTY
    if na_koniec:
        SEGMENTY.append(segment)
    else:
        SEGMENTY = [segment] + SEGMENTY
    return segment


def idz_do_gory():
    print("Wciśnięto klawisz góra")


def idz_na_dol():
    print("Wciśnięto klawisz dół")


def idz_w_lewo():
    obecne_x = SEGMENTY[0].xcor()
    obecne_y = SEGMENTY[0].ycor()
    nowe_x = obecne_x - SZEROKOSC_ELEMENTU
    nowe_y = obecne_y
    dodaj_segment(nowe_x, nowe_y, na_koniec=False)
    print("Wciśnięto klawisz lewo")


def idz_w_prawo():
    print("Wciśnięto klawisz prawo")


def zainicjalizuj_plansze():
    ekran = turtle.Screen()
    ekran.title("Snake, wynik: 0")
    ekran.bgcolor("white")
    ekran.setup(width=ROZMIAR_PLANSZY, height=ROZMIAR_PLANSZY)
    ekran.tracer(0)
    ekran.onkeypress(idz_do_gory, "Up")
    ekran.onkeypress(idz_na_dol, "Down")
    ekran.onkeypress(idz_w_lewo, "Left")
    ekran.onkeypress(idz_w_prawo, "Right")
    ekran.listen()
    return ekran


ekran = zainicjalizuj_plansze()

for i in range(LICZBA_SEGMENTOW_POCZATKOWYCH):
    dodaj_segment(SZEROKOSC_ELEMENTU * i, 0)


while True:
    # tutaj dodajemy akcje
    ekran.update()
    time.sleep(0.08)
