__author__ = 'Попцов А.В.'

# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):
    str_number = str(number)

    # Ищем позицию десятичного разделителя
    pos_dot = str_number.find('.')
    new_number_end = 0

    #Число с дробной частью на 1 разряд меньше исходного
    new_number = str_number[:pos_dot] + str_number[pos_dot:pos_dot + ndigits]

    # Дробная часть
    str_number_end = str_number[pos_dot + ndigits + 1:pos_dot + ndigits + 2]
    if str_number_end == "":
        str_number_end = "0"
    if int(str_number_end) > 5:
        new_number_end = int(str_number[pos_dot + ndigits:pos_dot + ndigits + 1]) + 1
    elif int(str_number_end) < 5:
        new_number_end = int(str_number[pos_dot + ndigits:pos_dot + ndigits + 1])

    return new_number + str(new_number_end)

print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

# def lucky_ticket(ticket_number):
#     def f_get_sum(tn):
#         sm = 0
#         for i in tn:
#             sm = sm + int(i)
#         return sm

#     ticket_number = str(ticket_number)
#     return (f_get_sum(ticket_number[:3]) == f_get_sum(ticket_number[3:]))


# print(lucky_ticket(123006))
# print(lucky_ticket(12321))
# print(lucky_ticket(436751))