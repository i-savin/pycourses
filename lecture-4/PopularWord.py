# coding: utf
# Самое популярное слово
# Ввести построчно текст, состоящий из пробелов, переводов строки и
# латинских букв, и заканчивающийся пустой строкой. Вывести слово,
# которое чаще других встречается в тексте, если оно такое одно,
# и ---, если таких слов несколько.

input_string = raw_input();
# text = 'Sed tempus ipsum quis eros tempus lacinia Cras finibus lorem ut lacinia egestas nunc nibh iaculis est convallis tincidunt mi mi sed nisl Sed porttitor aliquam elit ullamcorper tincidunt arcu euismod quis Mauris congue elit suscipit leo varius facilisis Cras et arcu sodales laoreet est vitae pharetra orci Integer eget nulla dictum aliquet justo semper molestie neque Maecenas bibendum lacus tincidunt auctor varius purus felis ullamcorper dui et laoreet ligula ex et risus Donec eget fringilla nibh Cras congue tincidunt accumsan Maecenas euismod eleifend elit ut rhoncus tortor sodales a Cras egestas finibus lorem non tempor tincidunt aera';
text = '';
while input_string != '':
    text += input_string;
    input_string = raw_input();
words = text.split();
words_frequency = {};
max_frequency = 0;
for word in words:
    if words_frequency.has_key(word):
        words_frequency[word] += 1;
    else:
        words_frequency[word] = 1;
    if words_frequency[word] > max_frequency:
        max_frequency = words_frequency[word];
most_frequent_word = '';
# print words_frequency;
# print max_frequency;
for word in words_frequency.iterkeys():
    if words_frequency[word] == max_frequency:
        if most_frequent_word == '':
            most_frequent_word = word;
        else:
            most_frequent_word = '---';
            break;
print most_frequent_word;
