#3. Задайте последовательность чисел. Напишите программу, которая 
# выведет список неповторяющихся элементов исходной последовательности.
a = map(int,input("Задайте последовательность чисел через пробел ").split())
b = []
for i in a:
    if i not in b:
        b.append(i)
print(b)