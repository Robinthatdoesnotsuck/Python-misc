

def bubbleSort(array):
    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if array[j] > array[j+1]:
                array[j], array[j + 1] = array[j+1], array[j]

    return array


arr = [64, 34, 25, 12, 22, 11, 90]
print(bubbleSort(arr))