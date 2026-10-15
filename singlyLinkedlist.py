# class Node:                      #For Creating a node in lined list
#     def __init__(self,data):
#         self.data=data
#         self.ref=None
# class LinkedList:                 #creating a linked list
#     def __init__(self):
#        self.head=None

#     def print_lst(self):
#         if self.head is None:
#             print("Linked list is empty")
#         else:
#             n=self.head
#             while n is not None:       #traversing through linked list and printing it
#                 print(n.data)
#                 n=n.ref
#     def add_begin(self,data):          #adding node ath the beginnig of the linked list
#         new_node=Node(data)
#         new_node.ref=self.head
#         self.head=new_node


# LL1=LinkedList()
# LL1.add_begin(10)
# LL1.add_begin(20)
# LL1.print_lst()

class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None

class LinkedList:
    def __init__(self):
        self.head=None

    def print_ll(self):
        if self.head is None:
            print("Linked List is Empty")
        else:
            n=self.head
            while n is not None:
                print(n.data)
                n=n.ref
    def add_begin(self,data):
        new_node=Node(data)
        new_node.ref=self.head
        self.head=new_node
LL1=LinkedList()
LL1.add_begin(30)
LL1.add_begin(20)
LL1.add_begin(10)
LL1.add_begin(5)
LL1.print_ll()