# coding: utf
# K-значные N-ричные
# Ввести через запятую K и N (1<N<17), 
# вывести в столбик все K-значные N-ричные числа 
# в порядке возрастания (латинские буквы для цифр — большие,
#  незначащие нули или пробелы не считаются).

from itertools import *;

digits = '0123456789ABCDEFG';

k,n = input();
base = digits[0:n];

for s in product(base,repeat=k):
    number = ''.join(i for i in s);
    if not number.startswith('0'):
        print number;
