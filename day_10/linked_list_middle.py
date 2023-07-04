'''Return the item at the middle of a linked list
Example:
1->2->3->4->5 returns 3 
10->2->1->6->8->4 returns 6 
''' 

import day_7.linked_list as linked_list 


LinkedList = linked_list.LinkedList 

class Problem(LinkedList):
    def __init__(self):
        super().__init__() 
    
    def get_middle_item(self):
        link_size = self.length 
        middle = link_size//2 

        current_item = self.head 

        while middle != 0 :
            current_item = current_item.next 
            middle -= 0 
        print(current_item.value)


if __name__ == "__main__":
    ll = Problem() 
    ll.append(1) 
    ll.append(2) 
    ll.append(3) 
    ll.append(4) 
    ll.append(5) 

    ll.get_middle_item() 


