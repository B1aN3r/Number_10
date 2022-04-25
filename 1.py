#создаем и открываем файлл, которого не существовало
file = open('file.txt', 'w')

#записываем строку в файл
file.write('Hi All')
file.close()

#считываем строку
file = open('file.txt', 'r')
print(file.read())