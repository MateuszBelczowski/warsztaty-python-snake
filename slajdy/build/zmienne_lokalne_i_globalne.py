ZMIENNA_GLOBALNA1 = 1

def tylko_odczyt():
    print(f"w funkcji 'tylko_odczyt': {ZMIENNA_GLOBALNA1}")

def nadpisanie_lokalne():
    ZMIENNA_GLOBALNA1 = 1000
    print(f"w funkcji 'nadpisanie_lokalne': {ZMIENNA_GLOBALNA1}")

def nadpisanie_globalne():
    global ZMIENNA_GLOBALNA1
    ZMIENNA_GLOBALNA1 = 1000
    print(f"w funkcji 'nadpisanie_globalne': {ZMIENNA_GLOBALNA1}")



print(f"wartosc początkowa: {ZMIENNA_GLOBALNA1}")
tylko_odczyt()
print(f"po wywolaniu tylko_odczyt: {ZMIENNA_GLOBALNA1}")
nadpisanie_lokalne()
print(f"po wywolaniu nadpisanie_lokalne: {ZMIENNA_GLOBALNA1}")
nadpisanie_globalne()
print(f"po wywolaniu nadpisanie_globalne: {ZMIENNA_GLOBALNA1}")

