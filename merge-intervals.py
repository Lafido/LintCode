"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    # @param intervals, a list of Interval
    # @return a list of Interval
    def merge(self, intervals):
        if intervals and len(intervals) > 0:
            intervals.sort(key = lambda x: x.start)
            result = [intervals[0]]
            for i in range(1, len(intervals)):
                prev, cur = result[-1], intervals[i]
                if prev.end >= cur.start:
                    prev.end = max(cur.end, prev.end)
                else:
                    result.append(cur)
            return result
        else:
            return intervals
