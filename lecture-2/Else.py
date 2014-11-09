# coding: utf
# Точки в круге
# В первой строке ввести координаты центра круга и его радиус 
# (три числа через запятую). Во второй строке ввести 
# координаты точек (чётное количество чисел через запятую). 
# Вывести YES, если все точки принадлежат кругу и NO, если не все.


center_coordinates = input();
points_list = input();
for point in points_list:
    if points_list.index(point) % 2 == 0:
        if abs((point - center_coordinates[0])) > center_coordinates[2]:
            print 'NO';
            break;
    else:
        if abs(point - center_coordinates[1]) > center_coordinates[2]:
            print 'NO';
            break;   
else:
    print 'YES';