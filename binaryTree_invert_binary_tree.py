from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if root is None :
            return 

        # swap left and right
        temp = root.left
        root.left = root.right
        root.right = temp

        # invert subtrees
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

# Helper Function (Inorder Traversal for Checking)
def inorder(root):
    if root is None:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)

# Empty Tree
root = None
print(Solution().invertTree(root))  
# Expected Output: None

# Single Node
root = TreeNode(1)
root = Solution().invertTree(root)
print(inorder(root))
# Expected Output: [1]

# Simple Tree
# #    1
# #   / \
# #  2   3

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

root = Solution().invertTree(root)
print(inorder(root))
# Expected Output: [3, 1, 2]


#        4
#       / \
#      2   7
#     / \ / \
#    1  3 6  9

root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)

root = Solution().invertTree(root)
print(inorder(root))
# Expected Output: [9, 7, 6, 4, 3, 2, 1]

# Time Complexity

# Time: O(n) (visit each node once)

# Space: O(h) (recursive stack, h = tree height)