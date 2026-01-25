from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def isMirror(t1, t2):
            # both null
            if t1 is None and t2 is None:
                return True

            # one null
            if t1 is None or t2 is None:
                return False

            return (
                t1.val == t2.val and
                isMirror(t1.left, t2.right) and
                isMirror(t1.right, t2.left)
            )

        if root is None:
            return True

        return isMirror(root.left, root.right)

# test case 1 : empty tree
root = None
print(Solution().isSymmetric(root))


# Test Case 2: Single Node
root = TreeNode(1)
print(Solution().isSymmetric(root))


# Test Case 3: Symmetric Tree
#         1
#       /   \
#      2     2
#     / \   / \
#    3   4 4   3
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(4)
print(Solution().isSymmetric(root))


# Test Case 4: Not Symmetric
#         1
#       /   \
#      2     2
#       \     \
#        3     3
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.right = TreeNode(3)
root.right.right = TreeNode(3)
print(Solution().isSymmetric(root))


# Test Case 5: Different Values
#         1
#       /   \
#      2     3
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
print(Solution().isSymmetric(root))