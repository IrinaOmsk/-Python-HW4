#4 Задана натуральная степень k. Сформировать случайным образом список
#  коэффициентов (значения от 0 до 100) многочлена и записать в файл 
# многочлен степени k.(записать в строку)
from random import randint, choice
k = int(input("Введите степень многочлена "))
a = f"{randint(1, 100)}*x**{k}"
for i in  range(k - 1, 0, -1):
    coef = randint(0, 100)
    if coef != 0:
        if i == 1:
            a = a + choice(["+", "-"]) + f"{coef}*x"
        else:
            a = a + choice(["+", "-"]) + f"{coef}*x**{i}"
    
else:
    coef = randint(0, 100)
    if coef != 0:
        a = a + choice(["+", "-"]) + f"{coef}"


with open("file.txt", "w") as f:
    f.write(a)