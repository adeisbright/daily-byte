'''
Find longest substring without repeating characters given a string s
'''

def longest_substring(word):
    n = len(word)
    chars = []
    j = 0 
    max = 0 
    if len(chars) == 1 : return 1
    for char in word:
        if char not in chars :
            chars.append(char)
        else:
            j = len(chars) 
            last_item = chars[-1]
            print(chars)
            if last_item != char :
                chars = [last_item , char]
            else:
                chars = [char]
            if j > max :
                max = j 

    print(chars)
    if len(chars)  > max :
        max =len(chars)
        
    return max 


def solution(word):
    left = 0 
    max_length = 0 
    char_map_index = {} 

    for index , char in enumerate(word):
        if char in char_map_index and char_map_index[char] >= left :
            left = char_map_index[char] + 1 

        char_map_index[char] = index 
        max_length = max(max_length , index  - left + 1)
    
    return max_length
if __name__ == "__main__":
    word = "abcabcbb"
    test = solution(word) 
    print(test)