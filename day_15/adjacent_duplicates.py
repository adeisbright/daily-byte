'''
Given a string s containing only lowercase letters, continuously 
remove adjacent characters that are the same and return the result.

Ex: Given the following strings...

s = "abccba", return ""
s = "foobar", return "fbar"
s = "abccbefggfe", return "a"

''' 
import sys 
from os import path 
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from day_8.stack import Stack

def adjacent_duplicates(word) :
    stack = Stack() 

    for char in word:
        peek = stack.peek()  
        if peek == char:
            stack.pop() 
        else:
            stack.push(char)
    
    return stack.stringnify() 

if __name__ == "__main__":
    word = "abccbefggfe" 
    test = adjacent_duplicates(word)
    print(test)


