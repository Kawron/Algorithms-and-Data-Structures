# Zadanie 6 (największy przedział). Dany jest ciąg przedziałów domkniętych [a1, b1], . . . ,[an, bn]. Proszę
# zapropnować algorytm, który znajduje taki przedział [at, bt], w którym w całości zawiera się jak najwięcej
# innych przedziałów.

# tworze tablice A = [start, idx] B = [end, idx_A] res = [res]
# 1.sortuje A po początkach malejąco
# 2.updateuje idx_A w B
# 3.sortuje B po końcach rosnąco
# 4.wpisuje wyniki do res

def main(tab):
    n = len(tab)
    res = [0 for _ in range(n)]
    A = [[None, None] for _ in range(n)]
    B = [[None, None] for _ in range(n)]
    for i in range(n):
        A[i][0] = tab[i][0]
        B[i][0] = tab[i][1]
        A[i][1] = i
    A.sort(key=lambda x:x[0])

    for i in range(n):
        idx = A[i][1]
        B[idx][1] = i
    B.sort(key=lambda x:(x[0], n-x[1]-1))

    for i in range(n):
        value = i
        idx_A = B[i][1]
        value += n-idx_A-1
        idx = A[idx_A][1]
        res[idx] = value

    
    print(A)
    print(B)
    print(res)

tab = [[1,14],[12,16],[15,16],[14,16],[13,16],[2,3],[3,4],[0,2]]
main(tab)