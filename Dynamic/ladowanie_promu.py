# Zadanie 3. (ładowanie promu) Dana jest tablica A[n] z długościami samochodów, które stoją w kolejce,
# żeby wjechać na prom. Prom ma dwa pasy (lewy i prawy), oba długości L. Proszę napisać program, który
# wyznacza, które samochody powinny pojechać na który pas, żeby na promie zmieściło się jak najwięcej aut.
# Auta muszą wjeżdżac w takiej kolejności, w jakiej są podane w tablicy A

# f(i,l,r) - czy można pierwsze i samochodów można rozmieścić tak by na lewym pasie 
# zając l miejsca, a na prawym r miejsca
# f(i,l,r) = max(f(i-1,l-A[i],r), f(i-1,l,r-A[i]))
# f(0,0,0) = 1

# wersja upgrade 
# jeśli wiemy ile aut wjechało, i ile mamy zajętego miejsca na jedynm pasie
# to możemy obliczyć ile zostało na drugim pasie
# f(i,l) - czy można pierwsze i samochodów można rozmiesić tak by na lewym pasie
# zając l miejsca
# f(i,l) = max(f(i-1, l-A[i]), f(i-1, l))
# f(0,0) = 1

def suma(A, i):
    res = 0
    for k in range(i+1):
        res += A[k]
    return res

def ferry(A, L, R):
    n = len(A)
    F = [[0 for _ in range(L+1)] for _ in range(n)]
    # warunek początkowy
    if A[0] <= R:
        F[0][0] = 1
    for l in range(L+1):
        if A[0] == l:
            F[0][l] = 1
    # main loop
    for i in range(1, n):
        for l in range(L+1):
            # spr czy jest miejsce na R
            all_cars = suma(A, i)
            if all_cars - l <= R:
                # dajemy na lewy
                if l-A[i] >= 0:
                    F[i][l] = F[i-1][l-A[i]]
                # dajemy na prawy
                F[i][l] = max(F[i][l], F[i-1][l])
    # finding res
    for l in range(L+1):
        if F[n-1][l] == 1:
            return 1, l, F
    return 0,0,0

def getting_solution(F, A, l, i):
    if i == -1:
        return
    if l-A[i] >= 0:
        if i == 0 or F[i][l] == F[i-1][l-A[i]]:
            print(f"Car {i} with lenght of {A[i]}, goes to lane L")
            return getting_solution(F, A, l-A[i], i-1)
    if suma(A,i) - l <= R:
        print(f"Car {i} with lenght of {A[i]}, goes to lane R")
        return getting_solution(F, A, l, i-1)

A = [2,3,1,1,1,2,4]
L = 7
R = 7
print(ferry(A,L,R))
flag, l, F = ferry(A,L,R)
getting_solution(F,A,l,len(A)-1)