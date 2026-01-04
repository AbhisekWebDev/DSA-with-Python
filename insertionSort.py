class Solution:
    def sortArray(self, nums) :
        
        # insertion sort
        for i in range (1, len (nums)) :

            key = nums[i]

            j = i - 1

            while j >= 0 and nums[j] > key :

                nums[j + 1] = nums[j]

                j -= 1

                nums[j + 1] = key
        
        return nums

nums = [5,2,3,1]   

sol = Solution()
ans = sol.sortArray(nums)
print(ans)

# space complexity = O(1)
# time complexity = 
#     worst = O(n^2)
#     best = O(n)