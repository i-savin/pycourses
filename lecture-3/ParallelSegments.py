# coding: utf
# Параллельные отрезки
# Ввести восемь чисел через запятую — целочисленные координаты 4-х 
# попарно несовпадающих точек A1, A2, A3 и A4: X1, Y1, X2, Y2, X3, Y3, X4, Y4.
# Вывести YES, если прямая A1A2 параллельна прямой A3A4 (или совпадает с ней), 
# и NO — если не параллельна.

from decimal import Decimal
x1,y1,x2,y2,x3,y3,x4,y4 = input();
x1 = Decimal(x1);
x2 = Decimal(x2);
x3 = Decimal(x3);
x4 = Decimal(x4);
y1 = Decimal(y1);
y2 = Decimal(y2);
y3 = Decimal(y3);
y4 = Decimal(y4);
if x1 - x2 == 0 and x3 - x4 == 0:
    print 'YES';
elif x1 - x2 == 0 and not x3 - x4 == 0:
    print 'NO';
elif not x1 - x2 == 0 and x3 - x4 == 0:
    print 'NO';
else:
    tan1 = (y1 - y2) / (x1 - x2);
    tan2 = (y3 - y4) / (x3 - x4);
    b1 = y1 - tan1 * x1;
    b2 = y3 - tan2 * x3;
    # print tan1, tan2, b1, b2;
    if tan1 == tan2:
        print 'YES';
    else:
        print 'NO';