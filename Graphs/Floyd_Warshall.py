def floyd_warshall(G):
    n = len(G)
    dist = [[float('inf') for _ in range(n)] for _ in range(n)]
    parent = [[None for _ in range(n)] for _ in range(n)]
    
    for u in range(n):
        dist[u][u] = 0
    
    for u in range(n):
        for v in range(n):
            if G[u][v] != 0:
                dist[u][v] = G[u][v]
                parent[u][v] = u
    
    for t in range(n):
        for u in range(n):
            for v in range(n):
                if dist[u][v] > dist[u][t] + dist[t][v]:
                    dist[u][v] = dist[u][t] + dist[t][v]
                    parent[u][v] = parent[t][v]
    return dist, parent

G = [[0,1,5,0,0],
    [1,0,2,8,7],
    [5,2,0,3,0],
    [0,8,3,0,1],
    [0,7,0,1,0]]