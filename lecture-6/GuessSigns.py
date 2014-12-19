# coding: utf 
# Вставить знаки в целочисленное выражение
# Ввести последовательность натуральных чисел через пробел
# (не более 12), и вывести YES, если можно ли между этими
# числами вставить произвольные знаки сложения или вычитания 
# и один знак "=", чтобы получилось равенство. Вывести NO, если нельзя. 
# Унарные операции и пропуск знака не допускаются.
# Input:
#  123 234 345 12
# Output:
#  YES

from itertools import product

numbers = raw_input().split(u' ');
signs = ['+','-'];
combinations = list(product(signs, repeat=len(numbers)-2));
stop = False;

for combination in combinations:
    for i, number in enumerate(numbers[:-1]):
        c = list(combination[:]);
        c.insert(i, '==');
        equation = ''.join(reduce(lambda x, y: x + y, zip(numbers, c))) + numbers[-1]
        if eval(equation):
            print 'YES';
            stop = True;
            break;
    if stop:
        break;
else:
    print 'NO'