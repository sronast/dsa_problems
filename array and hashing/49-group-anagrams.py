class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lookup = {}
        for word in strs:
            key = [0]*26
            for l in word:
                key[ord(l) - ord('a')] += 1
            key = tuple(key)
            if key not in lookup:
                lookup[key] = []
            lookup[key].append(word)
        return list(lookup.values())