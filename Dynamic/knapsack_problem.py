# problem plecakowy, wersja dyskretna

# A - lista cen, B - lista wag, max_w - maksymalna waga

# f(i,w) - najlepsza cena przedmiotów od 0-i nie przekraczająca wagi w
# zakładamy że nie przedmiotów o wadze 0

def knapsack(A, B, max_w):
    n = len(A)
    F = [[0 for _ in range(max_w+1)] for _ in range(n)]
    
    # wypełnianie F
    
    for w in range(max_w+1):
        if B[0] <= w:
            F[0][w] = A[0]
    
    # główna pętla
    for i in range(1, n):
        for w in range(1, max_w+1):
            F[i][w] = F[i-1][w]
            if w >= B[i]:
                F[i][w] = max(F[i][w], F[i-1][w-B[i]]+A[i])
    
    return F[n-1][max_w], F

def solution(A, B, F, i, w):
    if i < 0:
        return []
    if i == 0:
        if w >= B[0]:
            return [i]
        return []
    if w >= B[i] and F[i][w] == F[i-1][w-B[i]] + A[i]:
        return solution(A, B, F, i-1, w-B[i]) + [i]
    return solution(A,B,F,i-1,w)

A = [4,7,2,9,6]
B = [5,1,2,9,5]
max_w = 11
sol, F = knapsack(A,B,max_w)
print(sol)
print(solution(A,B,F,len(A)-1, max_w))