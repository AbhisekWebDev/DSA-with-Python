# lower bound - 
# gives index of the first element that is greater than the given target

class Solution:

    def lowerBound(self, nums, target) :
        
        n = len(nums)
        l = 0
        r = n - 1
        ans = n

        while l <= r :
            mid = (l + r) // 2

            if nums[mid] > target :
                ans = mid

                # piche bhi check kro
                r = mid - 1

            else :
                # right
                l = mid + 1
    
        return ans


    def searchInsert(self, nums, target: int) -> int:
        
        return self.lowerBound(nums, target)

nums = [1,3,5,6]
target = 5

nums1 = [1,3,5,6]
target1 = 2

nums2 = [1,3,5,6]
target2 = 7

sol = Solution()
ans = sol.searchInsert(nums, target)
ans1 = sol.searchInsert(nums1, target1)
ans2 = sol.searchInsert(nums2, target2)
print(ans)
print(ans1)
print(ans2)