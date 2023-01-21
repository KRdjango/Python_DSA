class Node:
    def __init__(self,data):
        self.data=data
        self.nref=None
        self.pref=None
class DoublyLinkedList:
    def  __init__(self):
        self.head=None
    def TraverseF(self):
        if self.head is None:
            print("LinkedList is Empty")
        else:
            n=self.head
            while n is not None:
                print(n.data,"-->",end=" ")
                n=n.nref
    def TraverseR(self):
        print()
        if self.head is None:
            print("LinkedList is Empty")
        else:
            n=self.head
            while n.nref is not None:
                n=n.nref
            while n is not None:
                print(n.data,"-->",end=" ")
                n=n.pref
    def insert_empty(self,data):
        if self.head is  None:
             new_node=Node(data)
             self.head=new_node
        else:
             print("LinkedList is Empty")
             
    def add_begin(self,data):
        new_node=Node(data)
        if self.head is  None:
            self.head=new_node
        else:
            new_node.nref=self.head
            self.head.pref=new_node
            self.head=new_node
            
    def add_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            n=self.head
            while n.nref is not None:
                n=n.nref
            n.nref=new_node
            new_node.pref=n
            
    def add_after(self,data,x):
         n=self.head
         if self.head is None:
              print("Linkedlist is Empty")
         else:
               while n is not None:
                    if x==n.data:
                         break
                    n=n.nref
               if n is None:
                    print("Given Node is not present in Linked List")
               elif n.nref is None:
                    new_node=Node(data)
                    n.nref=new_node
                    new_node.pref=n
                    new_node.nref=None
               else:
                    new_node=Node(data)
                    new_node.nref=n.nref
                    new_node.pref=n
                    n.nref.pref=new_node
                    n.nref=new_node
    def add_before(self,data,y):
         n=self.head
         if self.head is None:
              print("Linkedlist is Empty")
         else:
              while n is not None:
                   if y==n.data:
                        break
                   n=n.nref
              if n is None:
                   print("Given Node is Not present in Linked list")
              elif n.pref is None:
                   new_node=Node(data)
                   new_node.nref=n
                   new_node.pref=None
              else:
                   new_node=Node(data)
                   new_node.nref=n
                   new_node.pref=n.pref
                   n.pref.nref=new_node
                   n.pref=new_node
    def delete_begin(self):
         n=self.head
         if self.head is None:
              print("Nothing to Delete")
         else:
              self.head=self.head.nref
              self.head.pref=None
    def delete_end(self):
         n=self.head
         if self.head is None:
              print("Nothing to Delete")
         else:
              while n.nref is not None:
                    n=n.nref
              a=n.pref
              a.nref=None
    def delete_by_value(self,z):
         n=self.head
         while n.nref is not None:
               if z==n.data:
                    break
               n=n.nref
         if n is  None:
              print("Given Node is not present in the linkedlist")
              return
         if n is not None:
              n.nref.pref=n.pref
              n.pref.nref=n.nref
ddl=DoublyLinkedList()
ddl.insert_empty(200)
ddl.add_begin(100)
ddl.add_end(400)
ddl.add_after(500,400)
ddl.add_before(800,100)
ddl.add_before(300,400)
ddl.delete_begin()
ddl.delete_end()
ddl.delete_by_value(300)
ddl.TraverseF()
ddl.TraverseR()
print(ddl)