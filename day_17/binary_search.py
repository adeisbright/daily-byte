def binary_search(arr , target):
    left = 0 
    right = len(arr) - 1 

    while right >= left :
        # mid = (left + right)//2 
        mid = left + (right - left) // 2

        guess = arr[mid] 

        if guess == target :
            return mid 
        
        elif target > guess :
            left = mid + 1 
        else :
            right = mid 
            
    return -1

if __name__ == "__main__":
    arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    target = 7
    test = binary_search(arr , target)
    print(test)