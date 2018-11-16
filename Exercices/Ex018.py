import math
graus = float(input("Insira aqui um valor em graus: " ))
graus=math.radians(graus)
sen = math.sin(graus)
cos = math.cos(graus)
tan = math.tan(graus)

print("O seno é {:.2f}\nO cosseno é {:.2f}\nA tangente é {:.2f}".format(sen, cos, tan))
