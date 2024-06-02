class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        j = len(numbers)-1
        i = 0
        while i<j:
            res = numbers[i] + numbers[j]
            if res>target:
                j-=1
            elif res<target:
                i+=1
            else:
                return [i+1, j+1]
        return [-1, -1]