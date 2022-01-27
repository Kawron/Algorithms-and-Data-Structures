# Binary search działa tylko na posortowanej tablicy
# zlożoność O(log n)

def binary_search(A, p, r, val):
    q = (p+r)//2
    if A[q] == val:
        return q
    elif A[q] < val:
        return binary_search(A, p, q-1, val)
    else:
        return binary_search(A, q+1, r, val)

# binary search iteracyjny

def binary_search(T, x):
    left = 0
    right = len(T)-1
    while left <= right:
        mid = (left+right)//2
        if T[mid] == x:
            return mid
        elif T[mid] < x:
            left = mid + 1
        else:
            right = mid - 1