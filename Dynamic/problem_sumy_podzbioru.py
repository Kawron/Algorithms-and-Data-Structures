# Zadanie 2. (problem sumy podzbioru) Dana jest tablica n liczb naturalnych A. 
# Proszę podać i zaimplementować algorytm, który sprawdza, czy da się wybrać podciąg liczb z A, 
# które sumują się do zadanej wartości T.

# f(i,k) - czy istnieje podciąg sumujący się do k wśród indeksów od 0 do i
# f(0,k) = True if A[0] == k else False
# f(i,k) = max(f(i-1, k), f(i-1, k-A[i]))

def main(A,k):
    n = len(A)
    F = [[0 for _ in range(k+1)] for _ in range(n)]
    P = [[0 for _ in range(k+1)] for _ in range(n)]

    for val in range(k+1):
        if A[0] == val:
            F[0][val] = 1
            P[0][val] = 1
    
    for i in range(1,n):
        for val in range(k+1):
            F[i][val] = F[i-1][val]
            P[i][val] = 0
            if val-A[i] >= 0 and F[i-1][val-A[i]] > F[i-1][val]:
                F[i][val] = F[i-1][val-A[i]]
                P[i][val] = 1
    return F[n-1][k], P

def get_sol(A, P, i, val):
    if i < 0 or val == 0:
        return
    if P[i][val] == 1:
        print(A[i], end=" ")
        return get_sol(A, P, i-1, val-A[i])
    get_sol(A, P, i-1, val)

test = [3,34,4,12,5,2]
k = 42
sol, P = main(test, k)
print(sol)
get_sol(test, P, len(test)-1, k)