from string_reversal import reverse_using_join
'''
Given a string, return whether or not it forms a palindrome 
ignoring case and non-alphabetical characters.
Note: a palindrome is a sequence of characters that 
reads the same forwards and backwards.

Ex: Given the following strings...

"level", return true
"algorithm", return false
"A man, a plan, a canal: Panama.", return true

'''

def palindrome(word : str) -> bool :
    ''' Returns true if the word is a valid palindrome ''' 
    reversed_word = reverse_using_join(word) 
    return reversed_word == word 

print(palindrome("level")) 
print(palindrome("algorithm")) 
print(palindrome("A man , a plan , a canal; Panama"))

def palindrome_second(word : str) -> bool :
    ''' Returns true if the word is a valid palindrome ''' 
    test_word = word.strip() 
    special_chars = ("," , ";" , " ")
    valid_chars = "" 

    for char in test_word:
        if char not in special_chars:
            valid_chars = valid_chars + char 

    worded = valid_chars.lower() 

    print(valid_chars)
    reversed_word = reverse_using_join(worded) 
    return reversed_word == worded

print(palindrome_second("A man , a plan , a canal; Panama"))


