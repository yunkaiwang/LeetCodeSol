class Solution:
    def largestRectangleArea(self, heights):
        
        """
        Two solutions provided, one using stack and the other one uses two arrays to keep track of the number of heights higher than current height on the left and the number of heights higher than current height on the right
        """
        heights += [0]
        stack = []
        max_a = 0
        for i, h in enumerate(heights):
            index = i
            while stack and stack[-1][1] > heights[i]:
                index, height = stack.pop()
                max_a = max(max_a, (i - index) * height)
            stack.append((index, heights[i]))
        return max_a
            
                
        
        left = [1] * len(heights)
        right = [1] * len(heights)
        
        for i in range(len(heights)):
            j = i - 1
            while j >= 0:
                if heights[j] >= heights[i]:
                    left[i] += left[j]
                    j -= left[j]
                else:
                    break
            
            j = i + 1
            while j < len(heights):
                if heights[j] >= heights[i]:
                    right[i] += right[j]
                    j += right[j]
                else:
                    break
        
        max_r = 0
        for i in range(len(heights)):
            max_r = max(max_r, (right[i] + left[i] - 1) * heights[i])
        
        return max_r
            
                