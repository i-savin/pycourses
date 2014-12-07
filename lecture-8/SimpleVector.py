# coding: utf
# Вектора на плоскости
# Реализовать класс Vector, позволяющий
# задавать двумерный вектор (из двух чисел)
# вычислять вектор — сумму двух векторов
# вычислять вектор — результат умножения вектора на число (или числа на вектор)
# скалярно умножать вектор на вектор
# преобразовывать вектор в строку вида |x,y|

class Vector:
    def __init__(self, x, y):
        self.x = x;
        self.y = y;

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y);

    def __str__(self):
        return '|' + str(self.x) + ',' + str(self.y) + '|';

    def __mul__(self, other):
        if isinstance(other, int):
            return Vector(self.x * other, self.y * other);
        return self.x * other.x + self.y * other.y;

    def __rmul__(self, other):
        return self.__mul__(other);

# A = Vector(1,2)
# B = Vector(3,4)
# print A
# print A+B
# print A*B
# print 7*A