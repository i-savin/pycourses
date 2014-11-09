# coding: utf
# Ввести объект Python и вывести в столбик имена тех его полей 
# (независимо от типа ⇒ в т. ч. методов), которые не начинаются на «_»
inputObject = input();
objectsMethod = dir(inputObject);
for method in objectsMethod:
    if not method.startswith('_'):
        print method;
