import os
import shutil
from typing import Tuple, List


def copying_from_initial_directory(lab_file: str, path: str) -> None:
    result_dir = path + '\\' + lab_file
    final_dir = current_dir + '\\results\\' + lab_file
    shutil.copyfile(result_dir, final_dir)
    print(f'Файл {lab_file} скопирован в директорию с результатами')


def find_samples_in_directories(directories: Tuple[str], searching_samples: List[str]) -> List[str]:
    for path in directories:
        if not searching_samples:
            break
        founded_samples: List = []
        files_in_directory = tuple(os.listdir(path))
        for sample in searching_samples:
            for lab_file in files_in_directory:
                if sample in lab_file.lower():
                    print(f'Файл {lab_file} найден!')
                    copying_from_initial_directory(lab_file, path)
                    founded_samples.append(sample)
                    break
            if sample not in founded_samples:
                print(f'Проба {sample} не найден в директории', path)

        for sample in founded_samples:
            searching_samples.remove(sample)
    return searching_samples


if __name__ == '__main__':
    current_dir = os.getcwd()
    with open(current_dir + '\conf.txt', encoding="utf-8") as f:
        directories = tuple(f.read().split('\n'))

    command = int(input('''Введите команду
                           1 - выполнить поиск по пробам указанным в файле laboratory_samples.txt
                           2 - ввести ШК вручную
                           '''))
    if command == 1:
        with open(current_dir + '\\not_founded_samples.txt', 'w') as f:
            f.write('')

        with open(current_dir + '\laboratory_samples.txt', encoding="utf-8") as f:
            searching_samples = list(map(lambda x : x.strip().lower(), f.read().split(',')))
        not_founded_samples = find_samples_in_directories(directories, searching_samples)

        with open(current_dir + '\\not_founded_samples.txt', 'w') as f:
            f.write(', '.join(not_founded_samples))
        
                           
    while command == 2:
        searching_samples = []
        searching_samples.append(input('Введите штрихкод лаб исследования\n').lower())
        not_founded_samples = find_samples_in_directories(directories, searching_samples)

        command = int(input('Продолжить поиск?\n (2 - продолжить)\n (0 - выйти)'))
