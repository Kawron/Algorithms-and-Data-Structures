# bucket sort - wersja co działa też na liczby nie pomiędzy [0,1) ale musi być >= 0
# złożoność gdy liczby są rozłożone jednostajnie na przedziale: O(n)
# ogólnie O(n^2)
# jeśli chcemy także dla ujemnych liczb patrz Bucket_sort_negative

def bucket_sort(A):
    from math import floor
    n = len(A)
    buckets = [[]for _ in range(n)]

    maxi = float('-inf')
    for i in range(n):
        maxi = max(maxi, A[i])
    maxi += 1

    for i in range(n):
        buckets[floor(n*A[i]/maxi)].append(A[i])

    for bucket in buckets:
        bucket.sort()
    
    cnt = 0
    for bucket in buckets:
        for i in range(len(bucket)):
            A[cnt] = bucket[i]
            cnt += 1