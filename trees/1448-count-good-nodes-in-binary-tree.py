# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = [0]
        def dfs(node, path_max):
            if not node:
                return
            cur_val = node.val
            if cur_val >= path_max:
                res[0] = res[0] + 1
                path_max = cur_val
            dfs(node.left, path_max)
            dfs(node.right, path_max)
        dfs(root, root.val)
        return res[0]

            
        