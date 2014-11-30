# coding: utf 
# Счётчик слов
# Ввести строку (слова через пробел), 
# вывести её таким образом, что все вхождения слов,
# кроме первого, опущены. В случае, если слово
# встречалось в исходной строке более одного раза,
# после слова в скобках без пробела следует номер — позиция последнего вхождения.
# qwe sdf tyu qwe sdf try sdf qwe sdf rty sdf wer sdf wer
from collections import *;
words = raw_input();
words = [i for i in words.split(' ')];
words_dict = OrderedDict()
current_index = 0;
for word in words[:]:
    if word not in words_dict:
        words_dict[word] = -1;
    else:
        words_dict[word] = words.index(word) + current_index;
    words.remove(word);
    current_index += 1;
result = '';
for (word, position) in words_dict.iteritems():
    result += word;
    if position != -1:
        result += '(' + str(position) + ')';
    result += ' ';
print result;

