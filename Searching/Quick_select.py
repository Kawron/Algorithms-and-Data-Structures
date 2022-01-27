# quickselect dzieli tablice na mniejsze lub większe bądź równe elementy x
# jeśli chcemy podział na 3 częsci patrz three-way particioning
# złożoność O(n)

def partition(arr, p, r):
    i = p-1
    pivot = arr[r]
    for j in range(p, r):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[r] = arr[r], arr[i+1]
    return i+1

def quickselect(arr, p, r, k):
    if p == r:
        return arr[p]
    q = partition(arr, p, r)
    if q == k:
        return arr[k]
    elif q < k:
        return quickselect(arr, p, q-1, k)
    else:
        return quickselect(arr, q+1, r, k)