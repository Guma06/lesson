# файлы чтение и запись

# file = open('text.txt', 'r', encoding='utf-8')

# content = file.read()
# print(content)
# file.close()       это старый метод создания файла

# with open('text.txt', 'r', encoding='utf-8') as file:
#     content = file.read()
#     print(content)             это чтение файла
 
# with open('text.txt', 'a', encoding='utf-8') as file:
#     content = file.read('sdtfs')
#     print(content)    Это запись файла без очистки его внутри

# with open('text.txt', 'w', encoding='utf-8') as file:
#     lines = ['строка 1', 'строка 2']
#     content = file.writelines(lines)
#     print(content)

# with open('text.txt', 'r', encoding='utf-8') as file:
#     user = str(input('Вдохновляйся многоэтажками О, мгновение, задержись Я пройдусь по нам мурашками На чуть-чуть или на всю жизнь'))
#     content = file.write(user)
#     print(content)































