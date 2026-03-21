from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []
    
    # alternative solution using two pointers
    def twoSumTwoPointers(self, nums: List[int], target: int) -> List[int]:

        # Note: This logic only works if 'nums' is sorted. 
        # If it's not, you'd need: nums.sort()

        nums_with_indices = list(enumerate(nums))
        nums_with_indices.sort(key=lambda x: x[1])  # Sort by the number value
        
        left, right = 0, len(nums) - 1
        
        while left < right:
            current_sum = nums_with_indices[left][1] + nums_with_indices[right][1]
            if current_sum == target:
                return [nums_with_indices[left][0], nums_with_indices[right][0]]
            elif current_sum < target:
                left += 1
            else:
                right -= 1
        
        return []