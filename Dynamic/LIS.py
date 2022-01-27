# Longest increasing subsequence

# f(i) - najdłuższy rosnący podciąg kończący się na i
# f(0) = 1
# f(i) = max(po k) (f(i), f(k)+1) if A[k] < A[i]
def LIS(A):
    n = len(A)
    F = [-1 for _ in range(n)]
    F[0] = 1
    # main loop
    for i in range(1, n):
        for k in range(i):
            if A[k] < A[i]:
                F[i] = max(F[i], F[k]+1)
    # getting res
    maxi = -1
    for i in range(n):
        maxi = max(maxi, F[i])
    return F[i]