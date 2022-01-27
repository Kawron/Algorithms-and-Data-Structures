# Zadanie 2. (spadające klocki) Każdy klocek to przedział postaci [a, b]. Dany jest ciąg klocków [a1, b1],
# [a2, b2], . . ., [an, bn]. Klocki spadają na oś liczbową w kolejności podanej w ciągu. Proszę zaproponować
# algorytm, który oblicza ile klocków należy usunąć z listy tak, zeby każdy kolejny spadajacy klocek mieścił
# się w całości w tam, który spadł tuż przed nim.

# f(i) - ile minimalnie klocków trzeba usunąc by i-ty klocek dobrze spadł
# f(i) = min(po k) (f(i), f(k)+(i-k+1))
# f(0) = 0

def can_on_top(A,i,k):
    if A[i][0] >= A[k][0] and A[i][1] <= A[k][1]:
        return True
    else:
        return False

def second(A):
    n = len(A)
    F = [float('inf') for _ in range(n)]
    F[0] = 0
    # main loop
    for i in range(1, n):
        for k in range(0, i):
            if can_on_top(A,i,k):
                F[i] = min(F[i], F[k]+(i-k-1))
    # getting res
    mini = float('inf')
    for i in range(n):
        mini = min(mini, F[i]+(n-1-i))
    return mini

C = [(1,4),(2,3),(0,5),(1,4),(2,3),(1,4),(2,3)]
print(second(C))