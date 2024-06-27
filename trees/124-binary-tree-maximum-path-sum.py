# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [float('-inf')]
        def helper(node):
            if not node:
                return 0
            l = helper(node.left)
            r = helper(node.right)

            l = 0 if l<0 else l
            r = 0 if r<0 else r
            res[0] = max(res[0], l+r+node.val)

            return r+node.val if r>l else l+node.val
        helper(root)
        return res[0]