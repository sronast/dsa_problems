class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = {}
        for l in s:
            hashmap[l] = hashmap.get(l, 0) +1
        
        for l in t:
            hashmap[l] = hashmap.get(l, 0) - 1
        
        for v in hashmap.values():
            if v != 0:
                return False
        return True