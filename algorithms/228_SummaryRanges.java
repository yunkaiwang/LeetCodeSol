class Solution {
    public List<String> summaryRanges(int[] nums) {
        List<String> ranges = new LinkedList<String>();
        if (nums.length == 0)
            return ranges;
        
        for (int i=0; i<nums.length; ++i) {
            int start = nums[i];
            while (i < nums.length - 1 && nums[i+1] == 1 + nums[i])
                ++i;
            if (nums[i] == start)
                ranges.add(start + "");
            else
                ranges.add(start + "->" + nums[i]);
        }
        return ranges;
    }
}