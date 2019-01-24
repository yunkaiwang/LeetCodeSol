# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e
class Solution:
    def merge(self, intervals):
        """
        Sorting can save the runtime from O(n^2) to O(n logn) since otherwise for every interval we have to search through the entire list of intervals we have right now to find where to fit the current interval, best run time 56ms beats 99%
        """

        # assume that the collection of intervals are unsorted, even though the examples given are all sorted
        intervals.sort(key=lambda x:x.start) # since it's unsorted, then sorting them will give a better performance
        cur_intervals = intervals[:1]
        
        for interval in intervals[1:]:     
            if interval.start <= cur_intervals[-1].end:
                if interval.end > cur_intervals[-1].end:
                    cur_intervals[-1].end = interval.end
            else:
                cur_intervals.append(interval)
        return cur_intervals
            
            
        
        
            
            
        
        