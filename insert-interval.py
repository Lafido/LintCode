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
    """
    Insert a new interval into a sorted non-overlapping interval list.
    @param intevals: Sorted non-overlapping interval list
    @param newInterval: The new interval.
    @return: A new sorted non-overlapping interval list with the new interval.
    """

    def insert(self, intervals, newInterval):
        results = []
        if not newInterval:
            return intervals
        if not intervals or len(intervals) == 0:
            return [newInterval]
        debug = True
        flag = False
        for interval in intervals:
            if not flag: # before add newInterval
                if interval.end < newInterval.start:
                    results.append(interval)
                elif newInterval.end < interval.start:
                    results.append(newInterval)
                    results.append(interval)
                    flag = True
                elif newInterval.end == interval.start:
                    results.append(Interval(newInterval.start, interval.end))
                    flag = True
                elif newInterval.end > interval.start:
                    results.append(Interval(newInterval.start if newInterval.start < interval.start else interval.start, newInterval.end if newInterval.end > interval.end else interval.end))
                    flag = True
            else:
                lastInterval = results[-1]
                if lastInterval.end < interval.start:
                    results.append(interval)
                elif lastInterval.end >= interval.start:
                    results[-1] = Interval(lastInterval.start, lastInterval.end if lastInterval.end > interval.end else interval.end)
        if not flag:
            results.append(newInterval)
        return results
