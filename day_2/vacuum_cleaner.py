'''
Given a string representing the sequence of moves a robot vacuum makes, 
return whether or not it will return to its original position. 
The string will only contain L, R, U, and D characters, 
representing left, right, up, and down respectively.

Ex: Given the following strings...

"LR", return true
"URURD", return false
"RUULLDRD", return true
'''

def will_cleaner_return(moves : str) -> str :
    x_moves = 0 
    y_moves = 0 

    allowed_moves = ("L" , "R" , "U" , "D") 

    moves_dict = {
        "L" : -1 , 
        "R" : 1 , 
        "U" : 1 , 
        "D" : -1
    }
    try:
        for move in moves:
            if(move not in allowed_moves):
                raise Exception("{char} is  not a Valid Move".format(char=move))
            if move == "L" or move == "R":
                x_moves = x_moves + moves_dict.get(move) 
            else:
                y_moves = y_moves + moves_dict.get(move)
    except Exception as error:
        print(error)
        return False 
    
    return x_moves == 0 and y_moves == 0

movement = "RUULLDRDX" 

test = will_cleaner_return(movement) 
print(test)