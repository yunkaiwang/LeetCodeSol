class NumArray {
    int[] nums;
    int[] sums;
    
    public NumArray(int[] nums) {
        this.nums = nums;
        this.sums = new int[nums.length+1];
        
        int currSum = 0;
        for (int i=0; i<nums.length;++i) {
            currSum += nums[i];
            this.sums[i+1] = currSum;
        }
    }
    
    public void update(int i, int val) {
        int diff = val - this.nums[i];
        this.nums[i] = val;
        
        for (int j=i;j<this.nums.length;++j) {
            this.sums[j+1] += diff;
        }
    }
    
    public int sumRange(int i, int j) {
        return this.sums[j+1] - this.sums[i];
    }
}

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray obj = new NumArray(nums);
 * obj.update(i,val);
 * int param_2 = obj.sumRange(i,j);
 */