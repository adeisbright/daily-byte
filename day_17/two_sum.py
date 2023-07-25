def two_sum(nums , target):
    hash = {} 

    for i , num in enumerate(nums):
        diff = target - num 
        if diff in hash :
            return [hash[diff] , i] 
        else:
            hash[num] = i 
            
    return []

if __name__ == "__main__" : 
    arr = [2,7,11,15]
    test = two_sum(arr , 9)
    print(test)