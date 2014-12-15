# coding: utf
# Создать три класса:
# Trigon, обозначающий треугольник:
# заводится по трём сторонам
# имеет методы square() (площадь) и perimeter() (периметр)
# Pea, обозначающий грушу круг
# заводится (NB!) по трём сторонам вписанного треугольника
# имеет методы square() и perimeter()
# TrigonPea (унаследованный от Trigon и Pea), обозначающий треугольную грушу
# заводится по трём сторонам
# периметр и площадь равны периметру и площади треугольника
# имеет метод volume(), равный произведению периметра треугольника на площадь описанного круга
# Неравенство треугольника проверять не надо.
# Input:
# Output:
#  6.000000
# 12.000000
# 19.634954
# 235.619449
# 6.000000

from math import *;

class Trigon(object):
    def __init__(self, a, b, c):
        self.a = a;
        self.b = b;
        self.c = c;

    def perimeter(self):
        return self.a + self.b + self.c;

    def square(self):
        p = self.perimeter() / 2.0;
        return sqrt(p * (p - self.a) * (p - self.b) * (p - self.c));

class Pea(object):
    def __init__(self, a, b, c):
        self.a = a;
        self.b = b;
        self.c = c;
        self.r = self.radius();

    def square(self):
        return pi * self.r ** 2.0;

    def perimeter(self):
        return 2.0 * pi * self.r;

    def radius(self):
        p = (self.a + self.b + self.c) / 2.0;
        return self.a * self.b * self.c / (4.0 * sqrt(p * (p-self.a) * (p-self.b) * (p-self.c)));

class TrigonPea(Trigon, Pea):
    def __init__(self, a, b, c):
        super(TrigonPea, self).__init__(a,b,c);
        self.r = self.radius();

    def volume(self):
        return self.perimeter() * Pea.square(self);



# t=Trigon(3,4,5)
# p=Pea(3,4,5)
# z=TrigonPea(3,4,5)
# print "{:.6f}".format(t.square())
# print "{:.6f}".format(t.perimeter())
# print "{:.6f}".format(p.perimeter())
# print "{:.6f}".format(p.square())
# print "{:.6f}".format(z.volume())
# print "{:.6f}".format(z.square())
# print "{:.6f}".format(z.perimeter())