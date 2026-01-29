from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:

        newNode = TreeNode(target)

        if root == None :
            return newNode

        curr = root

        while curr != None :

            if target < curr.val :

                # left
                if curr.left != None :
                    curr = curr.left
                else :
                    curr.left = newNode
                    break
            
            else :

                # right
                if curr.right != None :
                    curr = curr.right
                else :
                    curr.right = newNode
                    break


        return root


# Helper function: Inorder Traversal (BST check)
# inorder traversal hmesha sorter hotal h
def inorder(root):
    if not root:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)  


# Insert into Non-Empty BST
#         4
#        / \
#       2   7

root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)

root = Solution().insertIntoBST(root, 5)
print(inorder(root))


# Output - [2, 4, 5, 7]

# Insert Smaller Value
root = Solution().insertIntoBST(root, 1)
print(inorder(root))


# Output -[1, 2, 4, 5, 7]

# Insert Larger Value
root = Solution().insertIntoBST(root, 8)
print(inorder(root))


# Output - [1, 2, 4, 5, 7, 8]

# Empty Tree
root = None
root = Solution().insertIntoBST(root, 10)
print(inorder(root))


# Output - [10]

# Complexity

# Time: O(h) (h = height of tree)

# Space: O(1) (iterative, no recursion) 