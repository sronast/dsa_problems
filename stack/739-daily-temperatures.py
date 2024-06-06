class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0 for i in range(len(temperatures))]
        stack = []

        for i, t in enumerate(temperatures):
            while stack and t>stack[-1][-1]:
                day, _ = stack.pop()
                res[day] = i-day
            stack.append((i, t))

        return res