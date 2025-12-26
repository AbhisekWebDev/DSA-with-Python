# Longest substring without repeating characters

def longest_substring(s):
    char_set = set()     # store unique characters
    left = 0
    result = 0
    
    for right in range(len(s)):       # expand window
        while s[right] in char_set:   # if duplicate found
            char_set.remove(s[left])  # shrink window
            left += 1
        
        char_set.add(s[right])        # add new char
        result = max(result, right-left+1)
    
    return result

print(longest_substring("abcabcbb"))  # Output: 3 ("abc")


# Used when asked for:

# longest / smallest substring

# subarray sum

# count something in continuous range