import os

# Создаем новый файл
# if not os.path.exists('file.txt'): # Если такого файла не существует
#     file = open('file.txt', 'w') # Создаем новый файл с названием 'file.txt', 'w' - переписываем файл
#     file.write(input('Enter words: ') + '\n') # .write('txt') записывает в файл 'txt'
#     file.close()

# Удаляем файл
# if os.path.exists('file.txt'): # Если такой файл существует
#     os.remove('file.txt') # Удаляем функцией os.remove()

# Переименуем файл
# inp = input('File name: ') # Файл который мы ищем
# if os.path.exists(inp): # Если такой файл существует
#     os.rename(inp, input()) # Переименовываем функцией os.rename(filename, newfilename)
# else: print("File doesn't exists!")

# Запись в файл
# file = open('students.txt', 'a') # Открываем файл через мод 'a', чтобы записать в текуший файл
# file.write('\nZarina') # Записываем '\nZarina'
# file.close()

# Переписываем файл
# file = open('students.txt', 'w') # Открываем файл через мод 'w', чтобы переписать в файл
# file.write('new txt\n') # Наш новый текст 'new txt\n'
# file.close()



# Directories:
# print('Текущая директория:', os.getcwd())
# os.chdir('..') - # Переходим в родительскую директорию
# print('Текущая директория:', os.getcwd())
# print(os.listdir())
# os.chdir('C:\\Users\\wupsi\\Desktop\\Folders\\Courses\\PP2_COURSE') - Переходим в директорию с введенным путем
# print('Текущая директория:', os.getcwd())
# print(os.listdir())
# os.getcwd() - Выводит директорию, на которой мы находимся
# os.chdir(path) - В терминале переходим в папку с путем path
# os.listdir() - Выводит все папки и файлы внутри текущей папки

# Создаем новую папку
# inp = input() # Название нашей папки
# if not os.path.isdir(inp): # Проверяем, существует ли такая папка
#     os.mkdir(inp) # функцмей mkdir() создаем новую папку

# Переименовываем директорию
# folder = input()
# if os.path.isdir(folder): # Проверяем, существует ли такая папка
#     os.rename(folder, input('Folder new name: '))

# Удаляем пустую директорию директорию
folder = input()
if os.path.isdir(folder): # Проверяем, существует ли такая папка
    os.rmdir(folder)

# директория - папка