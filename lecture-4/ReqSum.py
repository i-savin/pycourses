# coding: utf
# Сумма подпоследовательности
# Ввести число N, а на следующей строке — последовательность натуральных чисел
# через запятую. Проверить, является ли N суммой не более, 
# чем 10 каких-либо элементов последовательности, и вывести YES или NO 
# в зависимости от результата.

import sys;


def check(sequence, number):
    if len(sequence) > 0:
        current_number = sequence.pop();
        if number-current_number in sequence:
            return True;
        else:
            return check([i for i in sequence if i < number-current_number], number-current_number);
    return False;

number = input();
sequence = input();#xrange(100000000);

if number in sequence:
    print 'YES';
    sys.exit();
max_length = len(sequence);
if max_length > 10:
    max_length = 10;
s = sorted([i for i in sequence if i < number]);
s.reverse();


if (check(s,number)):
    print 'YES';
else:
    print 'NO';
