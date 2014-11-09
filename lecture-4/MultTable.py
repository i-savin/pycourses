# coding: utf
# Таблица умножения на N
# Ввести через запятую M и N и вывести таблицу умножения от M×1 до M×N в столбик,
# где K-я строчка имеет вид __P_=__K_*_M.
# Между элементами стоят символы подчёркивания, причём перед P
# может быть ноль или больше подчёркиваний,
# а перед K — одно или больше, в остальных случаях подчёркивание одно.
# В результате символы = и * должны стоять друг под другом.

def multiply(m,n):
    result_attend = len(str(m * n));
    m_attend = len(str(m));
    n_attend = len(str(n));
    for i in range(1,n+1):
        result = '';
        result += repr(i*m).rjust(result_attend);
        result += '_=_';
        result += repr(i).rjust(n_attend);
        result += '_*_';
        result += repr(m).rjust(m_attend);
        result = result.replace(' ','_',len(result));
        print result;

(m,n) = input();
multiply(m,n);
