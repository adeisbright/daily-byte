'''
Given a string only containing the following characters (, ), {, }, [, and ] 
return whether or not the opening and 
closing characters are in a valid order.

Ex: Given the following strings...

"(){}[]", return true
"(({[]}))", return true
"{(})", return false
'''
import sys 
from os import path 
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from day_8.stack import Stack

def valid_char(chars):
    opening_chars = ("{" , "(" , "[")
    closing_chars = ("}" , ")" , "]") 
    open_and_close = {
        "{" : "}",
        "(":  ")",
        "[": "]"
    }

    stack = Stack() 

    for char in chars:
        if char in opening_chars:
            stack.push(char)
        
        if char in closing_chars:
            peek = stack.peek() 
           
            peek_closer = open_and_close.get(peek)

            if peek_closer != char:
                return False 
            else:
                stack.pop()
    return True 

if __name__ == "__main__":
    chars = "(){}[]" 
    test = valid_char(chars)
    print(test)