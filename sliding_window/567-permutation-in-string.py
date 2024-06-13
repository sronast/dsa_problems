from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        lookup = Counter(s1)
        lookup_backup = lookup.copy()
        N = len(lookup)
        left = 0
        for right, l in enumerate(s2):
            if l in lookup and lookup[l] > 0:
                lookup[l] -= 1
                if lookup[l] == 0:
                    N-=1
            elif l in lookup and lookup[l] == 0:
                while s2[left] != l:
                    cur = s2[left]
                    if cur in lookup:
                        if lookup[cur] == 0:
                            N+=1
                        lookup[cur] += 1
                    left+=1
                left+=1
            else:
                lookup = lookup_backup.copy()
                N = len(lookup)
                left = right+1
            if N == 0:
                return True
        return False
                
