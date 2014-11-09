# coding: utf
# Найти минимум и максимум произвольной функции на целочисленном отрезке
# Ввести строку — произвольное выражение Python,
# в котором могут дополнительно встречаться функции из модуля math и переменная x.
# На следующей строке ввести через запятую целые числа A и B
# (выражение должно быть определено как минимум на A или на B).
# Вывести через пробел минимальное и максимальное значение выражения
# на всех целых x, принадлежащих отрезку [A,B]. Точностью вычислений не управлять.

from math import *;

function = raw_input();
limit = input();
left_border, right_border = limit;
result = [];
for x in xrange(left_border, right_border + 1, 1):
    try:
        result.append(eval(function));
    except:
        pass;

print min(result), max(result)
