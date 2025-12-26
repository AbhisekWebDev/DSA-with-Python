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