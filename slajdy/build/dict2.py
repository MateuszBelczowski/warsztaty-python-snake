slownik = {'jeden': 1, 'dwa': 2, 'slon': True}
print(slownik)

slownik['kon'] = False
print(slownik)

del slownik['dwa']

print('dwa' in slownik)

print(slownik)

slownik['slon'] = False
print(slownik)
