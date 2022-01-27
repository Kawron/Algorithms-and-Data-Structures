# Zadanie 4. (klocki) Dany jest ciąg klocków (K1, . . . , Kn). Klocek Ki zaczyna sie na pozycji ai
# i ciągnie
# się do pozycji bi (wszystkie pozycje to nieujemne liczby naturalne) oraz ma wysokość 1. Klocki układane są po
# kolei–jeśli klocek nachodzi na któryś z poprzednich, to jest przymocowywany na szczycie poprzedzającego
# klocka). Na przykład dla klocków o pozycjach (1, 3), (2, 5), (0, 3), (8, 9), (4, 6) powstaje konstrukcja o
# wysokości trzech klocków. Proszę podać możliwie jak najszybszy algorytm, który oblicza wysokośc powstałej
# konstrukcji.

# tworzymy drzewo przedziałowe. Na każdym przedziale trzymamy informacje który klocek jako ostatni zupdatowalismy.
# I dla każdego klocka trzymamy jego wyskość w osobnej tablicy

# pierwsze - budowanie drzewa BST

class Node():

    def __init__(self, key):
        self.key = key
        self.leaf = False
        self.span = None
        self.parent = None
        self.left = None
        self.right = None
        self.last = None

    def __str__(self):
        return f"{self.key}"

def points_array(array):
    tmp = []
    for interval in array:
        tmp.append(interval[0])
        tmp.append(interval[1])
    array = tmp
    # sortowanie i unikalnosc
    
    array.sort()
    tmp = [array[0]]
    i = 0
    j = 0
    while i < len(array):
        if array[i] != array[j]:
            tmp.append(array[i])
            i += 1
            j += 1
        else:
            i += 1

    array = tmp
    return array

def make_BST(points):

    def insert(root, key, leaf = False):
        aux = None
        while root != None:
            aux = root
            if root.key == key:
                return False
            elif key < root.key:
                root = root.left
            else:
                root = root.right
        node = Node(key)
        if key < aux.key:
            aux.left = node
        else:
            aux.right = node
        node.parent = aux
        # dodawanie spanu
        if node == node.parent.left:
            node.span = [node.parent.span[0], node.parent.key]
        else:
            node.span = [ node.parent.key, node.parent.span[1]]
        return True

    def insert_leafs(root):
        if root.left == None:
            root.left = Node(None)
            root.left.leaf = True
            root.left.span = [root.span[0], root.key]
        else:
            insert_leafs(root.left)
        if root.right == None:
            root.right = Node(None)
            root.right.leaf = True
            root.right.span = [root.key, root.span[1]]
        else:
            insert_leafs(root.right)
        
    def recurr(root, points, i, j):
        key = (j+i)//2
        if i <= j:
            insert(root, points[key])
            recurr(root, points, i, key-1)
            recurr(root, points, key+1, j)
    
    n = len(points)
    i = 0
    j = n-1
    q = (j+i)//2
    root = Node(points[q])
    root.span = [float("-inf"),float("inf")]
    
    recurr(root, points, i, q-1)
    recurr(root, points, q+1, j)
    
    insert_leafs(root)
    return root

def intersect(interval1, interval2):
    # zakładamy że x1 <= x2 and y1 <= y2
    x1, x2 = interval1[0], interval1[1]
    y1, y2 = interval2[0], interval2[1]
    return x1 <= y2 and y1 <= x2

def contains(interval1, interval2):
    # chcemy by interval1 zawieral się
    # w interval 2 dlatego taki return
    x1, x2 = interval1[0], interval1[1]
    y1, y2 = interval2[0], interval2[1]
    return (y1 <= x1 and y2 >= x2)

def inserting_block(node, idx):
    if contains(node.span, array[idx]):
        if node.last != None and heights[node.last] + 1 > heights[idx]:
            heights[idx] = heights[node.last] + 1
        return
    
    if intersect(node.span, array[idx]):
        node.last = idx
    
    # ide na boki
    if node.left != None and intersect(node.left.span, array[idx]):
        inserting_block(node.left, idx)
    if node.right != None and intersect(node.right.span, array[idx]):
        inserting_block(node.right, idx)

def main(array):
    points = points_array(array)
    root = make_BST(points)
    
    # wyskość każdego klocka
    global heights
    heights = [1 for _ in range(len(array))]

    for idx in range(len(array)):
        inserting_block(root, idx)

    maxi = -1
    for i in range(len(heights)):
        maxi = max(maxi, heights[i])
    print(maxi)

#array = [[1,3],[2,5],[0,3],[8,9],[4,6]]
array = [[1,2],[3,5],[4,8],[2,4],[0,2],[7,10],[5,8],[4,6]]
main(array)