# ajd list
# można jescze dodać czasy
def DFS(G):

    def DFS_visit(G,u):
        visited[u] = True
        for v in G[u]:
            if visited[v] == False:
                parent[v] = u
                DFS_visit(G,v)

    n = len(G)
    visited = [False]*n
    parent = [None]*n
    for u in range(n):
        if visited[u] == False:
            DFS_visit(G, u)
    return visited, parent


G = [[2, 4, 5], [4, 5], [0, 3, 4], [2], [0, 1, 2, 5], [0, 1, 4]]
x,y = DFS(G)
print(x)
print(y)