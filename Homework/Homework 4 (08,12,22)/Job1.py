# 1.	Вычислить число c заданной точностью d
# Пример:
# 	при $d = 0.001, π = 3.141.$ $10^{-1} ≤ d ≤10^{-10}$

# import math
#
# d = input ("Задайте число знаков после запятой: ")
#
# num = int (len (d.split(".")[1]))
# print (round (math.pi, num))

from math import pi

d = float(input('d = '))
i = 0
while d < 1:
    d = d * 10
    i += 1
print(f'π = {round(pi, i)}')
