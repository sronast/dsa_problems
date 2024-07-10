class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        def helper(string):
            if not string:
                return True
            
            if string in lookup:
                return lookup[string]
            res = False
            for word in wordDict:

                if word == string[:len(word)]:
                    res = res or helper(string[len(word):])
            lookup[string] = res
            return res
        
        lookup = {}
        return helper(s)