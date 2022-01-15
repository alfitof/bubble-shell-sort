import random
import time
import copy
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt


setting1 = 10
setting2 = 100
setting3 = 1000
setting4 = 10000
setting5 = 100000



# Bubble Sort
def bubble_sort(lst):
    for i in range(0, len(lst) - 1):
        for j in range(0, len(lst) - i - 1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]

# Shell Sort
def shell_short(lst):
    gap = len(lst) // 2

    while gap > 0:
        for i in range(gap, len(lst)):
            temp = lst[i]
            j = i
            while j >= gap and lst[j-gap] > temp:
                lst[j] = lst[j-gap]
                j -= gap
            lst[j] = temp

        gap //= 2


print("1. n = 10")
print("2. n = 100")
print("3. n = 1000")
print("4. n = 10000")
print("5. n = 100000\n")

choice = input("Masukan nomor 1 - 5: ")
print("\n")

print("----------------------------Hasil Kompleksitas Waktu------------------------------")
print("Note : Dalam satuan milisecond.\n")
if choice == str(1):
    w = [random.randint(0, 10000000) for a in range(0, setting1)]
    start = time.time()
    bubble_sort(w)
    end = time.time()
    execution_time_B1 = (end - start) * 1000
    print("Bubble Sort ( n =", str(setting1), "): ", execution_time_B1)

    w = [random.randint(0, 10000000) for a in range(0, setting1)]
    start = time.time()
    shell_short(w)
    end = time.time()
    execution_time_S1 =  (end - start) * 1000
    print("Shell Sort ( n =", str(setting1), "): ", execution_time_S1)


elif choice == str(2):
    w = [random.randint(0, 10000000) for a in range(0, setting2)]
    start = time.time()
    bubble_sort(w)
    end = time.time()
    execution_time_B2 = (end - start) * 1000
    print("Bubble Sort ( n =", str(setting2), "): ", execution_time_B2)

    w = [random.randint(0, 10000000) for a in range(0, setting2)]
    start = time.time()
    shell_short(w)
    end = time.time()
    execution_time_2 = (end - start) * 1000
    print("Shell Sort ( n =", str(setting2), "): ", execution_time_2)

elif choice == str(3):
   
    w = [random.randint(0, 10000000) for a in range(0, setting3)]
    start = time.time()
    bubble_sort(w)
    end = time.time()
    execution_time_B3 = (end - start) * 1000
    print("Bubble Sort ( n =", str(setting3), "): ", execution_time_B3)

    w = [random.randint(0, 10000000) for a in range(0, setting3)]
    start = time.time()
    shell_short(w)
    end = time.time()
    execution_time_S3 = (end - start) * 1000
    print("Shell Sort ( n =", str(setting3), "): ", execution_time_S3)

elif choice == str(4):

    w = [random.randint(0, 10000000) for a in range(0, setting4)]
    start = time.time()
    bubble_sort(w)
    end = time.time()
    execution_timeb4 = (end - start) * 1000
    print("Bubble Sort ( n =", str(setting4), "): ", execution_timeb4)

    w = [random.randint(0, 10000000) for a in range(0, setting4)]
    start = time.time()
    shell_short(w)
    end = time.time()
    execution_time_S4 = (end - start) * 1000
    print("Shell Sort ( n =", str(setting4), "): ", execution_time_S4)


elif choice == str(5):

    w = [random.randint(0, 10000000) for a in range(0, setting5)]
    start = time.time()
    bubble_sort(w)
    end = time.time()
    execution_time_B5 = (end - start) * 1000
    print("Bubble Sort ( n =", str(setting5), "): ", execution_time_B5)

    w = [random.randint(0, 10000000) for a in range(0, setting5)]
    start = time.time()
    shell_short(w)
    end = time.time()
    execution_time_S5 = (end - start) * 1000
    print("Shell Sort ( n =", str(setting5), "): ", execution_time_S5)

print("\n")
shell1 = np.array([10,100,1000,10000,100000])
shell2 = np.array([0.012159347534179688, 0.18525123596191406, 5.523204803466797, 65.52982330322266, 1297.572135952935])    #Sebagian memakai data running time di tabel laporan karena running lama dan cukup berat

bubble1 = np.array([10,100,1000,10000,100000])
bubble2 = np.array([0.016689300537109375, 0.965118408203125, 107.95736312866211, 11170.684337615967, 1322872.4863529205])   #Sebagian memakai data running time di tabel laporan karena running lama dan cukup berat

plt.title("Perbandingan Running time")
plt.xlabel("n")
plt.ylabel("Waktu(ms)")

plt.plot(shell1, shell2, label="Shell Sort")
plt.plot(bubble1, bubble2, label="Bubble Sort")
plt.legend()
plt.show()