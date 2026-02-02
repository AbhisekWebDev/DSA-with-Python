from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def check(self, root, mn, mx) :

        # Base case: empty tree is valid BST
        if root is None :
            return True

        # If current node violates BST range
        if root.val < mn or root.val > mx :
            return False

        # Left subtree must be < root.val
        # Right subtree must be > root.val
        checkLeft = self.check(root.left, mn, root.val - 1)
        checkRight = self.check(root.right, root.val + 1, mx)

        return checkLeft and checkRight

    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        # Use very large bounds
        return self.check(root, -100000000000000000000000, 100000000000000000000000)

# Valid BST
#         2
#        / \
#       1   3
root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)

print(Solution().isValidBST(root))  # True

# Invalid BST
#         5
#        / \
#       1   4
#          / \
#         3   6
# 3 is in the right subtree of 5, but is smaller than 5
root = TreeNode(5)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.right.left = TreeNode(3)
root.right.right = TreeNode(6)
print(Solution().isValidBST(root))  # False

# Single Node
root = TreeNode(10)
print(Solution().isValidBST(root))  # True

# Empty Tree
root = None
print(Solution().isValidBST(root))  # True

# Duplicate Values (Not Allowed in BST)
#     2
#      \
#       2
root = TreeNode(2)
root.right = TreeNode(2)

print(Solution().isValidBST(root))  # False

# Time Complexity
# Time: O(n) — visits each node once
# Space: O(h) — recursion stack (h = tree height)