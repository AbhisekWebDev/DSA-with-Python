# Question:
# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
# Merge nums1 and nums2 into a single array sorted in non-decreasing order.
# The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n

class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        i = m - 1
        j = n - 1
        k = (m + n) - 1

        while j >= 0 :
            
            if i < 0 or nums2[j] > nums1[i] :
                nums1[k] = nums2[j]

                k -= 1
                j -= 1
            
            else :
                nums1[k] = nums1[i]

                k -= 1
                i -= 1

nums1 = [1,2,3,0,0,0]   
m = 3
nums2 = [2,5,6]
n = 3

sol = Solution()
sol.merge(nums1, m, nums2, n)
print(nums1)



# Core Idea

# Instead of merging from the front (which shifts elements & is messy),
# we merge from the backwards because:

# Largest elements should go at end

# nums1 already has empty slots at end

# So we fill from last index k

# This avoids overwriting useful values.



# i → last valid element in nums1  (m−1)
# j → last element of nums2        (n−1)
# k → last index in nums1          (m+n−1)

# nums1 = [1,2,3,0,0,0]
#            i       k
# nums2 = [2,5,6]
#            j



# We only loop until nums2 finishes, because:

# Elements in nums1 are already sorted

# If nums2 is done, nums1 is already correct



# if i < 0 or nums2[j] > nums1[i]:
#     nums1[k] = nums2[j]
#     j -= 1
#     k -= 1

# Meaning:
# If nums1 is exhausted (i < 0)
# OR nums2’s element is bigger
# Place nums2[j] at nums1[k]



# else:
#     nums1[k] = nums1[i]
#     i -= 1
#     k -= 1

# Meaning:
# nums1[i] is greater or equal
# Place nums1[i] at nums1[k]



# Uses O(1) extra space

# Works in O(m+n) time

# Avoids overriding important data