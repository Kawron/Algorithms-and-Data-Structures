# złożoność O(nlogn)

# basic wersja
def partition(A,p,r):
    x = A[r]
    i = p-1
    for j in range(p,r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1

def quick_sort(A,p,r):
    if p < r:
        q = partition(A,p,r)
        quick_sort(A,p,q-1)
        quick_sort(A,q+1,r)

# usunięcie rekurencji ogonowej
def partition(A,p,r):
    x = A[r]
    i = p-1
    for j in range(p,r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1

def quick_sort(A,p,r):
    while p < r:
        q = partition(A,p,r)
        quick_sort(A,p,q-1)
        p = q+1

# zmniejszenie zużytej pamięci

def partition(A,p,r):
    x = A[r]
    i = p-1
    for j in range(p,r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1

def quick_sort(A,p,r):
    while p < r:
        q = partition(A,p,r)
        if q-p <= r-q:
            quick_sort(A, p, q-1)
            p = q + 1
        else:
            quick_sort(A,q+1,r)
            r = q-1