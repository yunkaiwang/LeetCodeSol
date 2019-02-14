# Definition for a point.
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution:
    def maxPoints(self, points: 'List[Point]') -> 'int':
        """
        O(n^2) method, has to time slope by 100 to get rid of the precision problem, faster than 88%
        """
        if len(points) < 2: return len(points)
        max = -float('inf')
        for point in points:
            dict = {}
            cur_max = -float('inf')
            horizontal = 0
            vertical = 0
            overlap = 0
            for point2 in points:
                if point.x == point2.x and point.y == point2.y:
                    overlap += 1
                elif point.x == point2.x:
                    horizontal += 1
                else:
                    slope = (point2.y - point.y) * 100.0 / (point2.x - point.x)
                    
                    if slope in dict:
                        dict[slope] = dict[slope] + 1
                    else:
                        dict[slope] = 1
                    
                    if dict[slope] > cur_max:
                        cur_max = dict[slope]
            
            horizontal += overlap
            cur_max += overlap
            if horizontal > cur_max:
                cur_max = horizontal
            if cur_max > max:
                max = cur_max
        return max
                    
                    
                    