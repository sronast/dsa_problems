class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        lookup={
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }

        res = []
        tmp = []
        def dfs(idx):
            if idx == len(digits):
                res.append(''.join(tmp))
                return
            for l in lookup[digits[idx]]:
                tmp.append(l)
                dfs(idx+1)
                tmp.pop()
        if not digits:
            return res
        dfs(0)
        return res
            