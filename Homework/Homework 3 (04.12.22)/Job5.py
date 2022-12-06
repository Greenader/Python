# 5.	Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# o	для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]


number = int(input("Введите число: "))

def fib(num):
    if num in [1, 2]:
        return 1
    else:
        return fib(num - 1) + fib(num - 2)

list_new = [0]
for i in range(1, number + 1):
    list_new.append(fib(i))
    list_new.insert(0, (fib(i) * (-1) ** (i + 1)))
print(list_new)


