from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:

        l = 0
        r = len(height) - 1

        l_max = 0
        r_max = 0

        res = 0

        while l < r :
            
            if height[l] < height[r] :

                # process left side
                if height[l] >= l_max:
                    l_max = height[l] # update max seen from left
                
                else:
                    res += l_max - height[l] # trap water!
                
                l += 1
            
            else:
                # process the right
                if height[r] >= r_max:
                    r_max = height[r] # update max seen from right
                else:
                    res += r_max - height[r] # trap water!
                r -= 1

        return res



        