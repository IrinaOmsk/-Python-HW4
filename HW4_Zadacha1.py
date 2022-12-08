#1. Вычислить число Пи c заданной точностью d
import math
d = input("Задайте точность ")
print(str(math.pi)[:len(d)])