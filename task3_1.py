# Дан список целых чисел.  Требуется вычислить, сколько раз встречается некоторое число X в этом списке.
# Пользователь вводит число X с клавиатуры. Список можно считать заданным.
# Если такого числа в списке нет - вывести -1.
# 	Примеры/Тесты:
#     Input:   [10, 5, 7, 3, 3, 0, 5, 7, 2, 8], x = 3
#     Output:  2

#     Input:   [10, 5, 7, 3, 3, 0, 5, 7, 2, 8], x = 20
#     Output:  -1
# Напишите алгоритм подсчета самостоятельно или воспользуйтесь методами списка.
# ```(*)``` **Усложнение.** При выводе результата на экран воспользуйтесь тернарным оператором.

list1 = [10, 5, 7, 3, 3, 0, 5, 7, 2, 8]
number = int(input("Введите число: "))
count = 0
if number not in list1: 
        print(-1)
else:
    for i in list1:
        if i == number:
            count = count + 1
    print(count)

