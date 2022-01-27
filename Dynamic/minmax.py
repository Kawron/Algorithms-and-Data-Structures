# Zadanie 5. (maximin) Rozważmy ciąg (a0, . . . , an−1) liczb naturalnych. Załóżmy, że został podzielony
# na k spójnych podciągów: (a0, . . . , a1), (a1+1, . . . , a2 ), . . . , (ak−1+1, . . . , an−1). 
# Przez wartość i-go podciągu rozumiemy sumę jego elementów a przez najgorszy podciąg rozumiemy 
# podciąg o najmniejszej wartości (rozstrzygając remisy w dowolny sposób). 
# Wartością podziału jest wartość jego najgorszego podciągu. 
# Zadanie polega na znalezienie podziału ciągu (a0, . . . , an−1) o maksymalnej wartości

# Analaogia do zadania z płoktami
# Mamy k pracowników malujących płoty, przychodzi k+1 pracownik, ile płotków dać mu do pomalowania?
# f(i,k) = max(po j) (f(i,k), min(f(j,k-1), sum(j do i)))

def suma(A, i, j):
    res = 0
    for x in range(i, j+1):
        res += A[x]
    return res

def main(A, x):
    n = len(A)
    F = [[-1 for _ in range(n)] for _ in range(x+1)]
    # warunek początkowy
    for i in range(n):
        F[0][i] = 0
        F[1][i] = suma(A,0,i)
    # main loop
    for k in range(2, x+1):
        for i in range(n):
            for j in range(i+1):
                F[k][i] = max(F[k][i], min(F[k-1][j], suma(A, j+1,i)))