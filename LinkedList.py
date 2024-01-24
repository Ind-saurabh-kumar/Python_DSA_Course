"""  Singly Linked List """


# Createing New Node Here
class Node:
    def __init__(self, item=None, next=None):
        self.item = item 
        self.next = next


# Creating Singly Linked List Here     
class SLL:
    def __init__(self, start = None):
        self.start = start 


    # Checking Here is empty or not
    def is_empty(self):
        return self.start == None

    # Print Elements of Linked List
    def print_list(self):
        temp = self.start
        while temp is not None:
            print(temp.item, end=' ')
            temp = temp.next

    # Insertion at start
    def insert_at_start(self, data):
        n= Node(data, self.start)
        self.start=n

    # Insertion at last of Linked List
    def inset_at_last(self, data):
        n = Node(data)
        if not self.is_empty():
            temp = self.start
            while temp.next is not None:
                temp = temp.next 
                temp.next = n
        else:
            self.start = n

    # Insertion at after in LinkedList
    def inset_after(self, temp, data):
        if temp is not None:
            n = Node(data, temp.next)
            temp.next = n


# Creating Driver Here 

sllist = SLL()
sllist.print_list()
sllist.is_empty()
sllist.insert_at_start(10)





