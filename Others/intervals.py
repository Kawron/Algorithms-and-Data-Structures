def intersection(A, B):
    # spr który się wcześniej zaczyna
    if A[0] < B[0]:
        x1, x2 = A[0], A[1]
        y1, y2 = B[0], B[1]
    else:
        x1, x2 = B[0], B[1]
        y1, y2 = A[0], A[1]
    # czy wg sie przecinaja
    if x1 <= y2 and y1 <= x2:
        return max(x1,y1), min(x2,y2)
    else:
        return None

def sum_of_intervals(A, B):
    # spr który się wcześniej zaczyna
    if A[0] < B[0]:
        x1, x2 = A[0], A[1]
        y1, y2 = B[0], B[1]
    else:
        x1, x2 = B[0], B[1]
        y1, y2 = A[0], A[1]
    if intersection((x1,x2), (y1,y2)) != None:
        return min(x1,y1), max(x2, y2)
    else:
        return (x1,x2),(y1,y2)

print(intersection((2,3),(0,4)))
print(sum_of_intervals((2,3),(0,4)))

print(intersection((2,5),(3,8)))
print(sum_of_intervals((2,5),(3,8)))

print(intersection((3,8),(2,5)))
print(sum_of_intervals((3,8),(2,5)))

print(sum_of_intervals((0,3), (8,9)))