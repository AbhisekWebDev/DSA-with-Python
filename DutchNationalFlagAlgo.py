# “Dutch National Flag” is the classic algorithm behind LeetCode Problem 75 – Sort Colors.

# 📌 LeetCode Details

# Problem Name: Sort Colors

# Problem Number: 75

# Concept: Dutch National Flag Algorithm

# Tags: Array, Two Pointers, Sorting

# The problem statement is literally designed from Edsger Dijkstra’s Dutch National Flag problem, where:

# 0 represents Red

# 1 represents White

# 2 represents Blue

# Why It's Called Dutch National Flag?

# Because the algorithm partitions the array into 3 regions:

# < pivot → left region (0s)

# == pivot → middle region (1s)

# > pivot → right region (2s)

# Exactly like 3 stripes of a flag.

class Solution:
    def sortColors(self, nums) :
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # two pointer approach
        left = 0
        right = len(nums) - 1

        i = 0

        while i <= right :

            # 0 ko left me bhejna h, 1 ko mid me rkhna h & 2 ko right me rkhna h
            if nums[i] == 1 :
                i += 1
            elif nums[i] == 0 :
                # swap the elements to left
                temp = nums[i]
                nums[i] = nums[left]
                nums[left] = temp

                i += 1
                left += 1
            elif nums[i] == 2 :
                # swap the elements to right
                temp = nums[i]
                nums[i] = nums[right]
                nums[right] = temp

                # i++ nhi, bas right++
                # jab bhi right se swap hoga i++ nhi hoga
                right -= 1

        return nums
    
nums = [2,0,2,1,1,0]   

sol = Solution()
ans = sol.sortColors(nums)
print(ans)

# it uses two pointers and sorting