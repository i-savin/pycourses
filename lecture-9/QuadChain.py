# coding: utf
# Прямоугольник из цепи
# Цепь состоит из прямых отрезков различной целой ненулевой длины,
# соединённых попарно в замкнутую ломаную. 
# Ввести строку целых чисел через запятую — длины отрезков цепи. 
# Вывести YES, если цепь можно превратить в прямоугольник с вершинами 
# в четырёх различных вершинах ломаной. Если нельзя, вывести NO.
# Input:
#  1, 3, 2, 2, 4, 4
# Output:
#  YES
import sys;

def shift(l,n):
    return l[n:] + l[:n]


chain = map(int, raw_input().split(','));
half_perimiter = sum(chain) / 2;
n = len(chain) / 2;
# print n;
max_index = chain.index(max(chain));

chain = shift(chain, max_index);

if len(chain) < 4 or not sum(chain) % 2 == 0:
    print 'NO';
    sys.exit();

finish = False;
while n >= 0 and not finish:
    chain = shift(chain, 1);
    n -= 1;
    sides = [0,0,0,0]
    index = 0;
    for i in chain:
        sides[0] += i;
        # print 'sides[0]=', sides[0];
        index += 1;
        # print sides;
        # print sides_indexes;
        if sides[0] < half_perimiter:
            f_index = index
            for j in chain[f_index:]:
                sides[1] += j;
                f_index += 1;
                if sides[1] + sides[0] >= half_perimiter:
                    break;
            if sides[0]+sides[1] == half_perimiter:
                for k in chain[f_index:]:
                    sides[2] += k;
                    f_index += 1;
                    if sides[2] >= sides[0]:
                        break;
                if sides[2] == sides[0]:
                    sides[3] = sum(chain[f_index:]);
                    # print 'sides[3]=', sides[3];
                    if sides[3] <= sides[1]:
                        finish = True;
                    else:
                        sides[1] = sides[2] = sides[3] = 0;
                else:
                    sides[1] = sides[2] = sides[3] = 0;
            else:
                sides[1] = sides[2] = sides[3] = 0;
        else:
            break;
        if finish:
            break;
# print sides;
if all(sides) and sides[1] == sides[3]:
    print 'YES';
else:
    print 'NO';
