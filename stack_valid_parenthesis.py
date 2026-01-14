# Valid Parentheses

def isValid(s):
    stack = []
    pair = {')':'(', ']':'[', '}':'{'}
    
    for ch in s:
        if ch in pair:                         # closing bracket
            if not stack or stack[-1] != pair[ch]:
                return False
            stack.pop()
        else:
            stack.append(ch)                   # push opening
    
    return len(stack) == 0

print(isValid("()"))          # Output: True
print(isValid("()[]{}"))      # Output: True
print(isValid("(]"))         # Output: False
print(isValid("([)]"))       # Output: False


# Used in:

# Valid Parentheses

# Next Greater Element

# Undo / Back Navigation

# Evaluate Expression

# Min Stack

# Browser History Navigation

# Balanced Brackets in Code Editors

# Syntax Checking in Compilers