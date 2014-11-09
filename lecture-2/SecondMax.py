# coding: utf
# Найти второй максимум
# Ввести список и вывести второй максимум этого списка, 
# т. е. элемент a∈S : ∃ b∈S : b>a и a⩾c ∀c∈S, c≠b.
# Если второго максимума нет, вывести NO.

input_list = input()
max1 = max(inputList);
max2 = min(inputList);
for element in inputList:
    if element > max2 and element < max1:
        max2 = element;
if not max2 == max1:
    print max2;
else:
    print 'NO';