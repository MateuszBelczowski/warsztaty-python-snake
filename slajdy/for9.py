print("początek")

imie = "Wierzchosława"

# Wypisuj litery aż natrafisz na `a`. Nie wypisuj jej ale kontynuuj wypisywanie
# pozostałych liter
for litera in imie:
    if litera == 'a':
        continue
    print(litera)

print("koniec")
