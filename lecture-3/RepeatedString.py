# coding: utf
# Ввести непустую строку s. Найти такое наибольшее число k и такую строку t, 
# что s совпадает со строкой t, выписанной k раз подряд. Вывести k.

s = raw_input();
index = range(1, len(s));
k = 1;
for i in index:
    sub_string = s[0:i];
    sub_index = range(len(sub_string), len(s), len(sub_string));
    for sub_i in sub_index:
        sub_sub_string = s[sub_i:sub_i+len(sub_string)];
        if sub_sub_string == sub_string:
            k += 1;
        else:
            k = 1;
            break;
    if k != 1:
        break;
print k;
