print("początek")


slownik = {
    'kon': 1,
    'slon': 2,
}

for kolejny in slownik:
    print(kolejny)
    print(slownik[kolejny])


for kolejny in slownik.items():
    print(kolejny[0])
    print(kolejny[1])

print("koniec")
