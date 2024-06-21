# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        d = [0]
        def helper(node):
            if not node:
                return 0
            l = helper(node.left)
            r = helper(node.right)

            d[0] = max(d[0], l+r)
            return 1 + max(l, r)
        helper(root)
        return d[0]