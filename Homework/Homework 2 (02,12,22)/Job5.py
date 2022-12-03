# 5.	Реализуйте алгоритм перемешивания списка (shuffle использовать нельзя,
# другие методы из библиотеки random - можно).

ran = range(1, 10)
numbers = list(ran)
print("Текущий список", numbers)
n = -1
for i in range(len(numbers) // 2):
    numbers[n], numbers[i] = numbers[i], numbers[n]
    n -= 2
print("Перемешанный список", numbers )