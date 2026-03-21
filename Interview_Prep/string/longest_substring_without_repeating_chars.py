# sliding window

class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:

        left = 0 # 'right' is handled by the loop, iterating 0 to end of string
        
        res = set() # This tracks characters in the CURRENT window

        max_len = 0 # Fixed variable name

        for right in range(len(s)):
            
            # If the new character is already in the set, we have a duplicate.
            # We must shrink the window from the left until the duplicate is gone.
            while s[right] in res:
                res.remove(s[left])
                left += 1
            
            # Now the window is valid, add the new character
            res.add(s[right])
            
            # Update the max length
            max_len = max(max_len, right - left + 1)

        return max_len
    
# How the Logic FlowsThe code maintains a "window" of unique characters between the left and right indices.
# The Expansion: The right pointer expands the window by one character in every iteration of 
# the loop.The Contraction: If s[right] is already in our res set, it means the window is no 
# longer valid. The while loop shrinks the window from the left until that specific duplicate 
# character is removed.The Record: Once the window is guaranteed to be unique, we update max_len.
# The length of any window is always $right - left + 1$.
# Efficiency AnalysisTime Complexity: $O(n)$. 
# Although there is a nested while loop, each character is added to the set once and removed 
# at most once. The left and right pointers both travel from $0$ to $n$.
# Space Complexity: $O(min(m, n))$, where $n$ is the length of the string and $m$ is the size 
# of the character set (e.g., 26 for lowercase English, or 128 for ASCII).