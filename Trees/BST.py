class Node():

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None

    def __str__(self):
        return f'{self.key}'

def find(root, key):
    while root != None and root.key != key:
        if key < root.key:
            root = root.left
        else:
            root = root.right
    return root

def next(root, key):
    node = find(root, key)
    if node.right != None:
        node = node.right
        return minimum(node)
    else:
        while node.parent != None:
            parent = node.parent
            if parent.right == node:
                node = parent
            elif parent.left == node:
                return parent
        return None

def prev(root, key):
    node = find(root, key)
    if node.left != None:
        node = node.left
        return maximum(node)
    else:
        while node.parent != None:
            parent = node.parent
            if parent.left == node:
                node = parent
            elif parent.right == node:
                return parent
        return None

def minimum(root):
    while root.left != None:
        root = root.left
    return root

def maximum(root):
    while root.right != None:
        root = root.right
    return root

def insert(root, key):
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
    return True

# MESS

from collections import deque
import math
def print_tree(root):
    
    def count_nodes(root):
        if root != None:
            return count_nodes(root.left) + count_nodes(root.right) + 1
        return 0

    multi = 2*3
    n = count_nodes(root)*multi
    curr_row = 0
    offset = n
    written = 0
    que = deque()
    que.append((root, curr_row))
    while curr_row < math.floor(math.log2(n)):#albo n razy row
        node, row = que.popleft()
        if node != None:
            que.append((node.left, row + 1))
            que.append((node.right, row + 1))
        else:
            que.append((None, row+1))
            que.append((None, row+1))
        if curr_row < row:
            curr_row = row
            offset = ((n-written) // 2**curr_row) # całe miejsce na jedna liczbe
            #offset -= 2**(curr_row-1)
            print()
        if node != None:
            print(str(node).center(offset), end="")
        else:
            print(" ".center(offset), end="")
        print(" ", end="")
        written += 1

def delete(root, key):
    node = find(root, key)
    if node == None:
        return False
    # brak dzieci
    if node.right == None and node.left == None:
        parent = node.parent
        if parent.left == node:
            parent.left = None
        else:
            parent.right = None
    # jedno dziecko
    elif node.right != None and node.left == None:
        parent = node.parent
        if node.parent == None:
            aux = node.right
            node.left = aux.left
            node.right = aux.right
            if aux.left != None:
                aux.left.parent = node
            if aux.right != None:
                aux.right.parent = node
            node.key, aux.key = aux.key, node.key
        elif parent.right == node:
            parent.right = node.right
            node.right.parnet = parent
        else:
            parent.left = node.right
            node.right.parnet = parent
    elif node.left != None and node.right == None:
        parent = node.parent
        if node.parent == None:
            aux = node.left
            node.left = aux.left
            node.right = aux.right
            if aux.left != None:
                aux.left.parent = node
            if aux.right != None:
                aux.right.parent = node
            node.key, aux.key = aux.key, node.key
        elif parent.right == node:
            parent.right = node.left
            node.left.parent = parent
        else:
            parent.left = node.left
            node.left.parent = parent
    else:
        aux = next(root, key)
        key = aux.key
        delete(root, key)
        node.key = key
    return True

root = Node(7)
insert(root, 8)
insert(root, 5)
insert(root, 4)
insert(root, 6)
insert(root, 9)
delete(root, 5)
print_tree(root)