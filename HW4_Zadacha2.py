#2. Задайте натуральное число N. Напишите программу, которая составит
#  список простых множителей числа N.
n = int(input("Задайте натуральное число "))

def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    else:
        return True

a = []
for i in range(2, n):
    if is_prime(i) and n % i == 0:
        a.append(i)

print(a)