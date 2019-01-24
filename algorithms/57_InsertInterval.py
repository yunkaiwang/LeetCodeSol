class Solution:
    def insert(self, intervals, newInterval):
        """
        O(n) solution runs in 52ms beats 99%, but in order to optimize the run time, we should use binary serach to find the place to insert the new interval, but we need to run binary search two time to find the index to insert the new interval since it has two end points, but then we still need to do a potential linear search to find the covered intervals
        """
        start, end, res, i = newInterval.start, newInterval.end, [], 0
        while i < len(intervals):
            if end < intervals[i].start:
                break
            if intervals[i].end < start:
                res.append(intervals[i])
                i += 1
            else:
                start = start if start < intervals[i].start else intervals[i].start
                if end <= intervals[i].end:
                    end = intervals[i].end
                    i += 1
                    break
                else:
                    i += 1
                    while i < len(intervals):
                        if intervals[i].start > end:
                            break
                        elif intervals[i].end >= end:
                            end = intervals[i].end
                            i += 1
                            break
                        else:
                            i += 1
                    break
        res.append(Interval(start, end))
        res += intervals[i:]
        return res