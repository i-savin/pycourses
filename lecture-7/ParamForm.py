# coding: utf
# Параметрическая формула
# Первая строка содержит Python-совместимую формулу,
# в которой могут присутствовать названия переменных
# и элементы модуля math. В следующей строке через
# пробел в виде переменная=значение 
# или переменная=начало_диапазона,конец_диапазона
# указаны допустимые целочисленные значения переменных
# (целочисленный диапазон включает и начальное, и конечное значения). 
# Вывести наибольшее значение формулы на всех допустимых целочисленных значениях переменных.
from math import *;
from itertools import product;
from collections import OrderedDict;

def string_to_dict(s):
    result = OrderedDict();
    for i in s.split(' '):
        try:
            result[i.split('=')[0]] = i.split('=')[1];
        except:
            continue;
    return result;

def generate_intervals(s):
    for (k,v) in s.iteritems():
        try:
            d = v.split(',');
            if (len(d) > 1):
                s[k]=xrange(int(d[0]), int(d[1])+1);
            else:
                s[k]=[int(d[0])];
        except:
            continue;
    return s;

formula = raw_input();
params = raw_input();

params = string_to_dict(params);
params = generate_intervals(params);

params_combination = product(*params.values());

func = 'lambda ';
for param in params.iterkeys():
    func += param + ', ';
func = func.rstrip(', ');
func += ': ' + formula;
func = eval(func);

func_max = None;
for param in params_combination:
    func_current = func(*param);
    if func_current > func_max:
        func_max = func_current;

print func_max;

