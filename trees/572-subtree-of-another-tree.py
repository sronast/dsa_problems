# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(r1, r2):
            
            if not r1 and not r2:
                return True
            elif (not r2 and r1) or (not r1 and r2) or r1.val!=r2.val:
                return False
            return isSameTree(r1.left, r2.left) and isSameTree(r1.right, r2.right)
        
        q = [root]
        while q:
            nxt = []
            for node in q:
                if isSameTree(node, subRoot):
                    return True
                if node.left:
                    nxt.append(node.left)
                if node.right:
                    nxt.append(node.right)
            q = nxt
        return False