class TimeMap:
    def __init__(self):
        self.storage = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.storage.setdefault(key, []).append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        arr = self.storage.get(key, [])

        if not arr:
            return ""

        l = 0
        r = len(arr) - 1
        result = -1

        while l <= r:
            mid = (l + r) // 2

            if arr[mid][1] == timestamp:
                return arr[mid][0]
            elif arr[mid][1] > timestamp:
                r = mid - 1
            else:
                result = mid
                l = mid + 1

        return arr[result][0] if result != -1 else ""
