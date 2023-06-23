'''
Given a string representing your stones and another
 string representing a list of jewels,
   return the number of stones that you have that are also jewels.

Ex: Given the following jewels and stones...

jewels = "abc", stones = "ac", return 2
jewels = "Af", stones = "AaaddfFf", return 3
jewels = "AYOPD", stones = "ayopd", return 0

'''

def stones_and_jewels(stones , jewels):
    stone_count = 0 
    jewel_hash = set() 
    for jewel in jewels:
        jewel_hash.add(jewel)
    for stone in stones:
        if stone in jewel_hash:
            stone_count += 1 

    return stone_count 

if __name__ == "__main__":
    jewels = "AYOPD"
    stones = "ayopd"
    test = stones_and_jewels(stones,jewels) 
    print(test) 
