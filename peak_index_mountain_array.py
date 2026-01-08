class Solution:
    def peakIndexInMountainArray(self, arr) -> int:

        n = len(arr)
        l = 0
        r = n - 2

        ans = n - 1

        while l <= r :
            
            mid = (l + r) // 2

            if arr[mid] < arr[mid + 1] :

                # right
                l = mid + 1
            
            else :

                ans = mid

                # agr elementagle wale se bada h, to wo decreasing slope me h
                # tab ye pata hoga k peak element us element k left me h

                # left
                r = mid - 1
    
        return ans

arr = [0,1,0]

sol = Solution()
print(sol.peakIndexInMountainArray(arr))