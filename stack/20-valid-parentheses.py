class Solution:
    def isValid(self, s: str) -> bool:
        a = '}{)(]['
        lookup = {}
        i = 0
        while i<len(a):
            print(a[i])
            lookup[a[i]] = a[i+1]
            i+=2
        
        stack = []
        for b in s:
            if b not in lookup:
                stack.append(b)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if top != lookup[b]:
                    return False
        return not stack