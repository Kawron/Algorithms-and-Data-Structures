# Dijkstra na adj list

# apropo PriorityQueue użycie que.queue[0] zwraca
# pierwszy element z kolejki
from queue import PriorityQueue

def dijkstra(G, s):
    n = len(G)
    visited = [False]*n
    parent = [None]*n
    dist = [float('inf')]*n
    que = PriorityQueue()
    
    dist[s] = 0
    que.put((dist[s],s))
    for _ in range(n):
        u = que.get()[1]

        # warunek stopu
        if dist[u] == float('inf'):
            return dist, parent
        
        # relaksacja
        for v in G[u]:
            v, w = v[0], v[1]
            if dist[v] > dist[u] + w and visited[v] == False:
                dist[v] = dist[u] + w
                parent[v] = u
                que.put((dist[v], v))
        visited[u] = True
        
    return dist, parent

def print_path(s, t, parent):
    if t == s:
        print(t, end=" ")
        return
    print_path(s, parent[t], parent)
    print(t, end=" ")

G = [[(1,1),(2,5)],
     [(0,1),(2,2),(3,8),(4,7)],
     [(0,5),(1,2),(3,3)],
     [(1,8),(2,3),(4,1)],
     [(1,7),(3,1)]]
    
dist, parent = dijkstra(G,3)
print_path(3,4, parent)
print()
print(dist)
print(parent)