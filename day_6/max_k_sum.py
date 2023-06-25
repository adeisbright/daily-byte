'''
 * QUESTION
 * ---------- 
 * Given an array of integers of size n. 
 * Our aim is to calculate the maximum sum of k
 * consecutive elements in the array.

 * EXAMPLES
 * ---------
 * Input  : arr[] = {100, 200, 300, 400} , k = 2
 * Output : 700
 * We get the maximum by using {300 , 400}
 * 
 * 
 * Input  : arr[] = {1, 4, 2, 10, 23, 3, 1, 0, 20} , k = 4 
 * Output : 39
 * We get maximum sum by adding subarray {4, 2, 10, 23} of size 4.
 * 
 * Input  : arr[] = {2, 3} , k = 3
 * Output : Invalid
 * There is no subarray of size 3 as size of whole array is 2.

'''
def max_k_sum(nums , k):
    '''
        For this problem, we already know we will have to loop over the array. 
        But the problem is which loop format should we use ; 
        We cannot use the for loop because :
        1. We want to control how the loop ends . This is because it depends on 
        the size of k 
        
        The while loop is suitable for repetions that are dynamic i.e repetition 
        that ends based on something else. 

    '''

    if(len(nums) <= k) : return "Invalid"
    
    max_sum  = 0 

    i  = 0 
    nums_length = len(nums)  

    while i + k <= nums_length:

        sub_list = nums[i:i+k] 
        sub_sum = sum(sub_list) 

        if(sub_sum > max_sum):
            max_sum = sub_sum

        i += 1 
    return max_sum 

if __name__ == "__main__":
    arr = [2, 3] 
    k = 3
    test= max_k_sum(arr , k)
    print(test)

