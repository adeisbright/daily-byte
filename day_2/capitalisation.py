'''
Given a string, return whether or not it uses capitalization correctly.
 A string correctly uses capitalization if all letters are capitalized, 
 no letters are capitalized, or only the first letter is capitalized.

Ex: Given the following strings...

"USA", return true
"Calvin", return true
"compUter", return false
"coding", return true

'''

def is_capitalized(word :str ) -> bool :
    '''
    check if the first character is capitalised , and 
    '''
    return word.isupper() or word.islower() or word.istitle()

test = is_capitalized("CAt") 

print(test)