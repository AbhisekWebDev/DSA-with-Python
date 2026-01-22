# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
from typing import Optional, List

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        ans = []

        if root is None :
            return ans

        # isko queue se kiya jata h
        q = deque([])
        # Queue for BFS
        q.appendleft(root)
        
        # isme ye change hoga - [root.val] k jagah sirf root.val
        ans.append(root.val)

        while len(q) > 0 :

            level = []

            # number of nodes in current level, utna baar ye loop chlega
            for i in range( len(q) ) :
                front = q.pop()

                if front.left != None :
                    q.appendleft(front.left)
                    level.append(front.left.val)

                if front.right != None :
                    q.appendleft(front.right)
                    level.append(front.right.val)

            if len(level) > 0 :

                #  isme ye change hoga - ans.append(level) k jagah sirf level[-1]
                # sirf last element chahiye hume right side view k liye
                ans.append(level[-1])
        
        return ans

# Build the tree
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

s = Solution()
print(s.levelOrder(root))


# Single Node
root = TreeNode(1)
print(Solution().levelOrder(root))


# Empty Tree
print(Solution().levelOrder(None))


    #     3
    #    / \
    #   9  20
    #      / \
    #     15  7