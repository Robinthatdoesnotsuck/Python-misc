

def selectionSort(array):
    for i in range(len(array)):
        min_idx = i
        for j in range(i+1, len(array)):
            if array[min_idx] > array[j]:
                min_idx = j
        
        array[i], array[min_idx] = array[min_idx], array[i]
    
    return array

array = [1, 4, 2, 8, 345, 123, 43, 32, 5643, 63, 123, 43, 2, 55, 1, 234, 92]

print(selectionSort(array))