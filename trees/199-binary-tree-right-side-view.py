# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res
        q = [root]
        while q:
            nxt = []
            for i, node in enumerate(q):
                if node.left:
                    nxt.append(node.left)
                if node.right:
                    nxt.append(node.right)
                if i == len(q) - 1:
                    res.append(node.val)
            q = nxt
        return res
        