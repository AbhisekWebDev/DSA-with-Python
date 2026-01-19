class Solution:
    def nextGreaterElement(self, nums1, nums2) :

         # length of nums2
        n = len(nums2)

        # dictionary to store:
        # key   -> element from nums2
        # value -> next greater element of that key
        ans = {}

        # stack to maintain a decreasing sequence (monotonic decreasing stack)
        st = []

        # Traverse nums2 from right to left
        for i in range(n - 1, -1, -1) :

            # remove all elements from stack
            # that are smaller than or equal to nums2[i]
            # because they can never be the next greater element
            while len(st) > 0 and st[-1] <= nums2[i] :
                st.pop()

            # if stack is empty,
            # no greater element exists to the right
            if len(st) == 0 :
                ans[nums2[i]] = -1
            else :
               
                # top of stack is the next greater element
                ans[nums2[i]] = st[-1]
            
            # push current element onto stack
            # for elements on the left
            st.append(nums2[i])

        # result list for nums1
        res = []

        # for each element in nums1,
        # fetch its next greater element from dictionary
        for i in nums1 :
            res.append(ans[i])
        
        return res

sol = Solution()

# Test Case 1
nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]
print(sol.nextGreaterElement(nums1, nums2))
# Expected: [-1, 3, -1]

# Test Case 2
nums1 = [2, 4]
nums2 = [1, 2, 3, 4]
print(sol.nextGreaterElement(nums1, nums2))
# Expected: [3, -1]

# Test Case 3
nums1 = [1, 3, 5, 2, 4]
nums2 = [6, 5, 4, 3, 2, 1, 7]
print(sol.nextGreaterElement(nums1, nums2))
# Expected: [7, 7, 7, 7, 7]

# Test Case 4 (Single element)
nums1 = [1]
nums2 = [1]
print(sol.nextGreaterElement(nums1, nums2))
# Expected: [-1]

# Test Case 5 (Already decreasing)
nums1 = [3, 2, 1]
nums2 = [3, 2, 1]
print(sol.nextGreaterElement(nums1, nums2))
# Expected: [-1, -1, -1]
