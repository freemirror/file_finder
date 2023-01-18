import os
import shutil


current_dir = os.getcwd()
directories = open(current_dir + '\directory.txt', encoding="utf-8").read()
dir_list = directories.split('\n')

finish = 1
while finish == 1:
    search_file_name = input('Введите штрихкод лаб исследования\n').lower()
    result_dir = 0

    for path in dir_list:
        file_list = os.listdir(path)

        for lab_file in file_list:
            if search_file_name in lab_file.lower():
                print('Файл ', lab_file, ' найден!')
                result_dir = path + '\\' + lab_file
                final_dir = current_dir + '\\' + lab_file
                shutil.copyfile(result_dir, final_dir)
                break

        if result_dir != 0:
            break
        print('Файл не найден в директории', path)

    finish = input('Продолжить поиск?\n (1 - продолжить)\n')
    if finish == '1':
        finish = 1
