from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def __init__(self):
        self.ans = True          # stores whether tree remains balanced or not

    def maxDepth(self, root: Optional[TreeNode]) -> int:

        # base case
        if root is None:
            return 0

        # height of left subtree
        leftHeight = self.maxDepth(root.left)

        # height of right subtree
        rightHeight = self.maxDepth(root.right)

        # NEW: if height difference exceeds 1, tree is unbalanced
        if abs(leftHeight - rightHeight) > 1:
            self.ans = False

        # return height of current subtree
        return max(leftHeight, rightHeight) + 1

    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        # NEW: trigger depth calculation which also updates self.ans
        self.maxDepth(root)

        # NEW: final balanced/unbalanced result
        return self.ans

# Test Case 1: Empty Tree
root = None
print(Solution().isBalanced(root))


# Test Case 2: Single Node
root = TreeNode(1)
print(Solution().isBalanced(root))


# Test Case 3: Balanced Tree
#         1
#        / \
#       2   3
#      /
#     4
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
print(Solution().isBalanced(root))


# Test Case 4: Unbalanced Tree
#         1
#        /
#       2
#      /
#     3
#    /
#   4
root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(3)
root.left.left.left = TreeNode(4)
print(Solution().isBalanced(root))


# Test Case 5: Height Difference at Root
#         1
#        / \
#       2   2
#      /
#     3
#    /
#   4
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.left.left = TreeNode(4)
print(Solution().isBalanced(root))


# Key Notes (Interview Tip):
# ✔ Time Complexity: O(n)
# ✔ Space Complexity: O(h) (recursion stack)
# ✔ Efficient because height & balance are checked together