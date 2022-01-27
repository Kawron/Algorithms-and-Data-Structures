# używamy zmodyfikowanego DFS
# przechodzimy DFS na bieżąco usuwając krawędzie po których prześliśmy
# DFS nie ma pola visited, usuwane krawędzie zapewniają nam, że nie 
# zapętlimy się
# gdy przetworzymy wierzchołek, tzn nie mamy gdzie iść
# to dopisujemy go na początek naszego cyklu

# reprezentacja macierzowa
from collections import deque

def does_cycle_exit(G):
    n = len(G)
    num_of_2st = []
    for v in range(n):
        cnt = 0
        for u in range(n):
            if u != v and G[v][u]:
                cnt += 1
        if cnt == 2:
            num_of_2st.append(v)
        elif cnt % 2 != 0:
            return None
    if len(num_of_2st) != 2:
        return None
    elif len(num_of_2st) == 2:
        return num_of_2st[0]
    return 0

def euler_cycle(G):
    
    def DSF_visit(G,u):
        for v in range(n):
            if G[u][v] > 0:
                G[u][v] *= -1
                G[v][u] *= -1
                DSF_visit(G,v)
        cycle.appendleft(u)
    
    s = does_cycle_exit(G)
    if s == None:
        return None
    n = len(G)
    cycle = deque()
    DSF_visit(G, s)
    return cycle

# G = [[0, 1, 0, 1, 0, 0],
# [1, 0, 1, 1, 1, 0],
# [0, 1, 0, 1, 1, 1],
# [1, 1, 1, 0, 1, 0],
# [0, 1, 1, 1, 0, 1],
# [0, 0, 1, 0, 1, 0]]
G = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
[0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
[0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
[0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
print(euler_cycle(G))