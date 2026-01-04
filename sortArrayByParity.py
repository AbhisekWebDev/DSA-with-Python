def sortArrayByParity(nums) :
    
    start = 0

    for i in range (len(nums)) :
        if nums[i] % 2 == 0 :
            temp = nums[i]
            nums[i] = nums[start]
            nums[start] = temp

            start += 1
        
    return nums

nums = [1,5,9,7,-8,3,4,6,2,8,0,-1,-5,-7]

print(sortArrayByParity(nums))

# Given an integer array nums, move all the even 
# integers at the beginning of the array followed 
# by all the odd integers.