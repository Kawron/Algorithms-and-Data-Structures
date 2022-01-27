# znajdowanie silnych spójnych składowych
# matrix

# zamiast tranpsozycji mozna zrobić bfs gdzie sprawdzamy G[v][u]
def SCC(G):

    def DFS_visit(G, u, flag):
        nonlocal time
        n = len(G)
        visited[u] = True
        for v in range(n):
            if visited[v] == False and G[u][v] == 1:
                DFS_visit(G, v, flag)
        times[u] = [time, u]
        time += 1
        if flag == True:
            components[idx].append(u)
    
    # first DFS
    n = len(G)
    time = 0
    times = [[-1, -1] for _ in range(n)]
    visited = [False for _ in range(n)]
    for u in range(n):
        if visited[u] == False:
            DFS_visit(G, u, False)
    # Transposition
    M = [[G[i][j] for i in range(n)] for j in range(n)]
    # second DFS
    time = 0
    times.sort(key=lambda x:x[0], reverse=True)
    visited = [False for _ in range(n)]
    components = []
    idx = 0
    for pair in times:
        u = pair[1]
        if visited[u] == False:
            components.append([])
            DFS_visit(M,u,True)
            idx += 1
    return components

G = [[0, 1, 0, 0, 0, 0, 0, 0],
[0, 0, 1, 1, 0, 0, 0, 0],
[1, 0, 0, 0, 0, 1, 0, 0],
[0, 0, 0, 0, 1, 0, 1, 0],
[0, 0, 0, 1, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 0, 1, 0],
[0, 0, 0, 0, 0, 1, 0, 1],
[0, 0, 0, 0, 0, 0, 0, 1]]

print(SCC(G))