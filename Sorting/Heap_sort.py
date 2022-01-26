# kopiec na tablicy
# max heap
# złożoność O(nlogn)
# heapify O(logn)
# buildheap O(n)
import math

def left(i):
    return 2*i+1

def right(i):
    return 2*i+2

def parent(i):
    return (i-1)//2

def heapify(A, n, i):
    l = left(i)
    r = right(i)
    m = i

    if l < n and A[l] > A[m]: m = l
    if r < n and A[r] > A[m]: m = r
    if m != i:
        A[i], A[m] = A[m], A[i]
        heapify(A, n ,m)

def build_heap(A):
    n = len(A)
    for i in range(parent(n-1),-1,-1):
        heapify(A, n, i)

def heapsort(A):
    n = len(A)
    build_heap(A)
    for i in range(n-1,0,-1):
        A[0], A[i] = A[i], A[0]
        heapify(A, i, 0)

def insert(A, key):
    n = len(A)
    A.append(key)
    i = n
    while True:
        p = parent(i)
        if p >= 0 and A[p] < A[i]:
            A[p], A[i] = A[i], A[p]
            i = p
            continue
        break

def delete(A, i):
    n = len(A)
    A[i], A[n-1] = A[n-1], A[i]
    A.pop()
    heapify(A,n-1,i)

# funkcja do printowania heap
def print_heap(A):
    n = len(A)
    h = math.floor(math.log2(n))
    width = 3*(2**(h))
    cnt = 0
    idx = 0
    for row in range(h+1):
        col_width = width//(2**row)
        for key in range(2**row):
            if idx+key > n-1:
                break
            out = " " + str(A[idx+key]) + " "
            print(out.center(col_width), end="")
            cnt += 1
        idx = cnt
        print()

A = [4,1,3,2,16,9,10,14,8,7]
build_heap(A)
print(A)
print_heap(A)