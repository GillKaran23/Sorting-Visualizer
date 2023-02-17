import time
from colors import *

def bubblesort(data, createarray, timeTick):
    size = len(data)
    for i in range(size-1):
        for j in range(size-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                createarray(data, [BLUE if x == j or x == j+1 else RED for x in range(len(data))] )
                time.sleep(timeTick)
                
    createarray(data, [RED for x in range(len(data))])