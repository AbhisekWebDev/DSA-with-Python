class Solution:

    def getHours(self, piles, mid) :

        ans = 0

        for pile in piles :

            ans += (pile + mid - 1) // mid # ceil value nikalne ka trika bina ceil function use kiye
        
        return ans



    def minEatingSpeed(self, piles, h: int) -> int:

        # isme binary search array pr nhi lgana h

        # binary search is k answer pr lgana h

        mn = 1 # left
        mx = max(piles) # right

        x = mx

        while mn <= mx :

            mid = (mn + mx) // 2

            # jb bhi numbers of hours zyada ho h se

            if self.getHours(piles, mid) > h :
                
                # right
                mn = mid + 1

            else :
                x = mid

                # hours aur kam ho skta h

                # left
                mx = mid - 1
        
        return x

piles = [3,6,7,11]
h = 8

sol = Solution()
print(sol.minEatingSpeed(piles, h))