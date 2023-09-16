# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа
# должна подсказывать «больше» или «меньше» после каждой попытки. Для генерации случайного
# числа используйте код:
# from random import randint
# num = randint(LOWER_LIMIT, UPPER_LIMIT)

from random import randint
num = randint(0, 1000)

a = int(input('Введите число от 0 до 1000: '))
count = 1

if(a >= 0 and a <= 1000):
    for i in range(2, 11):
        if(a != num):
            count = count + 1
            if(a > num):
                print('меньше')
                a = int(input(f'Попытка {count}. Введите число от 0 до 1000: '))
            elif(a < num):
                print('больше')
                a = int(input(f'Попытка {count}. Введите число от 0 до 1000: '))
        else:
            print('Угадал!')
            break
else:
    print('Введено не верное число')
if(count == 10):
    print('Попытки закончились. Попробуйте снова.')
    print(f'Загаданное число {num}.')