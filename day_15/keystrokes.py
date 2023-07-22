'''

Given two strings s and t , which represents a sequence of keystrokes , where 
# denotes backspace , return whether or not the sequences produce the same result. 

Example :  Given the following strings :
s = ABC , t = CD##AB 
return true 

s = como#pur#ter , t = computer return true 

s = cof#dim#g  , t = code returns false 
'''
import sys 
from os import path 
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from day_8.stack import Stack

def compare_keystrokes(s , t):
    '''
        1. We will loop over both characters till both are empty because any of them can contain # 
        2. Each time we encounter # for a string, we will remove the character that is closer to it 

        2. The strings should be compared with one another after all # has been removed 
    ''' 
    s_stack = Stack() 
    t_stack = Stack() 
    for char in s :
        if char == "#":
            s_stack.pop() 
        else:
            s_stack.push(char)

    for char in t :
        if char == "#":
            t_stack.pop() 
        else:
            t_stack.push(char)

    s1 = s_stack.stringnify() 
    t1 = t_stack.stringnify() 

    return s1 == t1 

if __name__ == "__main__":
    s = "cof#dim#g "
    t = "code"

    test = compare_keystrokes(s , t) 
    print(test)