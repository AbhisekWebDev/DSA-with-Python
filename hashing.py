# Two Sum

def twoSum(nums, target):
    hashmap = {}   # value → index
    
    for index, value in enumerate(nums):
        need = target - value
        
        if need in hashmap:     # found pair
            return [hashmap[need], index]
        
        hashmap[value] = index  # store number
    
    return []

print(twoSum([2,7,11,15], 9))  # Output: [0, 1] (2 + 7 = 9)