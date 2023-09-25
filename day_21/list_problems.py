def list_reversal(array):
    '''Given a list, rever''' 
    return array[::-1] 

def palindrome_checker(word):
    if len(word) == 0 or len(word) == 1 : return True 

    first_char = word[0] 
    last_char = word[-1]
    mid = word[1 : -1] 

    if first_char != last_char : return False 
    return palindrome_checker(mid)

def checker_task(a , b):
    a_hash = set() 
    for char in a :
        a_hash.add(char) 
    
    for char in b:
        if char in a_hash :
            return 'Common'
    return 'Uncommon'



if __name__ == "__main__":
    array = "bayo"
    test = print(list_reversal(array)) 
    word = "aba" 
    test = print(palindrome_checker(word)) 
    word_1 = "Money" 
    word_2 = "wife"  
    test = print(checker_task(word_1 ,word_2))


