# Zadanie z zaba zbigniewem

def frog(A):
    n = len(A)
    energy = 0
    for i in range(n):
        energy += A[i]
    F = [[float('inf') for _ in range(energy+1)] for _ in range(n)]
    # warunek początkowy
    for i in range(energy+1):
        if A[0] == i:
            F[0][i] = 0
    # main loop
    for i in range(1,n):
        for k in range(energy+1):
            for j in range(i):
                if k-A[i]+(i-j) <= energy:
                    F[i][k] = min(F[i][k], F[j][k-A[i]+(i-j)]+1)
    # finding res
    mini = float('inf')
    for i in range(energy+1):
        mini = min(mini, F[n-1][i])
    return mini

A = [2,2,1,0,0,0]
B = [4,5,2,4,1,2,1,0]
C = [6,0,2,0,3,0,1,0,1,0,0,1]
D = [2,0,15,0,3,0,0,0,8,0,0,0]
print(frog(D))