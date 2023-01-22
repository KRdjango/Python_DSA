import collections
stack=collections.deque()
while True:
     print("1.push",end="\n")
     print("2.pop",end="\n")
     c=int(input())
     if(c==1):
          element=int(input())
          stack.append(element)
          print(stack)
     elif(c==2):
          stack.pop()
          print(stack)
     else:
          break