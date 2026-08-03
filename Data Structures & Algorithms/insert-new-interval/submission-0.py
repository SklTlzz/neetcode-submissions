class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]

        intervals.append(newInterval)
        intervals.sort(key=lambda x: x[0])
        merged = [intervals[0]]

        for i in range(1, len(intervals)):
            if intervals[i][0] <= merged[-1][1]:
                curr_start = min(intervals[i][0], merged[-1][0])
                curr_end = max(intervals[i][1], merged[-1][1])
                merged[-1] = [curr_start, curr_end]
            else:
                merged.append(intervals[i])

        return merged