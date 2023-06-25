
#!Waring : You cannot reverse a string in 0(1) time but can do so in 0(1) space 
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

# names = ["Ade" , "Priya" , "Salman" , "Arushi"] 

# reversed_names = []

# def reverse_list(word) :
#     ''' Reverses a list '''

#     result  = []
#     word_length = len(word)
#     loop_count = 0
  

#     while(loop_count < word_length ):

#         result.append(word[word_length - 1 - loop_count])
#         loop_count = loop_count + 1

#     print(result)

# reverse_list(names)

def reverse_using_join(word):
    ''' 
        Description : Reverses a string 
        Parameters:
            word : string -> The string to reverse 
        Return :
            The reversed string 
    '''
    return "".join(reversed(word))

print(reverse_using_join("butterfly"))