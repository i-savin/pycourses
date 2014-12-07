# coding: utf
# Точки в N-мерном пространстве
# Реализовать клаcc Dot, позволяющий:
# Задавать точку в N-мерном пространстве (с помощью N чисел, где N>0)
# Преобразовывать точку в строку вида «X1,X2,…,XN»
# Вычислять расстояние (distance()) между двумя точками пространства одинаковой размерности
# Вычислять точку (middle()) — середину отрезка между двумя точками пространства одинаковой размерности
# При попытке работы с такими же точками пространства, но разной размерности порождать исключение ValueError

from math import *;

class Dot:
    def __init__(self, *coordinates):
        self.coordinates = coordinates;

    def __str__(self):
        return ",".join(map(str, self.coordinates));

    def distance(self, other):
        if not len(self.coordinates) == len(other.coordinates):
            raise ValueError;
        return sum((a-b)**2 for a,b in zip(self.coordinates, other.coordinates))**0.5;

    def middle(self, other):
        if not len(self.coordinates) == len(other.coordinates):
            raise ValueError;
        return Dot(*((a+b)/2.0 for a,b in zip(self.coordinates, other.coordinates)));


a = Dot(1,2,3);
b = Dot(3,4,5);
print a;
print a.distance(b);

for A,B in (mod.Dot(1,2,3),mod.Dot(3,4,5)), (mod.Dot(1,2),mod.Dot(3)):
    print A
    try:
        print "{:.3f}".format(A.distance(B))
        print A.middle(B)
    except ValueError:
   7     print "ERROR"