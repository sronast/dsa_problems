# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_ind = {v:i for i,v in enumerate(inorder)}
        pre = [0]
        def helper(left,right):
            if left>=right:
                return None
            val = preorder[pre[0]]
            pre[0]+=1
            node = TreeNode(val)
            val_ind = inorder_ind[val]
            node.left = helper(left, val_ind)
            node.right = helper(val_ind+1, right)
            return node
        return helper(0, len(inorder))   