import time
from colors import *

def partition(data, start, end, createarray, timeTick):
    i = start + 1
    pivot = data[start]

    for j in range(start+1, end+1):
        if data[j] < pivot:
            data[i], data[j] = data[j], data[i]
            i+=1
    data[start], data[i-1] = data[i-1], data[start]
    return i-1

def quicksort(data, start, end, createarray, timeTick):
    if start < end:
        pivot_position = partition(data, start, end, createarray, timeTick)
        quicksort(data, start, pivot_position-1, createarray, timeTick)
        quicksort(data, pivot_position+1, end, createarray, timeTick)

        createarray(data, [WHITE if x >= start and x < pivot_position else BLUE if x == pivot_position
                        else PINK if x > pivot_position and x <=end else RED for x in range(len(data))])
        time.sleep(timeTick)
        
    createarray(data, [RED for x in range(len(data))])