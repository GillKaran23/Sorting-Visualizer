import time
from colors import *

def selectionsort(data, createarray, timeTick):
    for i in range(len(data)-1):
        minimum = i
        for k in range(i+1, len(data)):
            if data[k] < data[minimum]:
                minimum = k

        data[minimum], data[i] = data[i], data[minimum]
        createarray(data, [BLUE if x == minimum or x == i else RED for x in range(len(data))] )
        time.sleep(timeTick)
        
    createarray(data, [RED for x in range(len(data))])