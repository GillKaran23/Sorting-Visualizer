import time
from colors import *

def merge(data, start, mid, end, createarray, timeTick):
    p = start
    q = mid + 1
    tempArray = []

    for i in range(start, end+1):
        if p > mid:
            tempArray.append(data[q])
            q+=1
        elif q > end:
            tempArray.append(data[p])
            p+=1
        elif data[p] < data[q]:
            tempArray.append(data[p])
            p+=1
        else:
            tempArray.append(data[q])
            q+=1

    for p in range(len(tempArray)):
        data[start] = tempArray[p]
        start += 1

def mergesort(data, start, end, createarray, timeTick):
    if start < end:
        mid = int((start + end) / 2)
        mergesort(data, start, mid, createarray, timeTick)
        mergesort(data, mid+1, end, createarray, timeTick)

        merge(data, start, mid, end, createarray, timeTick)

        createarray(data, [WHITE if x >= start and x < mid else BLUE if x == mid 
                        else PINK if x > mid and x <=end else RED for x in range(len(data))])
        time.sleep(timeTick)

    createarray(data, [RED for x in range(len(data))])