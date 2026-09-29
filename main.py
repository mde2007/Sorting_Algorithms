import random  # noqa: I001
import time

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

def tim_sort(arr, minrun=4):
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

A = generate_massive(100, 5000)
print(A)
A_tim = A.copy()
A_heap = A.copy()
A_bubble = A.copy()
start = time.time()
tim_sort(A_tim)
end = time.time()
print(f"Timsort: {end - start:.6f} сек")
start = time.time()
Heap_Sort(A_heap)
end = time.time()
print(f"Heap Sort: {end - start:.6f} сек")
start = time.time()
bubble_sort(A_bubble)
end = time.time()
print(f"Bubble Sort: {end - start:.6f} сек")