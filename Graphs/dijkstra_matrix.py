# Dijsktra na macierzy

def find_min(G, visited, dist):
    n = len(G)
    idx = -1
    mini = float('inf')

    for i in range(n):
        if dist[i] < mini and visited[i] == False:
            mini = dist[i]
            idx = i
    
    return idx

def dijkstra_matrix(G, s):
    n = len(G)
    visited = [False]*n
    parent = [None]*n
    dist = [float('inf')]*n
    
    dist[s] = 0
    for _ in range(n):
        u = find_min(G, visited, dist)
        
        # warunek końca
        if dist[u] == float('inf'):
            return dist, parent

        # relaksacja
        for v in range(n):
            if G[u][v] != 0 and visited[v] == False:
                if dist[v] > dist[u] + G[u][v]:
                    dist[v] = dist[u] + G[u][v]
                    parent[v] = u
        visited[u] = True

    return dist, parent

def print_path(s, t, parent):
    if t == s:
        print(t, end=" ")
        return
    print_path(s, parent[t], parent)
    print(t, end=" ")

G = [[0,1,5,0,0],
    [1,0,2,8,7],
    [5,2,0,3,0],
    [0,8,3,0,1],
    [0,7,0,1,0]]
dis, parent = dijkstra_matrix(G, 3)
print(parent)
print(dis)
print_path(3, 1, parent)