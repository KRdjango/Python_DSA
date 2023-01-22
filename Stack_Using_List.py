stack=[]
def push():
     element=int(input())
     stack.append(element)
     print(stack)
def pop():
     if stack==[]:
          print("Stack is Empty")
     else:
          stack.pop()
          print(stack)
def peek():
     n=len(stack)
     print(stack[n-1])
     print(stack)
def isempty():
     m=len(stack)
     if not m:
          print("Stack is empty ")
     else:
          print(stack)
while True:
     print("Enter Your Choice:",end="\n")
     print("1.push",end="\n")
     print("2.pop",end="\n")
     print("3.peek",end="\n")
     print("4.Check Stack",end="\n")
     Choice=int(input())
     if(Choice==1):
          print("Push",end="\n")
          push()
     elif(Choice==2):
          print("Pop",end="\n")
          pop()
     elif(Choice==3):
          print("Peek",end="\n")
          peek()
     elif(Choice==4):
          print("Check Stack",end="\n")
          isempty()
     elif(Choice==0):
          break;
     else:
          print("Invalid Choice")

     