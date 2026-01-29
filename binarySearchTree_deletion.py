from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        # base case
        if root is None :
            return None

        if key < root.val :
            root.left = self.deleteNode(root.left, key)

        elif key > root.val :
            root.right = self.deleteNode(root.right, key)

        elif key == root.val :

            if root.left is None and root.right is None :
                return None

            elif root.left is None :
                return root.right
            
            elif root.right is None :
                return root.left
            
            else :
                
                # dono hi chile null nhi h
                temp = root.right

                # right side ka left node - inorder successor
                while temp.left != None :
                    temp = temp.left
                
                root.val = temp.val

                root.right = self.deleteNode(root.right, temp.val)

        return root

# Inorder Traversal (BST should stay sorted)
def inorder(root):
    if root is None:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)

# Test Case 1 
# Input:
#         5
#        / \
#       3   6
#      / \   \
#     2   4   7
# key = 3

root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.right = TreeNode(7)

root = Solution().deleteNode(root, 3)
print(inorder(root))


# Output - [2, 4, 5, 6, 7]

# Delete Leaf Node
root = Solution().deleteNode(root, 2)
print(inorder(root))


# Output - [4, 5, 6, 7]

# Delete Node with One Child
root = Solution().deleteNode(root, 6)
print(inorder(root))


# Output - [4, 5, 7]

# Delete Root Node
root = Solution().deleteNode(root, 5)
print(inorder(root))


# Output - [4, 7]

# Delete from Empty Tree
print(Solution().deleteNode(None, 10))


# Output - None