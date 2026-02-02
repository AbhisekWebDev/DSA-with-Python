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

    def preorder (self, root) :

        if root is None :
            return

        self.ans.append(root.val)
        self.preorder(root.left)
        self.preorder(root.right)

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        self.ans = []

        self.preorder(root)

        return self.ans

def test_preorder():
    sol = Solution()

    # Test Case 1: Empty Tree
    root = None
    print(sol.preorderTraversal(root))  
    # Expected: []

    # Test Case 2: Single Node
    root = TreeNode(1)
    print(sol.preorderTraversal(root))  
    # Expected: [1]

    # Test Case 3: Balanced Tree
    #       2
    #      / \
    #     1   3
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    print(sol.preorderTraversal(root))  
    # Preorder: 2 → 1 → 3
    # Expected: [2, 1, 3]

    # Test Case 4: Unbalanced Tree
    #       3
    #      /
    #     2
    #    /
    #   1
    root = TreeNode(3)
    root.left = TreeNode(2)
    root.left.left = TreeNode(1)
    print(sol.preorderTraversal(root))  
    # Preorder: 3 → 2 → 1
    # Expected: [3, 2, 1]

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
    print(sol.preorderTraversal(root))  
    # Preorder: 5 → 3 → 2 → 4 → 6
    # Expected: [5, 3, 2, 4, 6]

test_preorder()


        