# implementacja matrixowa V^3 krawędziowa ma V*E
def Bellman_Ford(G, s):
    n = len(G)
    dis = [float('inf')]*n
    parent = [None]*n
    dis[s] = 0
    # relaksacje
    for _ in range(n-1):
        for u in range(n):
            for v in range(n):
                if G[u][v] != 0:
                    if dis[v] > dis[u] + G[u][v]:
                        dis[v] = dis[u] + G[u][v]
                        parent[v] = u
    # verification
    for u in range(n):
        for v in range(n):
            if G[u][v] != 0:
                if dis[v] <= dis[u] + G[u][v]: pass
                else: return None
    return dis, parent

G = [[0,1,5,0,0],
    [1,0,2,8,7],
    [5,2,0,3,0],
    [0,8,3,0,1],
    [0,7,0,1,0]]
dis, parents = Bellman_Ford(G, 3)
print(parents)