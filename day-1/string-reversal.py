'''
Ex: Given the following strings...

“Cat”, return “taC”
“The Daily Byte”, return "etyB yliaD ehT”
“civic”, return “civic”

'''

def reverse_string(word : str) -> str : 
    ''' Reverses a string'''
    
    word_length = len(word)
    middle_point = word_length//2 
    loop_count = 0
   
    str_list = []

    while(loop_count <= middle_point):

        str_list.append(word[word_length - 1 - loop_count])
        loop_count = loop_count + 1 
    
    return str_list


def reversal(word) :
    s = "" 
    word_length = len(word)
    loop_count = 0
  

    while(loop_count < word_length ):

        s = s + (word[word_length - 1 - loop_count])
        loop_count = loop_count + 1
    print(s)

reversal("Cat")
reversal("The Daily Byte")  
reversal("civic")

def splice(word):
    print(word[::-1])
    
splice("Cat")