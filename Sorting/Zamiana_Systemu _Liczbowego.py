# Proszę zaimplementować jak najszybszy algorytm sortujący n elementową 
# tablicę zawierajacą liczby ze zbioru [0,1,2,...,n^2-1]

# Opis algorytmu: n^2-1 to maksymalna liczba jaką możemy dostać przy
# uzyciu dwóch cyfr w systemie n. A więc każdą liczbę z tego przedziału
# możemy zapisać jako a*n+b. Gdy zapiszemy tak każdą liczbę możemy użyć
# radix sorta do posortowania tych liczb

def counting_sort(A, k, row):
    C = [0]*k
    B = [0]*len(A)
    for i in range(len(A)):
        C[A[i][row]] += 1
    
    for i in range(1, k):
        C[i] += C[i-1]
    
    for i in range(len(A)-1,-1,-1):
        C[A[i][row]] -= 1
        B[C[A[i][row]]] = A[i]
    
    # jeśli chcemy w spsoób
    # malejący to możemy wpisywać
    # na odwrót
    for i in range(len(A)):
        A[i] = B[i]

def radix_sort(A):
    n = len(A)

    for i in range(n):
        A[i] = [A[i]//n, A[i]%n]
    
    counting_sort(A,n,1)
    counting_sort(A,n,0)

    for i in range(n):
        A[i] = A[i][0]*n + A[i][1]

A = [55,11,2,99,23,3,12,65,23,67]
print(A)
radix_sort(A)
print(A)