from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:

        # Key Rule for minDepth
        # If one child is missing, you must take the depth of the other child.
        # You cannot choose a 0 depth unless the node is a leaf.

        # base case
        if root is None :
            return 0

        # if left subtree is missing
        if root.left is None:
            return self.minDepth(root.right) + 1

         # if right subtree is missing
        if root.right is None:
            return self.minDepth(root.left) + 1

        # + 1 for root
        # both subtrees exist
        return min(
            self.minDepth(root.left),
            self.minDepth(root.right)
        ) + 1

# Test Case 1: Empty Tree
root = None
print(Solution().minDepth(root))

# Test Case 2: Single Node
root = TreeNode(1)
print(Solution().minDepth(root))


# Test Case 3: Balanced Tree
#      1
#     / \
#    2   3
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
print(Solution().minDepth(root))


# Test Case 4: Unbalanced Tree
#      1
#     /
#    2
#   /
#  3
root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(3)
print(Solution().minDepth(root))


# Test Case 5: LeetCode Example
# Input: [3,9,20,null,null,15,7]
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(Solution().minDepth(root))
