class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_speed = 1
        max_speed = max(piles)
        
        while min_speed < max_speed:
            mid = min_speed + (max_speed-min_speed)//2
            hours = 0
            for p in piles:
                hours += p//mid
                if p % mid:
                    hours += 1
            
            if hours>h:
                min_speed = mid+1
            else:
                max_speed = mid
        return min_speed
                