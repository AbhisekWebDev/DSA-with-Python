# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    
    # Step 1: Inorder traversal
    def inorder(self, root, arr):
        if root is None:
            return
        
        self.inorder(root.left, arr)
        arr.append(root.val)
        self.inorder(root.right, arr)

    # Step 2: Build balanced BST
    def buildBST(self, arr, l, r):
        if l > r:
            return None
        
        mid = (l + r) // 2
        root = TreeNode(arr[mid])
        
        root.left = self.buildBST(arr, l, mid - 1)
        root.right = self.buildBST(arr, mid + 1, r)
        
        return root

    def balanceBST(self, root):
        arr = []
        self.inorder(root, arr)   # sorted values
        
        return self.buildBST(arr, 0, len(arr) - 1)
    

# level order traversal for output
from collections import deque

def printTree(root):
    if not root:
        return []

    q = deque([root])
    res = []

    while q:
        node = q.popleft()
        if node:
            res.append(node.val)
            q.append(node.left)
            q.append(node.right)
        else:
            res.append(None)

    # remove trailing None values
    while res and res[-1] is None:
        res.pop()

    return res


# Input tree: 1 -> 2 -> 3 -> 4 (right skewed)
root = TreeNode(1)
root.right = TreeNode(2)
root.right.right = TreeNode(3)
root.right.right.right = TreeNode(4)

sol = Solution()
newRoot = sol.balanceBST(root)

print(printTree(newRoot))



# Interview Tip

# Balance BST by converting to sorted array and rebuilding using divide & conquer.

# Time Complexity:

# Inorder: O(n)

# Build BST: O(n)
# 👉 Total O(n)