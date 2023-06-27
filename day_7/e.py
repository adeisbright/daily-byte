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

if __name__ == "__main__":
    print(find_max_sum([5, 9, 7, 11]))