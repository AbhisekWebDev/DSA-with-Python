from typing import Optional, List
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        h = []

        for i in nums :
            heapq.heappush(h, i)

            if len(h) > k :
                heapq.heappop(h)

        return h[0]
    
nums = [3,2,1,5,6,4]
k = 2
print(Solution().findKthLargest(nums, k))

nums = [3,2,3,1,2,4,5,5,6]
k = 4
print(Solution().findKthLargest(nums, k))