__author__ = 'Попцов А.В.'

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import shutil
import os

def create_dir(nm_dir):
    if nm_dir != '':
        try:
            os.mkdir(os.path.join(os.getcwd(), nm_dir))
        except FileExistsError:
            print(f"Папка '{nm_dir}' успешно создана!")
        else:
            print(f"Папка '{nm_dir}' успешно создана!")
    else:
        print("Не указано имя папки!")

def delete_dir(nm_dir):
    if nm_dir != '':
        try:
            os.rmdir(os.path.join(os.getcwd(), nm_dir))
        except OSError:
            print(f"Не удается удалить папку '{nm_dir}'!")
        else:
            print(f"Папка '{nm_dir}' успешно удалена!")
    else:
        print("Не указано имя папки!")

# pr_mode - режим работы: 1 - Создание, 2 - Удаление
def p_Dir_Processing(pr_mode, nm_dir = 'Dir'):
    if pr_mode == 1:
        for i in range(1, 9):
            create_dir(nm_dir + '_' + str(i))
    elif pr_mode == 2:
        for i in range(1, 9):
            delete_dir(nm_dir + '_' + str(i))

# Создаем
p_Dir_Processing(1)
# Удаляем
p_Dir_Processing(2)

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
def f_get_folders_dir(nm_dir = os.getcwd()):
    nm_files = os.listdir(nm_dir)
    return nm_files

print(f_get_folders_dir())

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
def p_copy_file(nm_file):
    if nm_file != '':
        try:
            shutil.copy(nm_file, nm_file + '_copy')
        except OSError:
            print(f"Не удается копировать файл '{nm_file}'!")
        else:
            print(f"Файл '{nm_file}' успешно скопирован в '{nm_file}_copy' !")
    else:
        print("Не указано имя файла!")

# Копируем
p_copy_file("5_easy.py")

