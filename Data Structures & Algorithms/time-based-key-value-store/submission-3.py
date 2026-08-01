class TimeMap:
    def __init__(self):
        self.storage = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.storage[key] = self.storage.get(key, []) + [[value, timestamp]]

    def get(self, key: str, timestamp: int) -> str:
        if not self.storage.get(key, []):
            return ""

        l = 0
        r = len(self.storage[key]) - 1
        result = -1

        while l <= r:
            mid = (l + r) // 2

            if self.storage[key][mid][1] == timestamp:
                return self.storage[key][mid][0]
            elif self.storage[key][mid][1] > timestamp:
                r = mid - 1
            else:
                result = max(result, mid)
                l = mid + 1

        return self.storage[key][result][0] if result != -1 else ""
