import find_union as fu
# zakładamy że dostajemy Graf w formie list krawędzi (u,v,w) i list wierzchołków

def Kruskal(E, V):
    A = []
    V = fu.make_set(V)
    E = sorted(E, key=lambda x:x[2])
    for edge in E:
        if fu.find(V[edge[0]]) != fu.find(V[edge[1]]):
            A.append(edge)
            fu.union(V[edge[0]], V[edge[1]])
    return A

E = [(0,1,2),(1,0,2),(1,5,6),(5,1,6),(1,3,5),(3,1,5),(5,4,1),(4,5,1),(0,5,7),(5,0,7),(5,2,8),(2,5,8),(1,2,3),(2,1,3),(5,3,2),(3,5,2),(4,3,1),(3,4,1)]
#E = [(0,1,2),(1,5,6),(1,3,5),(5,4,1),(0,5,7),(5,2,8)]
V = [0,1,2,3,4,5]
print(Kruskal(E,V))