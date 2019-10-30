class Solution:
    def maxArea(self, height):
        """
        easy O(n^2) solution, but very inefficient, O(n^2) time needed
        """
        # max = 0
        # for i in range(len(height) - 1):
        #     for j in range(i + 1, len(height)):
        #         min_height = height[j]
        #         if height[i] < height[j]:
        #             min_height = height[i]
                
        #         size = (j - i) * min_height
                
        #         if size > max:
        #             max = size
        # return max

        """ linear time algorithm """
        # the linear time algorithm for this problem is very easy to be think of, we start from the two end of the list, and tends to goes to middle, whenever we go, we keep track of the maximum size we met so far(and the indices of the max area if we need), then when we reach the mid point(not the actual mid point, but the point where left boundary and right boundary collide), then we know we are finished since all other possible areas are definitely smaller, this will save us from comparing n^2 numbers to only n numbers since we know the size doesn't only depend on the height but also the distance between two boundaries
        i, j = 0, len(height) - 1
        max_water = 0
        
        while i < j:
            l_h = height[i]
            r_h = height[j]
            
            max_water = max(min(l_h, r_h) * (j-i), max_water)
            if l_h < r_h:
                i+=1
            else:
                j-=1
        return max_water