class Bucket {
    int max = Integer.MIN_VALUE;
    int min = Integer.MAX_VALUE;
    boolean used = false;
    
    void insert(int num) {
        this.max = Math.max(this.max, num);
        this.min = Math.min(this.min, num);
        this.used = true;
    }
}

class Solution {
    public int maximumGap(int[] nums) {
        if (nums.length < 2) return 0;
        
        int max = Integer.MIN_VALUE, min = Integer.MAX_VALUE;
        for (int num: nums) {
            max = Math.max(max, num);
            min = Math.min(min, num);
        }
        
        int bucketSize = Math.max(1, (max - min) / (nums.length - 1));
        int bucketNum = (max-min) / bucketSize + 1;
        Bucket[] buckets = new Bucket[bucketNum];
        for (int i=0; i<bucketNum; ++i) {
            buckets[i] = new Bucket();
        }
        
        for (int num: nums) {
            int bucketIndex = (num - min) / bucketSize;
            buckets[bucketIndex].insert(num);
        }
        int prevMax = min, maxGap = 0;
        for (int i=0; i<bucketNum; ++i) {
            if (!buckets[i].used)
                continue;
            maxGap = Math.max(maxGap, buckets[i].min - prevMax);
            prevMax = buckets[i].max;
        }
        return maxGap;
    }
}