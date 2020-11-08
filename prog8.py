samochody = ['syrena', 'polonez', 'wolga', 'maluch']

print(samochody[0])
print(samochody[1])
print(samochody[3])


print("=== petla 1 ===")
for s in samochody:
    print(s)

for idx in [0, 1]:
    print(samochody[idx])

print("=== petla 2 ===")
print("len: {0}".format(len(samochody)))
print("range: {0}".format(range(3)))

print("=== petla 3 ===")
for idx in range( len(samochody) ) :
    print("idx: " + str(idx) + " : " + samochody[idx])


print("listy -> string")
print(", ".join(samochody))

print("string -> lista")
import_samochody = "kia,merc,volvo"
lista = import_samochody.split(',')
print(lista)


#arr = "a,b,c,d,e".(split(','))
