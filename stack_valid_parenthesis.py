# Valid Parentheses

def isValid(s):
    # ye islye kiye kyunki valid parenthesis hone k lye lenth even hona chahiye, because har opening parenthesis k lye closing parenthesis hona chahiye, yahi chiz k lye ye corner case kiye h
    if len(s) % 2 == 1 :
        return False
        
    st = []

    for ch in list(s) :

        # jab bhi ek opening parenthesis milega, hm usko stack me push kr denge
        if ch in '([{' :
            st.append(ch)
            
        else :

            # jab bhi ek closing parenthesis milega, usko stack se pop kr denge
            if len(st) == 0 :
                return False

            # agr opening parenthesis jo stack me present h aur agla closing parenthesis usi opening parenthesis ka hi closing parenthesis h to us opening parenthesis ko stack se pop kr denge
            top = st.pop()

            if ch == ')' and top != '(' :
                return False
            elif ch == '}' and top != '{' :
                return False
            elif ch == ']' and top != '[' :
                return False


    return len(st) == 0

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