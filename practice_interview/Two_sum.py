nums = [3,2,4]
target = 6 
output = []


for i in range(0, len(nums)):
    for j in range(0, len(nums)):
        val = target - nums[i]
        if i != j:
            if val == nums[j]:
                if len(output) != 2:
                    output.append(i)
                    output.append(j)
print(output)
