# NWP
# f(i,j) = 0 if i < 0 or j < 0
# f(i,j) = f(i-1, j-1) + 1 if A[i] == B[j]
# f(i,j) = max(f(i-1,j), f(i,j-1)) if A[i] != B[j]

def NWP(A, B):
    n = len(A)
    F = [[0 for _ in range(n)] for _ in range(n)]
    # warunki początkowe
    for i in range(n):
        if A[i] == B[0]:
            F[i][0] = 1
    for j in range(n):
        if B[j] == A[i]:
            F[0][j] = 1
    # main loop
    for i in range(1,n):
        for j in range(1,n):
            if A[i] == B[j]:
                F[i][j] = F[i-1][j-1] + 1
            else:
                F[i][j] = max(F[i-1][j], F[i][j-1])
    return F[n-1][n-1], F

def get_sol(A, B, F, i, j):
    if i < 0 or j < 0:
        return
    if A[i] == B[j]:
        get_sol(A, B, F, i-1, j-1)
        print(A[i], end=" ")
    elif F[i-1][j] > F[i][j-1]:
        get_sol(A, B, F, i-1, j)
    else:
        get_sol(A, B, F, i, j-1)
    

X = [1,5,6,2,3,4,7,8]
Y = [7,3,2,4,5,6,2,5]
sol, F = NWP(X,Y)
print(sol)
get_sol(X, Y, F, len(X)-1, len(Y)-1)