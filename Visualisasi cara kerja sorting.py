from tkinter import *
import time
import random

root = Tk()
root.title('Visualisasi Bubble Sort & Shell Sort')
root.geometry("880x640")
root.config (bg='white')

arr1 = []
arr2 = []
time_start = time.time()

def drawArr(arr, color, canvas):
    canvas.delete("all")
    c_width = 340
    c_height = 240
    x_width = c_width / (len(arr) + 1)
    offset = 10
    space = 5
    normalizedarr = [ i / max(arr) for i in arr]
    for i, height in enumerate(normalizedarr):
        
        x0 = i * x_width + offset + space
        y0 = c_height - height * 210
       
        x1 = (i + 1) * x_width + offset
        y1 = c_height

        canvas.create_rectangle(x0, y0, x1, y1, fill=color[i])

    root.update_idletasks()
    
def randomArray():
    global arr1
    global arr2
    arr1 = []  
    arr2 = []
    
    length = int(inputN.get())
    for _ in range(length):
        arr1.append(random.randrange(1, 100))
    arr2[:] = arr1[:]
    drawArr(arr1,['red' for x in range(len(arr1))],canvas1)
    drawArr(arr2,['red' for x in range(len(arr2))],canvas2)

def shell_sort(data,drawArr,canvas):
    global time_start
    time_start = time.time()    
    gap = len(data) // 2

    while gap > 0:
        for i in range(gap,len(data)):
            temp = data[i]
            j = i
            while j >= gap and data[j-gap] > temp:
                data[j] = data[j-gap]
                drawArr(data, ['green' if x == j or x == j+1 else 'red' for x in range(len(data))], canvas)
                updateTime(runTime2,time_start)
                j -= gap
            data[j] = temp
        gap //= 2
    drawArr(data, ['green' for x in range(len(data))], canvas)


def bubbleSort(data, drawArr, canvas):

    global time_start
    time_start = time.time()
    for i in range(len(data)):
        for j in range(0, len(data) - i - 1):
            if data[j] > data[j + 1]:
                temp = data[j]
                data[j] = data[j+1]
                drawArr(data, ['green' if x == j or x == j+1 else 'red' for x in range(len(data))], canvas)
                updateTime(runTime1,time_start)
                data[j+1] = temp
    drawArr(data, ['green' for x in range(len(data))], canvas)



def run():
    global arr1
    global arr2

    bubbleSort(arr1, drawArr, canvas1)
    shell_sort(arr2, drawArr, canvas2)

def updateTime(timeLabel,startTime):
    timeLabel.config(text=time.time() - time_start)

frameTombol = Frame(root, width = 720, height = 50, bg ='white')
frameTombol.grid(row = 0, column=0, padx =10, pady=10)

Label(frameTombol, text="n =", bg= 'white').grid(row=0, column=0, padx=5,pady=5)
inputN = Entry(frameTombol)
inputN.grid(row=1, column=0, padx=5,pady=5)

tombolRandm =Button(frameTombol, text="Acak Array", command=randomArray)
tombolRandm.grid(row=1, column=3, padx=5, pady=5)

tombolMulai = Button(frameTombol, text="Start", command=run)
tombolMulai.grid(row=1, column=5, padx=5, pady=5)

canvas1 = Canvas(root, width=340, height=240, bg = 'grey')
Label(text="Shell sort", bg= 'white').grid(row=2, column=1, padx=0,pady=0)
canvas1.grid(row=1, column=1, padx=1, pady=1)


canvas2 = Canvas(root, width=340, height=240, bg = 'grey')
Label(text="Bubble sort", bg= 'white').grid(row=0, column=1, padx=0,pady=0)
canvas2.grid(row=3, column=1, padx=1, pady=1)


frameText1 = Frame(root, width = 720, height = 50, bg='white')
Label(frameText1)
runTime1 = Label(frameText1,bg = "white")

frameText2 = Frame(root, width = 720, height = 50, bg='white')
runTime2 = Label(frameText2,  bg = "white")


root.mainloop()