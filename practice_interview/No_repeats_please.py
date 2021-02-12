import re
abecedario = ['a','b','c','d','e']
result = []
strEval = "abfdefa"
def permute(data, i, length):  
    if i == length:  
        result.append(''.join(data) )
        
    else:  
        for j in range(i, length):  
            # swap 
            data[i], data[j] = data[j], data[i]  
            
            permute(data, i + 1, length)  
            data[i], data[j] = data[j], data[i] 
            
count = 0
counter = []
permute(list(strEval), 0, len(strEval)) 
for permute in result:
    x = re.search(r"(.)\1+", permute)
    if x:
        count += 1

print(len(result) - count)

print("Resultant permutations", str(len(result))) 