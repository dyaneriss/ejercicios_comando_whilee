# Capital inicial
c1 = float(input("Capital de pedro"))
c2 = float(input("Capital de juan"))
c3 = float(input("Capital necesario para el negocio"))

meses = 0

while (c1 + c2) < c3:
    c1 = c1 * 1.03
    c2 = c2 * 1.04
    meses += 1

print("Podran hacer el negocio en", meses, "meses")
print("Capital final de pedro:", round(c1,2))
print("Capital final de Juan:", round(c2,2))
print("Capital totall:", round(c1+c2,2))