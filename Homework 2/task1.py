# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

num = int(input('Введите число в десятичной системе: '))
print(f'Число {num} в шестнадцатеричной системе с использованием hex: {hex(num)}')

result = ''
letters = list('0123456789abcdef')
while num > 0:
    result = letters[num % 16] + result
    num //= 16

print(f'Это же число в шестнадцатеричной системе без использования hex: {result}')