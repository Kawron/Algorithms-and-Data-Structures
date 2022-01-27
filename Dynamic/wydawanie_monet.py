# Zadanie 6. (wydawanie monet) Mamy daną tablicę z nominałami monet stosowanych w pewnym dziwnym kraju, 
# oraz kwotę T. Proszę podać algorytm, który oblicza minimalną ilość monet potrzebną do wydania
# kwoty T (algorytm zachłanny, wydający najpierw największą monetę, nie działa: dla monet 1, 5, 8 wyda
# kwotę 15 jako 8 + 5 + 1 + 1 zamiast 5 + 5 + 5).


# rozw O(n^3)
# f(i,x) - najmniejsza ilość monet by wydać sume x przy użyciu i-tego nominałach

# f(i,x) = min(po k, 0<=k<=len(A))(f(k, x-i)+1, f(i,x))

def main(A, x):
    n = len(A)
    F = [[float('inf') for _ in range(n)] for _ in range(x+1)]
    # warunki początkowe
    for i in range(n):
        F[0][i] = 0
    # main loop
    for i in range(n):
        for j in range(x+1):
            for k in range(n):
                F[j][i] = min(F[j-A[i]][k]+1, F[j][i])
    # res
    mini = float('inf')
    for i in range(n):
        mini = min(mini, F[x][i])
    return mini

A = [1,5,8]
x = 24
print(main(A, x))

# rozw O(n*x)
# 1. mamy jednowymiarową tablice F[i] gdzie trzymamy minimalną
# ilość monet do wydania sumy i gdzie i: 0<=i<=x
# 2. początkowo tablica jest wypełniona inf poza F[0] = 0
# 3. następnie dla każdego nominału i i dla każdej sumy j: 0<=j<=x-i
# wykonuje następujący algorytm: sprawdzam czy T[j]+1 < T[i+j] jeśli tak
# to updateuje wartość T[j+i] oznacza to że najmniejszą wartość reszty dla 
# T[j+i] mogę uzyskać dodając nominał i do sumy j.


def coin_change(A, x):
    F = [float('inf') for _ in range(x+1)]
    P = [-1 for _ in range(x+1)]
    F[0] = 0

    for i in A:
        for j in range(x+1-i):
            if F[j]+1 < F[j+i]:
                F[j+i] = F[j]+1
                P[j+i] = i
    return F, P

def get_sol(P, x):
    if x == 0:
        return
    nom = P[x]
    print(nom, end=" ")
    get_sol(P, x-nom)

A = [1,5,8]
x = 21
F, P = coin_change(A,x)
print(F)
get_sol(P, x)