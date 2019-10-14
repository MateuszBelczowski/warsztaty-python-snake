slownik = {'jeden': 1, 'dwa': 2, 'slon': True}
print(slownik)

print(slownik['jeden'])
print(slownik['slon'])

print('dwa' in slownik)

for element in slownik:
    print(element)

for klucz, wartosc in slownik.items():
    print(f'{klucz}: {wartosc}')
