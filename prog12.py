produkty = ['red label', 'black label', 'double black', 'green label']
koszt = [65, 119, 159, 210]
cena = sum(koszt)

print("\n=== Cennik ===\n")

for idx in range( len(produkty)):
    print(produkty[idx] + " kosztuje " + str(koszt[idx]) + " PLN")

print("\n=== Wartosc koszyka ===\n")

if len(produkty) > 3:
    print("Wartosc Twojego koszyka po znizce to " + str(cena*0.95) + ("PLN\n"))
else:
    print("Wartosc Twojego koszyka to " + str(cena) + ("PLN\n"))
