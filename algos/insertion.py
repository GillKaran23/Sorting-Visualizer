import time
from colors import *

def insertionsort(data, createarray, timeTick):
    for i in range(len(data)):
        temp=data[i]
        k=i
        while k>0 and temp<data[k-1]:
            data[k]=data[k-1]
            k-=1
        data[k] = temp
        createarray(data,[BLUE if x==k or x==i else RED for x in range(len(data))])
        time.sleep(timeTick)

    createarray(data, [RED for x in range(len(data))])