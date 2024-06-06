class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = 0
        i = 0
        j = len(height) - 1
        while i<j:
            cur_area = (j-i) * min(height[i], height[j])
            area = max(area, cur_area)
            if height[i]>height[j]:
                j-=1
            else:
                i+=1
        return area