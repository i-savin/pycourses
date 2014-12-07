# coding: utf
# Сравнение полей
# Реализовать класс Comparator, 
# содержащий только поле value и метод compare, 
# возвращающий результат сравнения value с полем value
# любого другого объекта
# (аналогичный работе стандартной функции cmp()).
#  Если такого поля нет, метод возвращает 1.
class Comparator:
    def __init__(self, value):
        self.value = value;

    def compare(self, other):
        try:
            return cmp(self.value, other.value);
        except:
            return 1;