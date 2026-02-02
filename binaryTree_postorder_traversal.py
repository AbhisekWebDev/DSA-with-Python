from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def __init__ (self) :

        self.ans = []

    def postorder (self, root) :

        if root is None :
            return

        self.postorder(root.left)
        self.postorder(root.right)
        self.ans.append(root.val)

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        self.ans = []

        self.postorder(root)

        return self.ans

def test_postorder():
    sol = Solution()

    # Test Case 1: Empty Tree
    root = None
    print(sol.postorderTraversal(root))
    # Expected: []

    # Test Case 2: Single Node
    root = TreeNode(1)
    print(sol.postorderTraversal(root))
    # Expected: [1]

    # Test Case 3: Balanced Tree
    #       2
    #      / \
    #     1   3
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    print(sol.postorderTraversal(root))
    # Postorder: 1 → 3 → 2
    # Expected: [1, 3, 2]

    # Test Case 4: Left Skewed Tree
    #       3
    #      /
    #     2
    #    /
    #   1
    root = TreeNode(3)
    root.left = TreeNode(2)
    root.left.left = TreeNode(1)
    print(sol.postorderTraversal(root))
    # Postorder: 1 → 2 → 3
    # Expected: [1, 2, 3]

    # Test Case 5: BST Example
    #       5
    #      / \
    #     3   6
    #    / \
    #   2   4
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(6)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    print(sol.postorderTraversal(root))
    # Postorder: 2 → 4 → 3 → 6 → 5
    # Expected: [2, 4, 3, 6, 5]


test_postorder()



        