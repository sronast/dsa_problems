import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for n in nums:
            hashmap[n] = hashmap.get(n, 0) + 1

        q = []
        for kk, v in hashmap.items():
            q.append((-v, kk))
        print(q)
        heapq.heapify(q)
        res = []
        for _ in range(k):
            _, nn = heapq.heappop(q)
            res.append(nn)
        return res