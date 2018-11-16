base = float(input("Largura da parede: "))
altura = float(input("Altura da parede: "))

area = base * altura
print("Sua parede de {} por {} tem uma area de {}m^2".format(base, altura, area))
tinta = area/2
print("Para pintar essa parede você vai precisar de {} litros de tinta".format(tinta))
