class Solution:
    def nextGreaterElements(self, nums) :

        # Duplicate the array to simulate circular behavior
        # Example: [1,2,3] → [1,2,3,1,2,3]
        nums += nums

        # Total length after duplication
        n = len(nums)

        # Initialize answer array of size n with 0s
        # This will store next greater elements
        ans = [0] * n

        # Stack to maintain a monotonic decreasing sequence
        # It stores potential next greater elements
        st = []

        # Traverse from right to left
        for i in range(n - 1, -1, -1) :

            # Remove all elements from stack that are
            # smaller than or equal to current element
            # because they cannot be the next greater element
            while len(st) > 0 and st[-1] <= nums[i] :
                st.pop()

            # If stack is empty, no greater element exists
            if len(st) == 0 :
                ans[i] = -1

            else :
                
                # Top of stack is the next greater element
                ans[i] = st[-1]
            
            # Push current element into stack
            # for elements on the left
            st.append(nums[i])

        # Return only the result for the original array length
        # (ignore duplicated part)
        return ans[:len(ans) // 2]

def run_tests():
    sol = Solution()

    test_cases = [
        ([1, 2, 1], [2, -1, 2]),
        ([3, 8, 4, 1, 2], [8, -1, 8, 2, 3]),
        ([1, 2, 3, 4, 3], [2, 3, 4, -1, 4]),
        ([5, 4, 3, 2, 1], [-1, 5, 5, 5, 5]),
        ([2, 2, 2], [-1, -1, -1]),
        ([1], [-1])
    ]

    for i, (nums, expected) in enumerate(test_cases, 1):
        result = sol.nextGreaterElements(nums.copy())
        print(f"Test Case {i}:")
        print(f"Input:    {nums}")
        print(f"Output:   {result}")
        print(f"Expected: {expected}")
        print("PASS" if result == expected else "FAIL")
        print("-" * 40)


# Run all test cases
run_tests()