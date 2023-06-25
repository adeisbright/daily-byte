import re 

def search(chars , word):
    ''' Searches a string for the pattern.
    Returns the first point where the pattern exists or none.
    The index of the start and end of that particular pattern.
    You should craft your meta characters properly
    '''
    return re.search(chars , word) 

test1 = search("\d+" , "abcd") 
print(test1)
test2 = search("\d+" , "abc12d")
w = "abc12d"[3:5]
print(test2 , w)

def split(word , pattern):
    ''' Returns an array of strings split along the pattern'''
    return re.split(pattern,word)

test3 = split("Ade is a boy" , "\s+") 
print(test3)

def match(pattern , word):
    ''' Returns true if the word matches the pattern ''' 
    pattern = re.compile(pattern)
    return pattern.match(word)


pattern = "^[a-zA-Z]{2}\s{1}(we)"
test4 = match(pattern , "Ad we for here")  
print(test4.group()) #Get the matched stuffs 

def find_all(pattern , word):
    ''' Returns true if the word matches the pattern ''' 
    pattern = re.compile(pattern)
    return re.findall(pattern,word)

test5 = match(pattern , "Ad we for here")  
print(test5)