# Zadanie 1. (Black Forest) Black Forest to las rosnący na osi liczbowej gdzieś w południowej Anglii. Las
# składa się z n drzew rosnących na pozycjach 0, . . . , n−1. Dla każdego i ∈ {0, . . . , n−1} znany jest zysk ci
# jaki można osiągnąć ścinając drzewo z pozycji i. John Lovenoses chce uzyskać maksymalny zysk ze ścinanych
# drzew, ale prawo zabrania ścinania dwóch drzew pod rząd. Proszę zaproponować algorytm, dzięki któremu
# John znajdzie optymalny plan wycinki.

# f(i) - najlepszy zysk z ścinania drzew od 0 do i, nie wiemy czy ścinamy i
# g(i) - najlepszy zysk z ścinania drzew od 0 do i, nie ścinamy i

# g(i) = f(i-1)
# f(i) = max(g(i), g(i-1)+A[i])

# bottom-up

def bottom_up(C):
    n = len(C)
    F = [-1 for _ in range(n)]
    G = [-1 for _ in range(n)]
    F[0] = C[0]
    G[0] = 0
    # main loop
    for i in range(1,n):
        G[i] = F[i-1]
        F[i] = max(G[i], G[i-1]+C[i])
    return F[n-1]

# up-bottom

def main(C):

    def f(i):
        if i == 0:
            return C[0]
        if F[i] != -1:
            return F[i]
        F[i] = max(g(i), g(i-1)+C[i])
        return F[i]

    def g(i):
        if i == 0:
            return 0
        if G[i] != -1:
            return G[i]
        G[i] = f(i-1)
        return G[i]

    n = len(C)
    F = [-1 for _ in range(n)]
    G = [-1 for _ in range(n)]
    F[0] = C[0]
    G[0] = 0
    return f(n-1)

C = [2,5,6,7,8]
print(bottom_up(C))
print(main(C))