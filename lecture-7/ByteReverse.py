# coding: utf
# Байты задом наперёд
# Ввести через запятую строку чисел типа «4-байтовое знаковое целое», 
# переставить байты в занимаемой ими совместно памяти в обратном порядке, 
# вывести в виде списка объектов типа «4-байтовое знаковое целое». 
# Обратите внимание на то, что и «int», и «long int» на разных архитектурах имеют разную длину.

from struct import *;

nums = raw_input();
nums = map(int, nums.split(','));
# print nums;

packed = pack(len(nums)*'i', *nums);
result = [i for i in unpack(len(nums)*'i', packed[::-1])];

print result;