# with open('text.txt', 'r', encoding='utf-8') as file:
#     content = file.read()

# new_content = content.replace('О мгновение', 'На минутку')

# with open('text.txt', 'w', encoding='utf-8') as new_file:
#     new_file.write(new_content)

# Т: Исключение
# try:
#     num = int(input('введите число: '))
#     res = 10 / num
#     print(res)
# except (ValueError, ZeroDivisionError):
#     print('ошибка')
# except ValueError:
#     print('ошибка значений')
# except ZeroDivisionError:
#     print('ошибка деления на 0')

# print('ok')

# num2 = int(input('введите число2: '))
# res2 = 2 / num2
# print(res2)


# 3 задание Шифр Цезаря
# alfavit_EU = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
# alfavit_RU = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя'
# lang = input('Выберите язык RU/EU: ')
# smeshenie = int(input('Шаг шифровки: '))
# message = input('Сообщение для шифровки: ')
# itog = ''

# if lang == 'RU':
#     for i in message:
#         mesto = alfavit_RU.find(i)
#         new_mesto = mesto + smeshenie
#         if i in alfavit_RU:
#             itog += alfavit_RU[new_mesto]
#         else:
#             itog += i
# else:
#     for i in message:
#         mesto = alfavit_EU.find(i)
#         new_mesto = mesto + smeshenie
#         if i in alfavit_EU:
#             itog += alfavit_EU[new_mesto].upper()
#         else:
#             itog += i
# print(itog)


#  1 задание < или >
# num = int(input('введите число '))
# v = num%2
# if v ==0:
#     print('четный')
# else:
#     print('не четный')


# 2 задание калькулятор
# num=int(input("введите число: "))
# num2=int(input("введите число: "))
# if num + num2:
#     print('Сумма чисел равна: ')

