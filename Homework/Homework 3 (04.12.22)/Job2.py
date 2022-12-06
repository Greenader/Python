# 2.	Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# 	[2, 3, 4, 5, 6] => [12, 15, 16];
# 	[2, 3, 5, 6] => [12, 15]


n = [2, 3, 4, 5, 6]
sum = []
for i in range((len(n) + 1) // 2):
    sum.append(n[i] * n[-1 - i])
print(sum)
