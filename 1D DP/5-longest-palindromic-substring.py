class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def check(l, r):
            while l>=0 and r<len(s):
                if s[l] == s[r]:
                    l-=1
                    r+=1
                else:
                    break
            return (l,r)

        l_i = 0
        r_i = 0

        for i in range(len(s)):
            l, r = check(i, i)
            if r-l > r_i - l_i:
                l_i = l
                r_i = r
            
            l, r = check(i,i+1)
            if r-l > r_i - l_i:
                l_i = l
                r_i = r
        return s[l_i+1:r_i]