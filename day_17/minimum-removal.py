'''
A solution to the problem that deals with minimum 
removal to make mountain array.
'''

def get_minimum_removal(arr):
    removal_count = 0
    
    left = 0 
    right = len(arr) - 1 

    while left < right :
        mid = left + (right - left) // 2 
       

        if  (arr[mid] <  arr[mid -1 ] or  arr[mid] > arr[mid + 1]) and mid >= 1 :
            removal_count += 1
        if arr[mid] > arr[mid -1 ] and arr[mid] > arr[mid + 1] :
            return removal_count 
        elif  arr[mid] < arr[mid + 1] :
            left = mid + 1 
        else :
            right = mid 
            
    return removal_count 

if __name__ == "__main__" : 
    arr = [2,1,1,5,6,2,3,1]
    test =get_minimum_removal(arr)
    print(test)