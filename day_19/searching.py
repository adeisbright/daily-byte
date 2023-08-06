# Implementing Searching Algorithms

# Search for a value in an unsorted array

def linear_search(nums, val):
    for num in nums:
        if num == val:
            return True
    return False


# Implement searching for an array that is already sorted

def binary_search(nums, val):
    left = 0
    right = len(nums) - 1

    while right >= left:
        mid = left + (right - left) // 2
        print(mid)
        guess = nums[mid]

        if guess == val:
            return True
        if val > nums[mid]:
            left = mid + 1
        else:
            right = mid

    return False


if __name__ == "__main__":
    nums = [1, 4, 3, 6, 9, 8]
    value = 10
    test = linear_search(nums, value)
    print(test)
    nums = [5, 10, 15, 16, 20]
    value = 5
    test = binary_search(nums, value)
    print(test)
