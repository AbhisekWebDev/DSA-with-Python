class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        if len(s) == 0 :
            return True

        st1 = []
        st2 = []

        for ch in list(s) :

            if ch != '#' :
                st1.append(ch)
            elif len(st1) > 0 :
                st1.pop()
            
        for ch in list(t) :

            if ch != '#' :
                st2.append(ch)
            elif len(st2) > 0 :
                st2.pop()

        return st1 == st2
        
sol = Solution()

# Test case 1
s = "ab#c"
t = "ad#c"
print(sol.backspaceCompare(s, t))   # True

# Test case 2
s = "ab##"
t = "c#d#"
print(sol.backspaceCompare(s, t))   # True

# Test case 3
s = "a#c"
t = "b"
print(sol.backspaceCompare(s, t))   # False

# Test case 4
s = "a##c"
t = "#a#c"
print(sol.backspaceCompare(s, t))   # True

# Test case 5 (edge case)
s = ""
t = ""
print(sol.backspaceCompare(s, t))   # True

# Test case 6 (edge case)
s = ""
t = "a#"
print(sol.backspaceCompare(s, t))   # True
