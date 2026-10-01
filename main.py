import random  # noqa: I001
import time
import tkinter as tk

def generate_massive(a, b):
    A = [random.randint(a, b) for x in range(2000)]
    return A


def bubble_sort(List):
    for i in range(len(List) - 1):
        for j in range(len(List) - 1 - i):
            if List[j] > List[j + 1]:
                List[j], List[j + 1] = List[j + 1], List[j]
    return List


def Heap_Sort(List):
    n = len(List)
    start = int(n / 2 - 1)
    for i in range(start, -1, -1):
        heapify(List, n, i)

    for i in range(n-1, 0 ,-1):
        List[0], List[i] = List[i], List[0]
        heapify(List, i, 0)
    return List

def heapify(List, n, i):
    parent = i
    leftchild = i * 2 + 1
    rightchild = i * 2 + 2
    larg = i
    if leftchild < n and List[leftchild] > List[parent]:
        larg = leftchild
    if rightchild < n and List[rightchild] > List[larg]:
        larg = rightchild

    if larg != parent:
        List[larg], List[parent] = List[parent], List[larg]
        heapify(List, n, larg)
        

def insertion_sort(arr, a, b):
    for i in range(a + 1, b):
        key = arr[i]
        j = i - 1
        while j >= a and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    return arr


def merge(arr, left, mid, right):
    left_part = arr[left:mid + 1]
    right_part = arr[mid + 1:right + 1]

    i = 0
    j = 0
    k = left

    while i < len(left_part) and j < len(right_part):
        if left_part[i] <= right_part[j]:
            arr[k] = left_part[i]
            i += 1
        else:
            arr[k] = right_part[j]
            j += 1
        k += 1

    while i < len(left_part):
        arr[k] = left_part[i]
        i += 1
        k += 1

    while j < len(right_part):
        arr[k] = right_part[j]
        j += 1
        k += 1

def find_end_run(arr, i):
    while i < len(arr) - 1:
        if arr[i] <= arr[i + 1]:
            i += 1
        else:
            break
    return i

def tim_sort(arr, minrun=32):
    n = len(arr)
    
    i = 0
    while i < n:
        run_end = find_end_run(arr, i)
        if run_end - i + 1 < minrun:
            run_end = min(i + minrun - 1, n - 1)
            insertion_sort(arr, i, run_end + 1)
        i = run_end + 1
    
    size = minrun
    while size < n:
        for left in range(0, n, 2 * size):
            mid = min(left + size - 1, n - 1)
            right = min(left + 2*size - 1, n - 1)
            if mid < right:
                merge(arr, left, mid, right)
        size *= 2
    
    return arr


def odd_even_sort(arr):
    n = len(arr)
    swap = True
    while swap:
        swap = False
        for i in range(0, n - 1, 2):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swap = True
        for i in range(1, n - 1, 2):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swap = True
    return arr
        

win = tk.Tk()
win.geometry('700x600')
win.title('Sorts')

name = tk.Label(win, text='Сортировка массива А длиной 2000 с диапазоном чисел [100; 2500]',
                font=('Arial', 12, 'bold'))
name.place(x=50, y=20)

A = generate_massive(100, 2500)
A_tim = A.copy()
A_heap = A.copy()
A_bubble = A.copy()
A_odd_ev = A.copy()
A_sort = A.copy()

results = []  

start = time.time()
tim_sort(A_tim)
end = time.time()
results.append(("Timsort", end - start))

start = time.time()
Heap_Sort(A_heap)
end = time.time()
results.append(("Heap Sort", end - start))

start = time.time()
bubble_sort(A_bubble)
end = time.time()
results.append(("Bubble Sort", end - start))

start = time.time()
odd_even_sort(A_odd_ev)
end = time.time()
results.append(("Odd-Even Sort", end - start))

start = time.perf_counter()
A_sort.sort()
end = time.perf_counter()
results.append(("Встроенная sorted()", end - start))

title = tk.Label(win, text='Результаты сортировки:', font=('Arial', 12, 'bold'))
title.place(x=50, y=70)

y_pos = 110
for name_sort, t in results:
    label = tk.Label(win, text=f"{name_sort}: {t:.6f} сек",
                    font=('Courier New', 11), anchor='w')
    label.place(x=50, y=y_pos, width=500)
    y_pos += 35

win.mainloop()