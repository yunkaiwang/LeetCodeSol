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
        max = 0
        start, end = 0, len(height) - 1 # current start and end container
        
        while start < end: # while not reached the middle point yet:
            l_h = height[start]
            r_h = height[end]
            
            if l_h > r_h:
                h = r_h
            else:
                h = l_h
            
            size = (end - start) * h
            if size > max:
                max = size
            if l_h > r_h:
                end -= 1
            else:
                start += 1
        return max