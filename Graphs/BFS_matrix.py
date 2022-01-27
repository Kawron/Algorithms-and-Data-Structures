from collections import deque

#matrix

def BFS(G,s):
    n = len(G)
    deq = deque()
    dist = [-1]*n
    parent = [None]*n
    visited = [False]*n
    dist[s] = 0
    visited[s] = True
    deq.append(s)
    while len(deq) != 0:
        u = deq.popleft()
        for v in range(n):
            if visited[v] == False and G[u][v] != 0:
                dist[v] = dist[u] + 1
                parent[v] = u
                visited[v] = True
                deq.append(v)
        visited[u] = True
    return parent, dist, visited

def print_path(G,parent,s,v):
    if s == v:
        print(s)
    elif parent[v] == None:
        print("Path does not exist")
    else:
        print_path(G,parent,s,parent[v])
        print(v)

G = [[2, 4, 5], [4, 5], [0, 3, 4], [2], [0, 1, 2, 5], [0, 1, 4]]
x,y,z = BFS(G, 3)
print(x)