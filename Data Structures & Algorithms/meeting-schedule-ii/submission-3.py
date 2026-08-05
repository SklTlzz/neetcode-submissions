"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0

        starts = [i.start for i in intervals]
        ends = [i.end for i in intervals]

        starts.sort()
        ends.sort()

        count_rooms = 0
        max_rooms = 0
        s, e = 0, 0

        while s != len(starts) and e != len(ends):
            if starts[s] < ends[e]:
                count_rooms += 1
                s += 1
            else:
                count_rooms -= 1
                e += 1

            max_rooms = max(max_rooms, count_rooms)

        return max_rooms
