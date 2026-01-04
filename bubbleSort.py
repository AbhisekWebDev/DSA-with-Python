def bubbleSort(nums) :
    
    for i in range (len (nums)) :

            isSwap = False

            for j in range (len (nums) - i - 1) :
                
                if nums[j] > nums[j + 1] :
                   
                    # swap
                    temp = nums[j] 
                    nums[j] = nums[j + 1] 
                    nums[j + 1] = temp

                    isSwap = True
            
            if not isSwap :
                break
        
    return nums

nums = [1,5,9,7,3,4,6,2,8,0]

print(bubbleSort(nums))

# space complexity = O(1)
# time complexity = 
#     worst = O(n^2)
#     best = O(n)