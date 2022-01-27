# quicksort z Hoare_partition

def Hoare_partition(arr, p, r):
    pivot = arr[p]
    i = p-1
    j = r+1
    while True:
        while True:
            i += 1
            if arr[i] >= pivot:
                break
        while True:
            j -= 1
            if arr[j] <= pivot:
                break
        if i >= j:
            return j
        arr[i], arr[j] = arr[j], arr[i]


def quicksort(arr,p,r):
    if p < r:
        q = Hoare_partition(arr, p, r)
        quicksort(arr, p, q)
        quicksort(arr, q+1, r)

tab = [2,6,0,1,2,8,4,2,9,2,1,4,6]
print(tab)
quicksort(tab,0,len(tab)-1)
print(tab)