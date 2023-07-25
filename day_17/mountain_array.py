'''
Mountain Array:
A mountain array is an array that increases monotonically and  
then decreases monotonically.

Our algorithm below specifically works for array that are mountain array. 

'''
def peakIndexInMountainArray(arr , index = 0):

    """
    :type arr: List[int]
    :rtype: int
    """
    lower = arr[0] 
    remnant = arr[1:] 
    mid = remnant[0]
    upper = remnant[1]
    index += 1
    if lower < mid and mid > upper :
        return index
    
    return peakIndexInMountainArray(remnant , index)

def peakMountainIndex(arr):
    left = 0 
    right = len(arr) - 1 

    while left < right :
        mid = left  + (right -  left)   //2 
        if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
            return mid 
        elif  arr[mid] <  arr[mid + 1] :
            left = mid + 1 
        else :
            right = mid 
    
    return left 


if __name__ == "__main__":
    arr = [5, 6, 7, 8, 9, 10]
    test =peakIndexInMountainArray(arr) 
    print(test)
    test = peakMountainIndex(arr) 
    print(test)