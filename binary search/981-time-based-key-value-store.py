class TimeMap:

    def __init__(self):
        self.lookup = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.lookup:
            self.lookup[key] = []
        self.lookup[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.lookup:
            return ""
        res = self.lookup[key]
        if timestamp<res[0][-1]:
            return ""
        left = 0
        right = len(res)
        while left<right:
            mid = (left+right)//2
            val, ts_mid = res[mid]
            if ts_mid<=timestamp:
                left = mid+1
            else:
                right = mid
        return res[left-1][0]