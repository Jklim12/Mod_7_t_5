import os
import time
import os.path
directory = '.'
for root, dirs, files in os.walk(directory):

  for file in files:

    filepath = os.path.join('D', 'mypythonprojects', 'mod_7', 'file.txt')

    filetime = os.path.getmtime('D:\mypythonprojects\mod_7')

    formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))

    filesize = os.path.getsize('D:\mypythonprojects\mod_7')

    parent_dir = os.path.dirname ('D:\mypythonprojects\mod_7')

    print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')