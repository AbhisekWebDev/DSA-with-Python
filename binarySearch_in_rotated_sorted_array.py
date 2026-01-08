class Solution:
    def search(self, nums, target: int) -> int:

        n = len(nums)
        l = 0
        r = n - 1

        while l <= r :
            
            mid = (l + r) // 2

            if nums[mid] == target :
                return mid
            
            # LEFT part is sorted
            if nums[l] <= nums[mid]:
                
                if nums[l] <= target and target < nums[mid] :
                     r = mid - 1
                
                else:
                    l = mid + 1
            
            # RIGHT part is sorted
            else:
                if nums[mid] < target and target <= nums[r]:
                    l = mid + 1
                
                else:
                    r = mid - 1
    
        return -1

nums = [4,5,6,7,0,1,2]
target = 0

sol = Solution()
print(sol.search(nums, target))