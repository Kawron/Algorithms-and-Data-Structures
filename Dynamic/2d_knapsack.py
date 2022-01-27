# Zadanie 5 (dwuwymiarowy problem plecakowy) Proszę zaproponować algorytm dla dwuwymiarowej
# wersji dyskretnego problemu plecakowego. Mamy dany zbiór P = {p1, . . . , pn} przedmiotów i dla każdego
# przedmiotu pi dane sa nastepujace trzy liczby:
# 1. v(pi) – wartość przedmiotu,
# 2. w(pi) – waga przedmiotu, oraz
# 3. h(pi) – wysokość przedmiotu

# f(i,w,h) - największa wartość przedmiotów nie przekraczająca wagi w i wyskosci h


def knapsack_2d(A,B,C,max_w,max_h):
    n = len(A)
    F = [[[0 for _ in range(max_w+1)] for _ in range(max_h+1)] for _ in range(n)]
    # warunki początkowe
    for w in range(max_w+1):
        for h in range(max_h+1):
            if B[0] <= w and C[0] <= h:
                F[0][h][w] = A[0]
    # main loop
    for i in range(1, n):
        for w in range(max_w+1):
            for h in range(max_h+1):
                F[i][h][w] = F[i-1][h][w]
                if w >= B[i] and h >= C[i]:
                    F[i][h][w] = max(F[i][h][w], F[i-1][h-C[i]][w-B[i]]+A[i])
    return F[n-1][max_h][max_w]

A = [5,3,2,7,1,5]
B = [9,1,7,3,7,3]
C = [9,1,7,3,7,3]
max_w = 7
max_h = 7
print(knapsack_2d(A,B,C,max_w,max_h))