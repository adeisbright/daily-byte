def bubble_sort(nums):
    n = len(nums)
    for i in range(n):
  
        for k in range(i , n):
            if nums[i] < nums[k]:
                temp = nums[k]
                nums[k] = nums[i] 
                nums[i] = temp 

    return nums 

if __name__ == "__main__" :
    nums = [1 , 2 , 4 , 3]  
    test = bubble_sort(nums) 

    print(test)

