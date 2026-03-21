class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        if len(s) <= 1 : return s
        
        LPS = ""
        
        for i in range(len(s)) :
            
            # Odd length palindrome
            low, high = i, i
            
            while low >= 0 and high < len(s) and s[low] == s[high]:
                if (high - low + 1) > len(LPS):
                    LPS = s[low:high + 1]
                low -= 1
                high += 1

            # Even length palindrome
            low, high = i, i + 1
            
            while low >= 0 and high < len(s) and s[low] == s[high]:
                if (high - low + 1) > len(LPS):
                    LPS = s[low:high + 1]
                low -= 1
                high += 1

        return LPS