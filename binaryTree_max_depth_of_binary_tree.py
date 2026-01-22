from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        # base case
        if root is None:
            return 0

        # left subtree height
        leftHeight = self.maxDepth(root.left)

        # right subtree height
        rightHeight = self.maxDepth(root.right)

        # +1 for current root
        return max(leftHeight, rightHeight) + 1

# Test Case 1: Empty Tree
root = None
print(Solution().maxDepth(root))

# Test Case 2: Single Node
root = TreeNode(1)
print(Solution().maxDepth(root))


# Test Case 3: Balanced Tree
#      1
#     / \
#    2   3
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
print(Solution().maxDepth(root))


# Test Case 4: Unbalanced Tree
#      1
#     /
#    2
#   /
#  3
root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(3)
print(Solution().maxDepth(root))


# Test Case 5: LeetCode Example
# Input: [3,9,20,null,null,15,7]
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(Solution().maxDepth(root))
