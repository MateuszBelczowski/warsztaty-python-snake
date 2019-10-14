print("początek")

wiek = int(input("Podaj swój wiek: "))

minimalny_wiek_mala_karuzela = 8

minimalny_wiek_duza_karuzela = 12

if wiek >= minimalny_wiek_duza_karuzela:
    print("Zapraszamy na dużą karuzelę")
elif wiek >= minimalny_wiek_mala_karuzela:
    print("Zapraszamy na małą karuzelę")
else:
    print("Musisz jeszcze trochę poczekać")

print("koniec")
