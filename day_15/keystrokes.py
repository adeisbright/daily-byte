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

def apply_backspace(word):
    stack = Stack() 
    for char in word :
        if char == "#":
            stack.pop() 
        else:
            stack.push(char)

    return stack.stringnify() 

def compare_keystrokes(s , t):
    return apply_backspace(s) == apply_backspace(t)

'''
Note: The solution can be re-implemented using an array instead of a stack . 
'''
if __name__ == "__main__":
    s = "cof#dim#g"
    t = "codig"

    test = compare_keystrokes(s , t) 
    print(test)