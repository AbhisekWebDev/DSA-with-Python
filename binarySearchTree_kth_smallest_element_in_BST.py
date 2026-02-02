from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def __init__ (self) :

        self.ans = []

    def inorder (self, root) :

        if root is None :
            return

        self.inorder(root.left)
        self.ans.append(root.val)
        self.inorder(root.right)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        self.ans = []

        self.inorder(root)
            
        return self.ans[k - 1]

def test_kth_smallest():
    sol = Solution()

    # Test Case 1
    #       3
    #      / \
    #     1   4
    #      \
    #       2
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.left.right = TreeNode(2)

    print(sol.kthSmallest(root, 1))  # Expected: 1
    print(sol.kthSmallest(root, 2))  # Expected: 2
    print(sol.kthSmallest(root, 3))  # Expected: 3

    # Test Case 2
    #       5
    #      / \
    #     3   6
    #    / \
    #   2   4
    #  /
    # 1
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(6)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.left.left.left = TreeNode(1)

    print(sol.kthSmallest(root, 3))  # Expected: 3


test_kth_smallest()

        