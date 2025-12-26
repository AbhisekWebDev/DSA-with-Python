class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Used to visit nodes in a non-decreasing order for BSTs.

# Inorder Traversal of a Binary Tree
def inorder(root):
    if not root:
        return
    
    inorder(root.left)
    print(root.val)
    inorder(root.right)

root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)
print("Inorder Traversal:")
inorder(root)
# Output should be: 1 2 3

# Preorder Traversal of a Binary Tree
def preorder(root):
    if not root:
        return
    
    print(root.val)
    preorder(root.left)
    preorder(root.right)

# Example usage:
print("Preorder Traversal:")
preorder(root)
# Output should be: 2 1 3

# Postorder Traversal of a Binary Tree
def postorder(root):
    if not root:
        return
    
    postorder(root.left)
    postorder(root.right)
    print(root.val)

print("Postorder Traversal:")
postorder(root)

# Level Order Traversal (BFS)
from collections import deque
def level_order(root):
    if not root:
        return
    
    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        print(node.val)
        
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

print("Level Order Traversal:")
level_order(root)

# Example usage:
# Constructing a simple binary tree
#         2
#        / \
#       1   3



# Used in:

# BST Validations

# Sorted Data Retrieval

# Print the node values during traversal






