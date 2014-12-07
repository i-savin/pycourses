# coding: utf
# Гласные поля
# Реализовать класс Vovel, у объекта которого можно получить 
# значение любого поля, если имя этого поля состоит 
# только из маленьких гласных латинских букв. 
# Значение это — строка, совпадающая с именем поля, 
# только состоящая из больших латинских букв. В противном случае поведение 
# объекта должно быть естественным (вызывть исключение AttributeError, 
# как минимум с тем же сообщением, что и «естественный» AttributeError 
# в случае несуществующего поля). Реализовывать что-то, кроме получения значения поля, не надо.

class Vovel:
    def __getattr__(self, item):
        vovels = set('aeiouy');
        item_set = set(str(item));
        if item_set.difference(vovels):
            raise AttributeError("Vovel instance has no attribute '" + str(item) + "'");
        else:
            return str(item).upper();

# A = Vovel()
# print A.aoao
# try:
#   print A.field
# except AttributeError, msg:
#   print "ERROR",msg
