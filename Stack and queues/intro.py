
from collections import deque
#here we are using deque as stack so we are using append.
stack=deque()
stack.append(2)
stack.append(3)
stack.append(4)
stack.append(5)
print(stack)
print(stack.pop())#stack LIFO so here element poped should be 5.Lets's check
print(stack)
#Now here we using deque as Queue i.e First in First out(FIFO)
dq=deque()
dq.appendleft(3)
dq.appendleft(4)
dq.appendleft(5)
dq.appendleft(6)
print(dq)
print(dq.pop())#here when we perform pop element that is inserted first should be poped.Lets see if 3 gets poped out the list or not


