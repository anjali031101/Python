class Node:
    def __init__(self, value):
        self.value=value
        self.next=None
        
class Linkedlist:
    def __init__(self,value):
        new_node = Node(value)
        self.head= new_node
        self.tail= new_node
        self.length = 1
        print("Linked list created with value:",value)
        
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp=temp.next
            
    def get_head(self):
        if self.head is None:
            print("Head:None")
        else:
            print("Head:",self.head.value)
            
    def get_tail(self):
        if self.tail is None:
            print("Tail:None")
        else:
            print("Tail:",self.tail.value)
            
    def get_length(self):
        print("Length:",self.length)
        
    