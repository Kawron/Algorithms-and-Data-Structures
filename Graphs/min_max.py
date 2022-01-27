# Zadanie 5. (problem przewodnika turystycznego) Przewodnik chce przewieźć grupę K turystów z
# miasta A do miasta B. Po drodze jest jednak wiele innych miast i między różnymi miastami jeżdzą autobusy o
# różnej pojemności. Mamy daną listę trójek postaci (x, y, c), gdzie x i y to miasta między którymi bezpośrednio
# jeździ autobus o pojemności c pasażerów.
# Przewodnik musi wyznaczyć wspólną trasę dla wszystkich tursytów i musi ich podzielić na grupki tak,
# żeby każda grupka mogła przebyć trasę bez rodzielania się. Proszę podać algorytm, który oblicza na ile
# (najmniej) grupek przewodnik musi podzielić turystów (i jaką trasą powinni się poruszać), źeby wszyscy
# dostali się z A do B.

# algorytm znajdowania wąskiego gardła, czyli dolnego ograniczenia na ilość "danych?" jakie możemy
# przesłać jedną ścieżką

# Algorytm
# -tworzymy graf
# -robimy posrtowana liste unikalnych wartości pojemności
# -odpalamy BFS z dodatkowym warunkiem bedącym środkowym ograniczeniem z naszej listy
# -w zależności czy udało nam się dotrzeć z s do t ograniczamy się tylko do górnej lub dolnej
#  połowy naszej listy
# -powtarzamy aż nie znajdziemy naszego wąskiego gardła

# Złożoność O(logE * (V+E)+ElogE) (btw warto pamiętać że E to co najwyżej V^2
# a więc O(logE) = O(logV))

# zakładam implementacje Adj list

# 1. zamienić input na graf
# 2. zrobić unikalną posortowaną liste wag
# 3. odpalić "binary searcha"
# 4. wypisać odpowiedź

# drugi sposób Kruskal 
# find union po malejących krawędziach

from collections import deque


def min_max(s, t, lista):

    def BFS(G,s,t,value):
        n = len(G)
        deq = deque()
        parent = [None]*n
        visited = [False]*n
        
        visited[s] = True
        deq.append(s)

        while len(deq) != 0:
            u = deq.popleft()
            for v in G[u]:
                v, capacity = v[0], v[1]
                if visited[v] == False and capacity >= value:
                    parent[v] = u
                    visited[v] = True
                    deq.append(v)
            visited[u] = True
        if visited[t] == True:
            return True, parent
        return False, parent

    def make_graph(lista):
        # znajdowanie liczby wierzchołków
        # zakładam że wierzchołki są numerowane od zera
        maxi = -1
        for triple in lista:
            maxi = max(maxi, triple[1])
        # inicjalizowanie grafu
        G = [[] for _ in range(maxi+1)]
        for triple in lista:
            G[triple[0]].append([triple[1], triple[2]])
        # graf G ma postać listy adj z wagami
        return G

    def make_uniq_list(lista):
        lista.sort(key = lambda x: x[2])
        tmp = [lista[0][2]]
        p = 1
        q = 0
        while p < len(lista):
            if lista[p][2] != tmp[q]:
                tmp.append(lista[p][2])
                p += 1
                q += 1
            else:
                p += 1
        return tmp

    def get_path(parent, v):
        if parent[v] == None:
            return res
        get_path(parent, parent[v])
        res.append(parent[v])
        return res

    uniq = make_uniq_list(lista)
    G = make_graph(lista)
    i = 0
    j = len(uniq)-1
    bottleneck = float('-inf')
    while i < j:
        q = uniq[(j-i)//2]
        flag, parent = BFS(G,s,t,q)[0], BFS(G,s,t,q)[1]
        if flag == True:
            bottleneck = min(bottleneck, q)
            i = q+1
        else:
            j = q
    res = []
    get_path(parent, t)
    res.append(t)
    return res

G = [[(1, 4), (2, 3)],  # 0
     [(3, 2)],  # 1
     [(3, 5)],  # 2
     []]  # 3
lista = [[0,1,4],[0,2,3],[1,3,2],[2,3,5]]
s = 0
t = 3
C = 3

print(min_max(s,t,lista))