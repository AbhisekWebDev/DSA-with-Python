from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def searchBST(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:

        if root is None :
            return None

        curr = root

        while curr != None :
            if curr.val == target :
                return curr
            elif target < curr.val :
                curr = curr.left # isko left subtree me le jynge
            else :
                curr = curr.right

        # jab kuch a mile tab
        return None
    

def print_tree(root):
    if not root:
        return []
    return [root.val, print_tree(root.left), print_tree(root.right)]

# Normal BST
#         4
#        / \
#       2   7
#      / \
#     1   3

root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)

result = Solution().searchBST(root, 2)
print(print_tree(result))


# Output
# [2, [1, [], []], [3, [], []]]

# Target is Root
result = Solution().searchBST(root, 4)
print(print_tree(result))


# Output
# [4, [2, [1, [], []], [3, [], []]], [7, [], []]]

# Target Not Found
result = Solution().searchBST(root, 5)
print(result)


# Output - None


# Empty Tree
result = Solution().searchBST(None, 1)
print(result)

# Output - None




# Time & Space Complexity

# Time: O(h) → height of BST

# Space: O(1) (iterative, no recursion)