liczba = int(input("Podaj liczbę całkowitą: "))

if liczba > 0 and liczba < 10:
    print("Liczba z zakresu (0,10)")

if liczba == 10:
    print("rowne 10")

if 0 < liczba < 10:
    print("Liczba z zakresu (0,10)")

if not (liczba > 0 and liczba < 10):
    print("Liczba spoza zakresu (0,10)")

if not liczba > 0 or not liczba < 10:
    print("Liczba spoza zakresu (0,10)")
