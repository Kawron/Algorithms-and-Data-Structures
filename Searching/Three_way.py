# program tak ustawia array że na początku występują wartości mniejsze od value
# potem równe value a na koniec większe od value

# złożoność O(n)

def three_way(arr, value):
    i = 0
    j = 0
    k = len(arr)-1
    while j < k:
        if arr[j] < value:
            arr[j], arr[i] = arr[i], arr[j]
            i += 1
            j += 1
        elif arr[j] > value:
            arr[j], arr[k] = arr[k], arr[j]
            k -= 1
        else:
            j += 1

arr = [9,8,7,6,5,4,5,3,5,2,5,1]
print(arr)
three_way(arr, 5)
print(arr)