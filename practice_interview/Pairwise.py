

pair = [1,4,2,3,0,5]
target = 7
def pairwise(array, number):
    vecResult = []
    for i in range(len(array)):
        for j in range(len(array)):
            val = target - array[i]
            if val == array[j] and not j in vecResult and not i in vecResult and not j == i:
                vecResult.append(i)
                vecResult.append(j)
    result = 0
    print(vecResult)
    for i in vecResult:
        result += i
    return result


print(pairwise(pair,target))