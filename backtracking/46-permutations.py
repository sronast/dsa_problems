class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        temp, res, visited = [], [], {}
        def helper():
            if len(temp) == len(nums):
                res.append(temp.copy())
                return
            for num in nums:
                if num in visited and visited[num]:
                    continue
                visited[num] = 1
                temp.append(num)
                helper()
                temp.pop()
                visited[num] = 0
            
        helper()
        return res
                
            
        