class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]

        merged = []

        for i, interval in enumerate(intervals):
            if interval[1] < newInterval[0]:
                merged.append(interval)
            elif interval[0] > newInterval[1]:
                merged.append(newInterval)
                
                return merged + intervals[i:]
            else:
                curr_start = min(interval[0], newInterval[0])
                curr_end = max(interval[1], newInterval[1])
                newInterval = [curr_start, curr_end]

        merged.append(newInterval)

        return merged
