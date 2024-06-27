class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        res = []
        if not root:
            return res
        q = [root]
        while q:
            nxt = []
            tmp = []
            for node in q:
                tmp.append(node.val)
                if node.left:
                    nxt.append(node.left)
                if node.right:
                    nxt.append(node.right)
            res.append(tmp)
            q = nxt
        return res