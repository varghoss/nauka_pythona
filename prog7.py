imie = 'Ala'
ile = 5
zwierze = 'kot'

if ile == 1:
    print('{0} ma {1}a'.format(imie, zwierze))
elif ile ==2:
    print('{0} ma {1} {2}y'.format(imie, ile, zwierze))
else:
    print('{0} ma {1} {2}ow'.format(imie, ile, zwierze))

if 'ot' in zwierze:
    print('Zacyna sie na ot')
