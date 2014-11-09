
# coding: utf
# Перетасовать кортеж
# Ввести последовательность A объектов Python через запятую и вывести кортеж, 
# состоящий из элементов последовательности, 
# стоящих на чётных местах — в обратном порядке (включая A[0]),
# после которых идут элементы последовательности, стоящие на нечётных местах.

input_tuple = input();
if len(input_tuple) % 2 == 0:
    last_index = len(input_tuple) - 2;
else:
    last_index = len(input_tuple) - 1;
output_tuple = input_tuple[last_index:0:-2]+(input_tuple[0],)+input_tuple[1:len(input_tuple):2];
print tuple(output_tuple);
