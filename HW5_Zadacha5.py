#5. Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.
import sympy
x = sympy.Symbol("x")
with open("file1.txt", "r") as f1:
    exp1 = f1.readline().strip()
with open("file2.txt", "r") as f2:
    exp2 = f2.readline().strip()

with open("file3.txt", "w") as f3:
    f3.write(str(sympy.simplify(exp1 + "+" + exp2)))