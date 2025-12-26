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


# Used in:

# Two Sum

# 4Sum

# Subarray Sum Equals K

# Pair Sum

# Count Distinct Elements in Window

# Longest Subarray with Sum K

# Group Anagrams

# Find Duplicate in Array

# Intersection of Two Arrays

# Happy Number

# Contains Duplicate

# Top K Frequent Elements

# Subarray Sums Divisible by K