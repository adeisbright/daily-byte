'''
Given a string and the ability to delete at most one character, 
return whether or not it can form a palindrome.
Note: a palindrome is a sequence of characters that reads 
the same forwards and backwards.

Ex: Given the following strings...

"abcba", return true
"foobof", return true (remove the first 'o', the second 'o', or 'b')
"abccab", return false

'''
def palindrome_on_removal(word):
    if len(word) == 0 or len(word) == 1 :  return True 

    first_char = word[0] 
    last_char = word[-1] 
    mid_char = word[1:-1] 

    outliers = {}
    if first_char != last_char : 
        if(not bool(outliers)):
            outliers["first"] = first_char 
            outliers["second"] = last_char 
        else:
            return False 
    
    return palindrome_on_removal(mid_char)

test = palindrome_on_removal("abccab") 
print(test)