from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        lookup = Counter(t)
        count = len(lookup)
        left = 0
        index_left, index_right = 0, len(s)
        found = False
  
        for right, l in enumerate(s):
            if l not in lookup:
                continue
            lookup[l] = lookup[l] - 1
            if lookup[l] == 0:
                count-=1
            while count == 0:
                found = True
                if left<=right:
                    if right-left<= index_right - index_left:
                        index_left = left
                        index_right = right
                    if s[left] in lookup:
                        lookup[s[left]] = lookup[s[left]]+1
                        if lookup[s[left]] > 0:
                            count+=1
                    left+=1
                else:
                    break
        return s[index_left:index_right+1] if found else ''
                
               

