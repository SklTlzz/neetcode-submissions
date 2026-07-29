class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k = float('inf')
        l = 1
        r = max(piles)

        while l <= r:
            need_for_eat = 0
            mid = (l + r) // 2

            for pile in piles:
                hours = (pile + mid - 1) // mid                
                need_for_eat += hours

            if need_for_eat > h:
                l = mid + 1
            elif need_for_eat < h:
                k = min(k, mid)
                r = mid - 1
            else:
                k = min(k, mid)
                r = mid - 1

        return int(k)
