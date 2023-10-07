# Напишите функцию группового переименования файлов. Она должна:
# 1.  принимать параметр желаемое конечное имя файлов.
# При переименовании в конце имени добавляется порядковый номер.
# 2.  принимать параметр количество цифр в порядковом номере.
# 3.  принимать параметр расширение исходного файла.
# Переименование должно работать только для этих файлов внутри каталога.
# 4. принимать параметр расширение конечного файла.
# 5.  принимать диапазон сохраняемого оригинального имени.
# Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла.
# К ним прибавляется желаемое конечное имя, если оно передано.
# Далее счётчик файлов и расширение.

import os


def rename(new_name: str, digit: int, old_extension: str, new_extension: str, files: list):
    start, finish = files[0] - 1, files[1]
    for _, _, file in os.walk(os.getcwd()):
        for n, i in enumerate(file, 1):
            old_name, target_extension = i.split('.')
            if target_extension == old_extension:
                remaining_name = i[start:finish]
                res = f'{remaining_name}{new_name}_{(digit - len(str(n))) * "0"}{n}.{new_extension}'
                os.rename(i, res)
                print(res)


rename('task', 5, 'txt', 'pdf', [1, 2])
