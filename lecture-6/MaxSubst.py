# coding: utf
s = raw_input();
dic = {}; # номер символа - длина последовательности, которая начинается с него
max = 0; # переменная для хранения максимальной длины последовательности
compare = 0;
for i in range(len(s)):
    if len(s) - i <= max:
        break;
    dic[i] = 1;
    for j in range(i+1, len(s)):
        compare = compare + 1;
        if s[j] not in s[i:j]:
            dic[i] += 1;
        else:
            break;
    if dic[i] > max:
        max = dic[i];
        max_index = i;
    # if i + max == len(s) - 1:
    #     break;
# for (k,v) in dic.iteritems():
#     print k,v;
# print max_index;
# print dic[max_index];
print compare;
print s[max_index:max_index+dic[max_index]];