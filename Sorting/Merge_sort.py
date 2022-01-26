# złożoność O(nlogn)

def merge(T,p,q,r):
    new = [None] * (r-p+1)
    index = 0
    i = p
    j = q+1
    while i <= q and j <= r:
        if T[i] <= T[j]:
            new[index] = T[i]
            i += 1
        else:
            new[index] = T[j]
            j += 1
        index += 1

    while i <= q:
        new[index] = T[i]
        i += 1
        index += 1
    while j <= r:
        new[index] = T[j]
        j += 1
        index += 1
    
    index = 0
    for i in range(p, r+1):
        T[i] = new[index]
        index += 1

def merge_sort(T, p, r):
    if p < r:
        q = (p+r)//2
        merge_sort(T,p,q)
        merge_sort(T,q+1,r)
        merge(T,p,q,r)