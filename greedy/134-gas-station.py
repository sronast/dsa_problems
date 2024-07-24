class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost)>sum(gas):
            return -1
        
        start = 0
        surplus = 0
        i = 0
        while i < len(gas):
            station = gas[i] - cost[i]
            if surplus + station >=0:
                surplus += station
            else:
                start = i+1
                surplus = 0
            i+=1
        return start