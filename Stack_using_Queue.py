import queue
stack=queue.LifoQueue()
while True:
     print("1.push",end="\n")
     print("2.pop",end="\n")
     c=int(input())
     if(c==1):
          element=int(input())
          stack.put(element)
          print(stack)
     elif(c==2):
          stack.get()
          print(stack)
     else:
          break