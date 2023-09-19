# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей.
# Для проверки своего кода используйте модуль fractions

from fractions import Fraction

frac1 = input('Введите первую дробь: ')
frac2 = input('Введите вторую дробь: ')

numer1, denum1 = map(int, frac1.split("/"))
numer2, denum2 = map(int, frac2.split("/"))

sum_frac_num = numer1 * denum2 + numer2 * denum1
sum_frac_denum = denum1 * denum2

mult_frac_num = numer1 * numer2
mult_frac_denum = denum1 * denum2

print(f'Сумма дробей {frac1} и {frac2} - {sum_frac_num}/{sum_frac_denum}')
print(f'Произведение дробей {frac1} и {frac2} - {mult_frac_num}/{mult_frac_denum}')

a = Fraction(numer1, denum1)
b = Fraction(numer2, denum2)

sum = a + b
mult = a * b

print(f'Сумма дробей с использованием fractions: {sum}')
print(f'Произведение дробей с использованием fractions: {mult}')