class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int total_len = nums1.length + nums2.length;
        int mid = total_len / 2;
        if (total_len%2 == 1)
            return findKth(0, 0, nums1, nums2, mid);
        else
            return (findKth(0, 0, nums1, nums2, mid) + findKth(0, 0, nums1, nums2, mid-1))/2.0;
    }
    
    public int findKth(int i, int j, int[] nums1, int[] nums2, int k) {
        if (i == nums1.length) {
            return nums2[j + k];
        } else if (j == nums2.length) {
            return nums1[i + k];
        } else if (k == 0) {
            return Math.min(nums1[i], nums2[j]);
        }
        int mid1 = Math.min(nums1.length-i, (k+1)/2);
        int mid2 = Math.min(nums2.length-j, (k+1)/2);
        if (nums1[i+mid1-1] < nums2[j+mid2-1])
            return findKth(i+mid1, j, nums1, nums2, k-mid1);
        return findKth(i, j+mid2, nums1, nums2, k-mid2);
    }
}