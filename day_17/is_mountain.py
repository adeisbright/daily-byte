'''
Implement an algorithm to determine if an array is 
a mountain array 
'''

def is_mountain(arr):
    
    arr_length = len(arr)  
    peek_index = -1 

    if (arr_length) == 0:
        return False 
    
    for i in range(1 , arr_length - 1):
        if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
            peek_index = i 
    
    if peek_index == -1 or peek_index == 0 or peek_index == arr_length - 1 :
        return False 
    
    for i in range(peek_index):
        if arr[i] >  arr[i + 1]:
            return False 
    
    for i in range(peek_index , arr_length - 1):
        if arr[i] < arr [ i + 1]:
            return False 
    
    return True 

if __name__ == "__main__":
    array = [5, 6, 7, 8, 9, 10, 7]
    test = is_mountain(array) 
    print(test)