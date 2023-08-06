def find_max_sum(numbers):
  
    numbers_length = len(numbers)
    if numbers_length < 2 : 
      return 0 
    
    first_max = max(numbers[0] , numbers[1]) 
    second_max = min(numbers[0] , numbers[1]) 

    for i in range(2 , numbers_length):
      if numbers[i] > first_max:
        second_max = first_max 
        first_max = numbers[i]
        
      elif numbers[i] > second_max:
        second_max = numbers[i]

    return first_max + second_max    



def solution(nums):
    n = len(nums) 
    first = max(nums[0] , nums[1]) 
    second = min(nums[0] , nums[1]) 

    for i in range(2 , n):
        if nums[i] > first :
          second = first 
          first = nums[i] 
        elif nums[i] > second :
           second = nums[i]
    


    return first + second 





if __name__ == "__main__":
    print(solution([5, 9, 7, 11]))