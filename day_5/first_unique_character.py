'''
Given a string, return the index of its first unique character. 
If a unique character does not exist, return -1.

Ex: Given the following strings...

"abcabd", return 2
"thedailybyte", return 1
"developer", return 0

'''
def first_unique_character(word):
    char_dict = {}
    for (index , char ) in enumerate(word):
        if char in char_dict:
           del char_dict[char]
        else:
            char_dict[char] = index 
    values = list(char_dict.values())
    return values[0] 

if __name__ == "__main__":
    word = "developer"
    
    test = first_unique_character(word)
    print(test)