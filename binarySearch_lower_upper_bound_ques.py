class Solution:

    def lowerBound(self, nums, target) :
        
        n = len(nums)
        l = 0
        r = n - 1
        ans = n

        while l <= r :
            mid = (l + r) // 2

            if nums[mid] >= target :
                ans = mid

                # piche bhi check kro
                r = mid - 1

            else :
                # right
                l = mid + 1
    
        return ans

    def upperBound(self, nums, target) :
        
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

    def searchRange(self, nums, target: int) :

        lb = self.lowerBound(nums, target)
        ub = self.upperBound(nums, target)

        if lb == ub :
            
            # element is not present
            return[-1, -1]

        else :
            return [lb, ub - 1]


nums = [5,7,7,8,8,10]
target = 8

nums1 = [5,7,7,8,8,10]
target1 = 6

sol = Solution()
ans = sol.searchRange(nums, target)
ans1 = sol.searchRange(nums1, target1)
print(ans)
print(ans1)