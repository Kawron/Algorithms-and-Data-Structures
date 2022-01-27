from collections import deque

def Edmonds_Karp(G, s, t):
    n = len(G)
    flow = 0
    F = [[0 for _ in range(n)] for _ in range(n)]
    while True:
        parent, cap = bfs(G,F,s,t)
        if cap == 0:
            return flow
        flow += cap
        v = t
        while v != s:
            u = parent[v]
            F[u][v] += cap
            F[v][u] -= cap
            v = u

def bfs(G, F, s, t):
    n = len(G)
    deq = deque()
    parent = [-1 for i in range(n)]
    parent[s] = None
    C = [0 for i in range(n)]
    C[s] = float('inf')
    deq.append(s)
    while len(deq) != 0:
        u = deq.popleft()
        for v in range(n):
            if v != u and G[u][v]-F[u][v] > 0 and parent[v] == -1:
                parent[v] = u
                C[v] = min(C[u], G[u][v]-F[u][v])
                if v == t:
                    return parent, C[t]
                deq.append(v)
    return parent, C[t]

G = [[0, 0, 5, 0, 0, 0, 6, 0, 0, 0],
[0, 0, 0, 0, 0, 1, 0, 0, 0, 0], 
[0, 0, 0, 2, 2, 0, 0, 0, 0, 0], 
[0, 1, 0, 0, 1, 0, 2, 0, 0, 0], 
[0, 0, 0, 0, 0, 5, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 0, 0, 0, 5], 
[0, 2, 0, 0, 0, 0, 0, 5, 3, 0], 
[0, 0, 0, 0, 0, 0, 0, 0, 1, 3], 
[0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

G1 = [[0,4,0,3,0,0],
     [0,0,2,2,0,0],
     [0,0,0,0,0,4],
     [0,0,2,0,2,0],
     [0,0,0,0,0,5],
     [0,0,0,0,0,0]]

print(Edmonds_Karp(G1, 0, 5))