class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        stack = []

        def helper(start, end, n):
            if end == n:
                result.append(''.join(stack.copy()))
                return
            if start<n:
                stack.append('(')
                helper(start+1, end, n)
                stack.pop()
            if end<start:
                stack.append(')')
                helper(start, end+1, n)
                stack.pop()
        
        helper(0, 0, n)
        return result
        