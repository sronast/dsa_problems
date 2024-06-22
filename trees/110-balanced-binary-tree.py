# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        res = [True]
        def helper(node):
            if not node:
                return 0
            l = helper(node.left)
            r = helper(node.right)

            res[0] = res[0] and (0<=abs(l-r)<=1)

            return 1+max(l,r)
        
        helper(root)
        return res[0]