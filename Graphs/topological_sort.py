# adjlist

def topo_sort(G):

    def DFS_visit(G,u):
        visited[u] = True
        for v in G[u]:
            if visited[v] == False:
                DFS_visit(G,v)
        sort_vertices.append(u)

    sort_vertices = []
    visited = [False]*len(G)
    for u in range(len(G)):
        if visited[u] == False:
            DFS_visit(G, u)
    sort_vertices.reverse()
    return sort_vertices

G = [[1],[],[0,3],[0,1]]
print(topo_sort(G))