'''
Given two strings s and t return whether or not s is an anagram of t.
Note: An anagram is a word formed by reordering the letters of another word.

Ex: Given the following strings...

s = "cat", t = "tac", return true
s = "listen", t = "silent", return true
s = "program", t = "function", return false


'''
def valid_anagram(s , t):
    ''' I assume that both words will contain unique characters  '''
    t_hash = set()
    for char in t :
        t_hash.add(char)
    for char in s :
        if char not in t_hash:
            return False 
    return True 

if __name__ == "__main__":
    s = "program" 
    t = "function"
    test=valid_anagram(s , t)
    print(test)