h = float(input("Ingrese la altura inicial de la  pelota: "))

altura = h
limite = h / 5
rebote = 0

while altura >= limite:
    altura = altura * 0.9
    rebote += 1

print("La pelota deja de alcanzar la quinta parte de la altura inicial en rebote:", rebote)