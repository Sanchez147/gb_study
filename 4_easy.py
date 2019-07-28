__author__ = 'Попцов А.В.'

# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

a = [i**2 for i in [1, 2, 4, 0]]
print(a)

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

# lst_1 = [t for t in ["яблоко", "банан", "киви", "арбуз", "апельсин"]]
# lst_2 = [p for p in ["груша", "банан", "киви", "апельсин", "вишня"]]
# lst_3 = []
# for i in lst_2:
#     for j in lst_1:
#         if j == i:
#             lst_3.append(j)


# 27.07.2019 - Через генератор списка
lst_11 = {"яблоко", "банан", "киви", "арбуз", "апельсин"}
lst_22 = {"груша", "банан", "киви", "апельсин", "вишня"}

lst_ii = [i for i in lst_11 if i in lst_22]
print(lst_ii)

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

import random
lst_33 = [random.randint(0, 10) for i in range(10)]
lst_34 = [i for i in lst_33 if i%3==0 and i > 0 and i%4!=0]
print(lst_34)