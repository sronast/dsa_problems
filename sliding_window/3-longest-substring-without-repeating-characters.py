class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lookup = {}
        start = 0
        max_len = 0
        for i, l in enumerate(s):
            if l in lookup and start<=lookup[l]:
                start = lookup[l] + 1
            max_len = max(max_len, i-start+1)
            lookup[l] = i
        return max_len