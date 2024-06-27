class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def inorder(root):
            if not root:
                return []
            return inorder(root.left)+[root.val]+inorder(root.right)
        
        res = inorder(root)
        for i,n in enumerate(res):
            if i == 0:
                continue
            if res[i-1]>=n:
                return False
        return True