def removeDuplicates(nums) -> int:

    if len(nums) <= 2 :
        
        return len(nums)

    start = 1

    for i in range (2, len(nums)) :
            
        # unique elements
        if nums[i] != nums[start - 1] :
            start += 1
            nums[start] = nums[i]
        
    return start + 1

nums = [1,1,1,2,2,3]

k = removeDuplicates(nums)

print(k, nums[:k])


# Given an integer array nums sorted in non-decreasing order, 
# remove some duplicates in-place such that each unique element 
# appears at most twice. T
# he relative order of the elements should be kept the same.

# Since it is impossible to change the length of the array in 
# some languages, you must instead have the result be placed in 
# the first part of the array nums. More formally, if there are 
# k elements after removing the duplicates, then the first k 
# elements of nums should hold the final result. It does not 
# matter what you leave beyond the first k elements.

# Return k after placing the final result in the first k slots 
# of nums.

# Do not allocate extra space for another array. You must do 
# this by modifying the input array in-place with O(1) extra 
# memory.