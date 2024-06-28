class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        def is_palindrome(s):
            l = 0
            r = len(s)-1
            while l<r:
                if s[l] != s[r]:
                    return False
                l+=1
                r-=1
            return True

        def dfs(start, end):
            if start == end:
                res.append(tmp.copy())
            for i in range(start,end):
                p1 = s[start:i+1]
                if not is_palindrome(p1):
                    continue
                tmp.append(p1)
                dfs(i+1, end)
                tmp.pop()
        res = []
        tmp = []
        dfs(0, len(s))
        return res
            