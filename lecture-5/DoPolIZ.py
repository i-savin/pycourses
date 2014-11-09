# coding: utf
# Вычислить выражение в польской инверсной записи
# Ввести целочисленное выражение в польской инверсной записи, 
# в котором могут содержаться разделённые пробелом целые числа и 
# 4 знака арифметики: "+", "-", "*" и "/". Если выражение можно вычислить, 
# вывести результат. В противном случае (синтаксическая ошибка, 
# в стеке остался не один элемент, и т. п.) вывести ERROR

def calculate(input_string):
    try:
        stack = [];
        for operand in input_string.rsplit():
            if operand not in '+-*/':
                stack.append(operand);
            else:
                op2 = stack.pop();
                op1 = stack.pop();
                expression = op1 + operand + op2;
                result = eval(expression);
                stack.append(str(result));
            # print 'stack', stack;
        result = stack.pop();
        if len(stack) == 0:
            return result;
        else:
            raise Exception('ERROR');
            # print 'ERROR';
    except Exception, e:
        # print e.message;
        raise Exception('ERROR');



input_string = raw_input();
try:
    print calculate(input_string);
except Exception, e:
    print e.message;



