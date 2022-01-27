# Zadanie 6 (ścieżka w drzewie) Dane jest drzewo ukorzenione T, gdzie każdy wierzchołek v ma—
# potencjalnie ujemną—wartość value(v). Proszę zaproponować algorytm, który znajduje wartość najbardziej
# wartościowej ścieżki w drzewie T.

# f(v) - najelpsza ścieżka zaczynająca sie w v i idąca w dół
# f(v) = max(0, v.value, f(left)+v.value, f(right)+v.value)

class Node():
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
        self.f = 0

v = Node(5)
u = Node(-2)
w = Node(3)
z = Node(10)

v.left = u
v.right = w
w.left = z

def f(v):
    if v == None:
        return (0,0)
    L, best_in_left = f(v.left)
    R, best_in_right = f(v.right)

    v.f = max(0, v.val, v.val+L, v.val+R)
    best_path = max(best_in_left, best_in_right, v.f)
    return (v.f, best_path)

print(f(v))