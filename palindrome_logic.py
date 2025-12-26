str = "racecar"

def is_palindrome(s):
    left = 0                 # start pointer
    right = len(s) - 1       # end pointer
    
    while left < right:      # loop until they meet
        if s[left] != s[right]:
            return False     # mismatch → not palindrome
        
        left += 1            # move left forward
        right -= 1           # move right backward
    
    return True

print(is_palindrome(str))


# Used in:

# Remove Duplicates

# Trapping Rain Water

# 3Sum

# Reverse String

# Pair Sum

# String Manipulation

# Anagram Check

# Longest Palindromic Substring

# Palindrome Number

# Valid Palindrome

# Permutation Palindrome