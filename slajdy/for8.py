def generator_liter(napis):
    for litera in napis:
        return litera

print("początek")

imie = "Wierzchosława"

litera = None
generator = generator_liter(imie)
while litera != 'o':
    litera = next(generator)
    print(litera)

print("koniec")
