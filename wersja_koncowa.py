import time
import random
import turtle

ROZMIAR_PLANSZY = 600

SZEROKOSC_ELEMENTU = 20

SEGMENTY = []


def dodaj_segment(x, y):
    segment = turtle.Turtle()
    segment.speed(2)
    segment.shape("square")
    segment.color("green")
    segment.penup()
    segment.goto(x, y)
    return segment


LICZBA_SEGMENTOW_POCZATKOWYCH = 10
WYNIK_PER_DODATKOWY_SEGMENT = 20



def wygeneruj_jedzenie():
    food = turtle.Turtle()
    food.speed(2)
    food.shape("square")
    food.color('red')
    x = random.randint(-ROZMIAR_PLANSZY / 2, ROZMIAR_PLANSZY / 2)
    y = random.randint(-ROZMIAR_PLANSZY / 2, ROZMIAR_PLANSZY / 2)
    food.penup()
    food.goto(x, y)
    return food


OBECNY_KIERUNEK = "lewo"


def idz_do_gory():
    global OBECNY_KIERUNEK
    if OBECNY_KIERUNEK != "dol":
        OBECNY_KIERUNEK = "gora"


def idz_na_dol():
    global OBECNY_KIERUNEK
    if OBECNY_KIERUNEK != "gora":
        OBECNY_KIERUNEK = "dol"


def idz_w_lewo():
    global OBECNY_KIERUNEK
    if OBECNY_KIERUNEK != "prawo":
        OBECNY_KIERUNEK = "lewo"


def idz_w_prawo():
    global OBECNY_KIERUNEK
    if OBECNY_KIERUNEK != "lewo":
        OBECNY_KIERUNEK = "prawo"


def zainicjalizuj_plansze():
    ekran = turtle.Screen()
    ekran.title("Snake, score: 0")
    ekran.bgcolor("white")
    ekran.setup(width=ROZMIAR_PLANSZY, height=ROZMIAR_PLANSZY)
    ekran.tracer(0)  # Turns off the screen updates
    ekran.onkeypress(idz_do_gory, "Up")
    ekran.onkeypress(idz_na_dol, "Down")
    ekran.onkeypress(idz_w_lewo, "Left")
    ekran.onkeypress(idz_w_prawo, "Right")
    ekran.listen()
    return ekran


ekran = zainicjalizuj_plansze()

for i in range(LICZBA_SEGMENTOW_POCZATKOWYCH):
    SEGMENTY.append(dodaj_segment(SZEROKOSC_ELEMENTU * i, 0))
jedzenie = wygeneruj_jedzenie()


def zderzyl_sie_z_samym_soba():
    head = SEGMENTY[0]
    for segment in SEGMENTY[1:]:
        if czy_segmenty_na_siebie_nachodza(head, segment):
            return True
    return False


def czy_segmenty_na_siebie_nachodza(a, b):
    roznica_x = abs(a.xcor() - b.xcor())
    roznica_y = abs(a.ycor() - b.ycor())
    return roznica_x < SZEROKOSC_ELEMENTU and roznica_y < SZEROKOSC_ELEMENTU


def jedzenie_zostalo_polkniete():
    for segment in SEGMENTY:
        zostalo_polkniete = czy_segmenty_na_siebie_nachodza(segment, jedzenie)
        if zostalo_polkniete:
            return True
    return False


def wyszedl_poza_obszar():
    for segment in SEGMENTY:
        if abs(segment.xcor()) > ROZMIAR_PLANSZY/2:
            if OBECNY_KIERUNEK == "prawo":
                segment.penup()
                segment.goto(-ROZMIAR_PLANSZY / 2, segment.ycor())
            elif OBECNY_KIERUNEK == "lewo":
                segment.penup()
                segment.goto(ROZMIAR_PLANSZY / 2, segment.ycor())
            return
        elif abs(segment.ycor()) > ROZMIAR_PLANSZY/2:
            if OBECNY_KIERUNEK == "gora":
                segment.penup()
                segment.goto(segment.xcor(), -ROZMIAR_PLANSZY / 2)
            elif OBECNY_KIERUNEK == "dol":
                segment.penup()
                segment.goto(segment.xcor(), ROZMIAR_PLANSZY / 2)
            return


def oblicz_obecny_wynik():
    return (len(SEGMENTY) - LICZBA_SEGMENTOW_POCZATKOWYCH) * WYNIK_PER_DODATKOWY_SEGMENT


def koniec_gry():
    ekran.clear()
    wynik = oblicz_obecny_wynik()
    t = turtle.Turtle()
    t.hideturtle()
    t.write(f"Koniec gry, wynik: {wynik}",align="center", font=("Arial", 16, "normal"))
    time.sleep(4)
    ekran.bye()


def oblicz_nowe_wspolrzedne():
    if OBECNY_KIERUNEK == "gora":
        x = pierwszy_segment.xcor()
        y = pierwszy_segment.ycor() + SZEROKOSC_ELEMENTU
    elif OBECNY_KIERUNEK == "dol":
        x = pierwszy_segment.xcor()
        y = pierwszy_segment.ycor() - SZEROKOSC_ELEMENTU
    elif OBECNY_KIERUNEK == "prawo":
        x = pierwszy_segment.xcor() + SZEROKOSC_ELEMENTU
        y = pierwszy_segment.ycor()
    elif OBECNY_KIERUNEK == "lewo":
        x = pierwszy_segment.xcor() - SZEROKOSC_ELEMENTU
        y = pierwszy_segment.ycor()
    else:
        x = pierwszy_segment.xcor()
        y = pierwszy_segment.ycor()
    return x, y


while True:
    if zderzyl_sie_z_samym_soba():
        print("koniec gry")
        koniec_gry()
    if jedzenie_zostalo_polkniete():
        jedzenie.hideturtle()
        jedzenie = wygeneruj_jedzenie()
        ekran.update()
    else:
        ostatni_segment = SEGMENTY.pop()
        ostatni_segment.hideturtle()
    pierwszy_segment = SEGMENTY[0]
    x, y = oblicz_nowe_wspolrzedne()
    nowy_segment = dodaj_segment(x, y)
    SEGMENTY = [nowy_segment] + SEGMENTY
    wyszedl_poza_obszar()
    wynik = oblicz_obecny_wynik()
    ekran.title(f"Snake, score: {wynik}")
    ekran.update()
    time.sleep(0.08)

