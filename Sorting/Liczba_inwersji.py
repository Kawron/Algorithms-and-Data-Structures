# Podaj liczbę inwersji w tablicy
# korzystamy z merge sorta

# Opis algorytmu: Stosujemy merge_sorta, za każdym razem gdy przy mergu
# bierzemy element z "prawej" tablicy to oznacza to, że wszytskie nie wzięte elementy
# z lewej tablicy są w inwersji z właśnie wziętym elementem. W ten sposób zliczamy
# wszystkie inwersje

def merge(T,p,q,r):
    new = [None] * (r-p+1)
    index = 0
    cnt = 0
    i = p
    j = q+1
    while i <= q and j <= r:
        if T[i] <= T[j]:
            new[index] = T[i]
            i += 1
        else:
            new[index] = T[j]
            j += 1
            cnt += q-i+1
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
    return cnt

def merge_sort(tab, p, r):
    cnt = 0
    if p < r:
        q = (p+r)//2
        cnt += merge_sort(tab,p,q)
        cnt += merge_sort(tab,q+1,r)
        cnt += merge(tab,p,q,r)
    return cnt


T = [5,3,4,2]
res = merge_sort(T, 0, len(T)-1)
print(res)
print(T)