# znajdowanie mostów
# używamy funkcji low
# d(v) - czas odwiedzenia v w DFS
# u - taki wierzchołek że istnieje krawędz wsteczna
# z v do u
# w - dziecko v
# low(v) = min(d(v), min(d(u)), min(low(w)))
# most to krawędz {v, p(v)} gdzie low(v) = d(v)

# matrix
def bridge(G):
    
    def DFS_visit(G, u):
        nonlocal time

        d[u] = time
        time += 1
        visited[u] = True
        low[u] = d[u]
        for v in range(n):
            if visited[v] == False and G[u][v] == 1:
                parent[v] = u
                DFS_visit(G,v)
                low[u] = min(low[u], low[v])
            elif parent[u] != v and G[u][v] == 1:
                low[u] = min(low[v], d[v])


    n = len(G)
    visited = [False for _ in range(n)]
    parent = [-1 for _ in range(n)]
    d = [-1 for _ in range(n)]
    low = [float('inf') for _ in range(n)]
    time = 0
    for u in range(n):
        if visited[u] == False:
            DFS_visit(G,u)
    for v in range(n):
        if low[v] == d[v]:
            print(v, parent[v])

G = [[0, 1, 0, 1, 0, 0, 0],
[1, 0, 1, 0, 0, 0, 0],
[0, 1, 0, 1, 1, 0, 0],
[1, 0, 1, 0, 0, 0, 0],
[0, 0, 1, 0, 0, 1, 1],
[0, 0, 0, 0, 1, 0, 1],
[0, 0, 0, 0, 1, 1, 0]]
bridge(G)