# Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей. 
# Дано a, b, c - стороны предполагаемого треугольника. Требуется сравнить длину каждого отрезка-стороны с суммой двух других. 
# Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника с такими сторонами не существует. 
# Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.

print('Стороны:')
a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))
 
if a + b > c and a + c > b and b + c > a:
    print('Треугольник существует')
    if a != b != c:
        print('Треугольник разносторонний')
    if (a == b or a == c or b == c) and (a != b != c):
        print ('Треугольник равнобедренный')
    if a == b == c:
        print ('Треугольник равносторонний')
else:
    print('Треугольник не существует')