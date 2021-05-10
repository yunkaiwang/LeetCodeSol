class Solution:
    def findMedianSortedArrays(self, nums1: 'List[int]', nums2: 'List[int]') -> 'float':
        """
        O(log(m+n)) method for finding the median
        """
        m, n = len(nums1), len(nums2)
        def findKth(i, j, k):
            if i == m:
                return nums2[j + k]
            elif j == n:
                return nums1[i + k]
            elif k == 0:
                return min(nums1[i], nums2[j])
            
            mid1 = min(m - i, (k + 1) // 2)
            mid2 = min(n - j, (k + 1) // 2)
            a = nums1[i + mid1 - 1]
            b = nums2[j + mid2 - 1]
            if a < b:
                return findKth(i + mid1, j, k - mid1)
            return findKth(i, j + mid2, k - mid2)
        
        if (m + n) % 2:
            return findKth(0, 0, (m+n)//2)
        else:
            return (findKth(0, 0, (m+n)//2-1)+findKth(0,0,(m+n)//2))/2
        