class Solution {
    public boolean containsNearbyAlmostDuplicate(int[] nums, int k, int t) {
        /**
         * 2 solutions provided, one using treeSet, which will run in O(n lgk) time since we are keep tracking k items in the set, and we are manipulating n items, each will take logk time, so the total complexity becomes O(nlogk).
         * 
         * The second idea is better, which uses HashSet, and use bucket to store the numbers instead, so it combines the idea using bucket sort and the set idea, the difference between each number in the same bucket is at most t, so there are 3 buckets possible, where the neadby element can live in
         */

        // if (t < 0 || k < 1 || nums.length == 0) return false;
        // TreeSet<Long> set = new TreeSet<Long>();
        // for (int i=0; i<nums.length; ++i) {
        //     Long num = new Long(nums[i]);
        //     Long floor = set.floor(num + t);
        //     Long ceil = set.ceiling(num - t);
        //     if ((floor != null && floor >= num)
        //             || (ceil != null && ceil <= num)) {
        //         return true;
        //     }
        //     set.add(num);
        //     if (i >= k)
        //         set.remove((long)nums[i-k]);
        // }
        // return false;


        if (k < 1 || t < 0) return false;
        Map<Long, Long> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            long remappedNum = (long) nums[i] - Integer.MIN_VALUE;
            long bucket = remappedNum / ((long) t + 1);
            if (map.containsKey(bucket)
                    || (map.containsKey(bucket - 1) && remappedNum - map.get(bucket - 1) <= t)
                        || (map.containsKey(bucket + 1) && map.get(bucket + 1) - remappedNum <= t))
                            return true;
            if (map.entrySet().size() >= k) {
                long lastBucket = ((long) nums[i - k] - Integer.MIN_VALUE) / ((long) t + 1);
                map.remove(lastBucket);
            }
            map.put(bucket, remappedNum);
        }
        return false;
    }
}