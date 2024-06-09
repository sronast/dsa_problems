class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start = 0 
        end = len(matrix) - 1

        mid = 0

        while start<end:
            mid = (end+start)//2
            if target<=matrix[mid][-1]:
                end = mid
            else:
                start = mid+1
        left = 0
        right = len(matrix[0]) - 1

        while left<right:
            center = left + (right-left)//2
            if target<=matrix[start][center]:
                right = center
            else:
                left = center+1
        return matrix[start][left] == target