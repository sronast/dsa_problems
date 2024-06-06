class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arr = [(p,s) for p, s in zip(position, speed)]
        arr.sort(reverse=True)

        res = len(position)
        print(arr)
        prev_time = float('inf')
        
        for i,ps in enumerate(arr):
            time = (target-ps[0])/ps[1]
            if i == 0:
                prev_time =time 
                continue
            if time<=prev_time:
                res-=1
            else:
                prev_time = time

        return res

        