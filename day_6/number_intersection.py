'''
Given two integer arrays, return their intersection.
Note: the intersection is the set of elements that are common to both arrays.

Ex: Given the following arrays...

nums1 = [2, 4, 4, 2], nums2 = [2, 4], return [2, 4]
nums1 = [1, 2, 3, 3], nums2 = [3, 3], return [3]
nums1 = [2, 4, 6, 8], nums2 = [1, 3, 5, 7], return []

'''
def number_intersections(nums1 , nums2):
    ''' Return the common numbers in the two sets '''
    nums1_hash = set()  
    nums2_hash = set() 

    common_nums = []
    for num in nums1:
        nums1_hash.add(num) 
    for num in nums2:
        nums2_hash.add(num) 

    for num in nums2_hash:
        if num in nums1_hash:
            common_nums.append(num)
    return common_nums

if __name__ == "__main__":
    nums1 = [1, 2, 3, 3]
    nums2 =  [3,3]
    
    test= number_intersections(nums1 , nums2)
    print(test)