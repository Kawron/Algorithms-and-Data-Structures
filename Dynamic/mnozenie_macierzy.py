def matrix_multiplication(A):
    n = len(A)
    F = [[float('inf') for _ in range(n)] for _ in range(n)]
    # warunek początkowy
    for i in range(n):
        F[i][i] = 0
    # main loop
    for l in range(1, n):
        for i in range(n-l):
            j = i+l
            for k in range(i, j):
                n_val = F[i][k] + F[k+1][j] + A[i][0]*A[k][1]*A[j][1]
                if n_val < F[i][j]:
                    F[i][j] = n_val
    for row in F:
        print(row)

P = [(10,5),(5,100),(100,50)]
S = [(2,5),(5,10),(10,3),(3,7),(7,6)]
G = [(7,9),(9,2),(2,3),(3,4),(4,5),(5,10)]
print(matrix_multiplication(G))