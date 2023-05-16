import re

def count_sym(string):
    count_open = 0
    count_close = 0
    for i in string:
        if i == '(':
            count_open += 1
        elif i == ')':
            count_close +=1

    if count_open > count_close:
        return(True)
    else:
        return(False)
    

def check_dot(string):
    string = re.split(r'[-|+|*|/|(|)]', string)        
    string = [i for i in string if i != '']

    if '.' in string[-1]:
        return(False)
    else:
        return(True)
    
def calc_percent(str_line):
    first_step = str_line[:-1]
    answer = f'{first_step}/ 100'
    answer = eval(answer)
    return(answer)
