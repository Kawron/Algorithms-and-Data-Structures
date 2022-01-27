class Node():
    def __init__(self, val):
        self.val = val
        self.rank = 0
        self.parent = self
    
    def __str__(self):
        return f'Node {self.val}'

def make_set(T):
    n = len(T)
    for i in range(n):
        T[i] = Node(T[i])
    return T

def find(x):
    if x != x.parent:
        x.parent = find(x.parent)
    return x.parent

def union(x,y):
    x = find(x)
    y = find(y)
    if x == y: return
    if x.rank > y.rank:
        y.parent = x
    else:
        x.parent = y
        if x.rank == y.rank: 
            y.rank += 1

# T = make_set([1,2,3,4,5,6])
# for rec in T:
#     print(rec)