# coding: utf
# Количество разных символов
# Ввести строку (слова, разделённые пробелами), и вывести через пробел
# вначале слова, состоящие из повторения единственного 
# символа (если таковые имеются), затем — слова, образованные всего из
# двух символов в любом количестве и сочетании, затем — из трёх и т. д.
# Слова с одинаковым количеством символов выводить в порядке их появления в строке.

input_string = raw_input().split(' ');
max_letters = 0;
for word in input_string:
    if len(word) > max_letters:
        max_letters = len(word);

output_string = '';

for i in range(1, max_letters+1):
    for word in input_string:
        if len(set(word)) == i:
            output_string += word;
            output_string += ' ';
print output_string.rstrip();

# print input_string;
# print max_letters;