'''
Given two arrays of numbers, where the first array 
is a subset of the second array, return an array 
containing all the next greater elements for each element
in the first array, in the second array. If there is 
no greater element for any element, output -1 for that number.

Ex: Given the following arrays…

nums1 = [4,1,2], nums2 = [1,3,4,2], return [-1, 3, -1] 
because no element in nums2 is greater than 4,
 3 is the first number in nums2 greater than 1, 
 and no element in nums2 is greater than 2.

nums1 = [2,4], nums2 = [1,2,3,4], return [3, -1] 
because 3 is the first greater element that occurs 
in nums2 after 2 and no element is greater than 4.
'''
def greater_elements(child , parent):
    bigger = [] 
    for j , num in enumerate(child) :
        replacer = -1 
        for index,e in enumerate(parent):
            if e > num:
                replacer = e 
                parent.pop(j)
                break
            
        bigger.append(replacer)
    return bigger 

if __name__ == "__main__":
    nums1 = [4,1,2]
    nums2 = [1,3,4,2]
    test = greater_elements(nums1 , nums2)
    print(test) #[-1, 3, -1] 
