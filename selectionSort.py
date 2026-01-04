class Solution:
    def sortArray(self, nums) :
        
        # selection sort
        for i in range (len(nums) - 1) :
            
            #  Assume the current position holds the minimum element
            min_num = i
            
            
            # Iterate through the unsorted portion to find the actual minimum
            for j in range (i + 1, len(nums)) :

                if nums[j] < nums[min_num] :
                    
                    min_num = j

            # swap
            temp = nums[i]
            nums[i] = nums[min_num]
            nums[min_num] = temp

        return nums

nums = [5,2,3,1]   

sol = Solution()
ans = sol.sortArray(nums)
print(ans)


# space complexity = O(1)
# time complexity = 
#     worst = O(n^2)
#     best = O(n^2)