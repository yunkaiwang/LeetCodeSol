class Solution:
    def merge(self, nums1, m, nums2, n):  
        """
        constant space and linear time complexity
        """      
        i, j = m - 1, n - 1
        
        for k in range(m + n - 1, -1, -1):
            if i > -1 and j > -1:
                if nums1[i] > nums2[j]:
                    nums1[k] = nums1[i]
                    i -= 1
                else:
                    nums1[k] = nums2[j]
                    j -= 1
            elif i > -1:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1