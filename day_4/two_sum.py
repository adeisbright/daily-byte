'''
Given an array of integers, return whether or not two numbers sum to a given target, k.
Note: you may not sum a number with itself.

Ex: Given the following...

[1, 3, 8, 2], k = 10, return true (8 + 2)
[3, 9, 13, 7], k = 8, return false
[4, 2, 6, 5, 2], k = 4, return true (2 + 2)

'''
def two_sum(numbers , target):

    for (i , a) in enumerate(numbers):
        for j in numbers[i+1:]:
            sum = a + j 
            if(sum == target) : return True  
            print("a is {} and j is {}".format(a , j))      
    return False 

#Using the complements method 

def two_sum_slide(numbers , target):
    complement = set() 

    for num in numbers:
        diff = target - num 
        if diff in complement:
            return True 
        complement.add(num) 
    return False

if __name__ == "__main__":
    numbers = [4, 2, 6, 5, 2]
    k = 12
    test = two_sum_slide(numbers , k)
    print(test)

