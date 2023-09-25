# A Recap of some basic programming problems 

def linear_search(array , target):
    for num in array:
        if num == target:
            return True 
    return False 

def binary_search(array , target):
    size = len(array) 
    left = 0 
    right = size - 1

    while (right > left ):
        mid = left + (right - left)//2 
        guess = array[mid] 
        if guess == target:
            return True
        if guess > target :
            left = mid + 1 
        else:
            right = mid 
    return False 

def bubble_sort(array):
    size = len(array) 

    for i in range(size):
        for j in range(i , size):
            if array[i] < array[j] :
                temp = array[j] 
                array[j] = array[i] 
                array[i] = temp  

    return array 


if __name__ == "__main__":
    l = [1 , 3 , 4 , 7 , 10] 
    num = 4
    test = print(linear_search(l , num)) 
    unsorted = [1 , 4 , 3 , 5 , 3 , 7 , 5] 
    test = print(bubble_sort(unsorted)) 


    