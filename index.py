from tkinter import *
from tkinter import ttk
import random
from colors import *

#Algorithms 
from algos.bubble import bubblesort
from algos.merge import mergesort
from algos.insertion import insertionsort
from algos.quick import quicksort
from algos.selection import selectionsort

#Index Window 
root = Tk()
root.title("Sorting Visualizer")
root.maxsize(1000, 1000)
root.config(bg = SKIN)
l = Label(root, font="times_roman 30 bold ", fg=PURPLE ,text="VISUALIZER", bg=SKIN)
l.grid(row=0, column=0, padx=10, pady=5)

algorithm_name = StringVar()
algo_list = ['Bubble Sort', 'Merge Sort', 'Insertion Sort','Quick Sort','Selection Sort']

speed_name = StringVar()
speed_list = ['Fast', 'Medium', 'Slow']

data = []


def createarray(data, bars):
    arrbox.delete("all")
    arrboxwidth = 800
    arrboxheight = 400
    width_x = arrboxwidth / (len(data) + 1)
    offset = 4
    space = 5
    structured_bars= [i / max(data) for i in data]

    for i, height in enumerate(structured_bars):
        x0 = i * width_x + offset + space
        y0 = arrboxheight - height * 390
        x1 = (i + 1) * width_x + offset
        y1 = arrboxheight
        arrbox.create_rectangle(x0, y0, x1, y1, fill=bars[i])

    root.update_idletasks()


#BARS
def generate():
    global data

    data = []
    for i in range(0, 30):
        randvalue = random.randint(1, 150)
        data.append(randvalue)

    createarray(data, [RED for x in range(len(data))])

#SPEED
def set_speed():
    if speed.get() == 'Slow':
        return 0.4
    elif speed.get() == 'Medium':
        return 0.2
    else:
        return 0.002

#SORTING
def sort():
    global data
    timeTick = set_speed()
    
    if methods.get() == 'Bubble Sort':
        bubblesort(data, createarray, timeTick)
    elif methods.get() == 'Merge Sort':
        mergesort(data, 0, len(data)-1, createarray, timeTick)
    elif methods.get() == 'Insertion Sort':
        insertionsort(data, createarray, timeTick)
    elif methods.get() == 'Quick Sort':
        quicksort(data, 0, len(data)-1, createarray, timeTick)
    elif methods.get() == 'Selection Sort':
        selectionsort(data, createarray, timeTick)

#EXIT
def exit():
    root.destroy()

#INPUTS 
userinputs = Frame(root, width= 900, height=300, bg=SKIN)
userinputs.grid(row=2, column=0, padx=15, pady=10)

#METHODS
l1 = Label(userinputs, text="Methods: ", bg=WHITE)
l1.grid(row=0, column=0, padx=10, pady=5, sticky=W)
methods = ttk.Combobox(userinputs, textvariable=algorithm_name, values=algo_list)
methods.grid(row=0, column=1, padx=5, pady=5)
methods.current(0)

l2 = Label(userinputs, text="Speed: ", bg=WHITE)
l2.grid(row=0, column=2, padx=10, pady=5, sticky=W)
speed = ttk.Combobox(userinputs, textvariable=speed_name, values=speed_list)
speed.grid(row=0, column=3, padx=5, pady=5)
speed.current(0)

#START
b1 = Button(userinputs, text="Start", command=sort, bg=GRAY)
b1.grid(row=0, column=5, padx=5, pady=5)

#BARS 
b3 = Button(userinputs, text="Create Bars",command=generate, bg=GRAY)
b3.grid(row=0, column=4, padx=5, pady=5)

#EXIT
b3 = Button(userinputs, text="Exit", command=exit, bg=GRAY)
b3.grid(row=0, column=6, padx=5, pady=5)


#BARBOX 
arrbox = Canvas(root, width=780, height=400, bg=BLACK)
arrbox.grid(row=1, column=0, padx=10, pady=5)

root.mainloop()