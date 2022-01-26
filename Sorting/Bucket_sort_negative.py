# bucket sort ale z ujemnymi liczbami

def bucket_sort(A):
    from math import floor
    n = len(A)
    buckets = [[] for _ in range(n)]
    maxi = float('-inf')
    mini = float('inf')
    for i in range(n):
        maxi = max(maxi, A[i])
        mini = min(mini, A[i])
    
    width = maxi-mini+1

    for i in range(n):
        buckets[floor(n*(A[i]-mini)/width)].append(A[i])
    
    for bucket in buckets:
        bucket.sort()

    cnt = 0
    for bucket in buckets:
        for i in range(len(bucket)):
            A[cnt] = bucket[i]
            cnt += 1