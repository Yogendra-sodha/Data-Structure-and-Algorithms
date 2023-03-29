from collections import deque
# Functions in dequeue module
# deque(maxlen = n)
# append
# popleft
# clear

csq = deque(maxlen = 2)
csq.append(1)
csq.append(2)
print(csq)
csq.popleft()
print(csq)
csq.clear()
print(csq)

import queue as q
from multiprocessing import Queue

# put() == enqueue
# get() == dequeue
# empty == clear
# full() == 
# task_done() == to see if queue is done in concurrent
# join() == to see if work allocated is done