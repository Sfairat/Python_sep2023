# Напишите код, который запрашивает число и сообщает является ли оно простым или составным. Используйте правило для проверки: 
# “Число является простым, если делится нацело только на единицу и на себя”. 
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

a = int(input('Введите число от 0 до 100000: '))

if(a >= 0 and a <= 100000):
    num = 0
    for i in range(2, a // 2 + 1):
        if(a % i == 0):
            num = num + 1       
    if(num <= 0):
        print(f'{a} - простое число')
    else:
        print(f'Число {a} не простое число')
else:
    print('Введено не верное число')