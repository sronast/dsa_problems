class Solution:
    def countSubstrings(self, s: str) -> int:
        def check(i,j):
            c = 0
            while i>=0 and j<len(s):
                if s[i] == s[j]:
                    i-=1
                    j+=1
                    c+=1
                else:
                    break
            return c
        res = 0
        for k in range(len(s)):
            res+=check(k, k)
            res+=check(k,k+1)
        return res 