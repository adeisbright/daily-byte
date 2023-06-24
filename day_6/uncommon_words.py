'''
Given two strings representing sentences, 
return the words that are not common to both strings (i.e. the words that only appear in one of the sentences).
 You may assume that each sentence is a sequence of words (without punctuation) 
 correctly separated using space characters.

Ex: given the following strings...

sentence1 = "the quick", sentence2 = "brown fox", return ["the", "quick", "brown", "fox"]
sentence1 = "the tortoise beat the haire", sentence2 = "the tortoise lost to the haire", 
return ["beat", "to", "lost"]
sentence1 = "copper coffee pot", sentence2 = "hot coffee pot", return ["copper", "hot"]
'''

def uncommon_words(sentence1 , sentence2):
    s1_hash = set() 
    s2_hash = set() 
    uncommon_list = []
    
    for word in sentence1.split():
        s1_hash.add(word) 
    for word in sentence2.split() :
        s2_hash.add(word)

    for val in sentence1.split():
        if val not in s2_hash:
            uncommon_list.append(val)

    for val in sentence2.split():
        if val not in s1_hash:
            uncommon_list.append(val)

    return uncommon_list 

if __name__ == "__main__":
    sentence1 = "the tortoise beat the haire"
    sentence2 = "the tortoise lost to the haire"
    test = uncommon_words(sentence1 , sentence2)
    print(test)