class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        res = 0
        max_c = 0
        hashmap = {}
        for right, l in enumerate(s):
            hashmap[l] = hashmap.get(l, 0) + 1
            max_c = max(hashmap[l], max_c)
            if k+max_c < 1+ right-left:
                hashmap[s[left]]-=1
                left+=1
            res = max(res, right+1-left)
        return res