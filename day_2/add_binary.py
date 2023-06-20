'''
 Given two binary strings (strings containing only 1s and 0s) return their sum (also as a binary string).
Note: neither binary string will contain leading 0s unless the string itself is 0

Ex: Given the following binary strings...

"100" + "1", return "101"
"11" + "1", return "100"
"1" + "0", return  "1"
'''

def add_binary_wrong(a , b):
    '''
        Adds two binary numbers together. 
        Step 1: Check for which string has the largest length 
        1 + 1 > 1 = 0 carryover 1 
    '''
    carry_over ="0" 
    a_length = len(a) 
    b_length = len(b)
    x = a if a_length > b_length else b 
    loop_count = 1 
    
    result = ""

    for char in x :
        if(loop_count > b_length ):
            val = carry_over + char 
            if (int(val) > 1) : val = "01"

            result = result + str(val) 
            print(result)
            return "".join(reversed(result))
        
        a_value = int(a[-loop_count]) + int(carry_over)

        if a_value  > 1 : a_value = "1"
        
        sum = int(a_value) + int(b[-loop_count]) 

        if(sum > 1):
            carry_over = "1"
            sum = "0"
        else:
            carry_over = "0"
        print("When loop is {loop}, sum is {sum}".format(loop = loop_count , sum = sum))

        result = result + str(sum) 
        loop_count = loop_count + 1
    return "".join(reversed(result))


#correct version 

def add_binary(a , b):
    '''Adds two binary numbers, and returns their results'''

    carry_over = 0  

    ai = len(a) - 1
    bi = len(b) - 1 
    
    result = ""

    while ai >= 0 or bi >= 0 :

        ath = int(a[ai]) if ai >= 0 else 0 
        bth = int(b[bi]) if bi >= 0 else 0 

        carry_sum = carry_over + ath + bth 

        result += str(carry_sum % 2)
        carry_over = carry_sum//2 

        ai -= 1 
        bi -= 1 

    if carry_over > 0:
        result += str(carry_over)
    
    return "".join(reversed(result))
    

a = "100" 
b = "1"
test = add_binary(a , b) 
print(test)

