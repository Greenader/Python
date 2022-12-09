# 4.	Задайте числами список из N элементов, заполненных из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

# Не смог разобраться как создать в файле file.txt


print('Введите число N: ')
n = int(input())
lst = []
for i in range(-n, n + 1):
    lst.append(i)
print(lst)
with open('file.txt', 'r') as f:
    inds = f.readlines()
multiple = 1
for i in inds:
    multiple *= lst[int(i)]
print(multiple)
