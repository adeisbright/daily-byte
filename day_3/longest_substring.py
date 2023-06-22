'''
Given an array of strings, return the longest common prefix that
is shared amongst all strings.
Note: you may assume all strings only contain lowercase alphabetical 
characters.

Ex: Given the following arrays...

["colorado", "color", "cold"], return "col"
["a", "b", "c"], return ""
["spot", "spotty", "spotted"], return "spot"

'''
def common_prefix(words):
    '''
    Note: Prefix means the word must start from the beginning 
    For that, the first prefix must be the first word.
    So, create a variable prefix to hold the first word in the list. 
    Just as with many string related problem, we will have to run a loop over
    each word starting from the second element .

    When we get a word, we will check if the word begins with our prefix using 
    python's built in startswith.

    If it is not, we will keep removing the characters at the end of the 
    word till we get the longest prefix or just return an empty string if there  
    is none
    ''' 
    prefix = words[0]
    for word in words[1:]:
        while not word.startswith(prefix):
            prefix = prefix[:-1] 
            if len(prefix) == 0:
                return ""
    return prefix

if __name__ == "__main__":

    words = ["colorado", "color", "cold"]
    test = common_prefix(words) 
    print(test)
    words = ["a", "b", "c"]
    test = common_prefix(words) 
    print(test)
    words = ["spot", "spotty", "spotted"]
    test = common_prefix(words) 
    print(test)