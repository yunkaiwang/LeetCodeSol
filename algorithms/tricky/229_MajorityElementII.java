class Solution {
    public List<Integer> majorityElement(int[] nums) {
        Integer[] eles = new Integer[3];
        int[] count = new int[3];
        for (int num : nums) {
            boolean isMajority = false;
            for (int i=0; i<3; ++i) {
                if (eles[i] != null && eles[i] == num) {
                    isMajority = true;
                    ++count[i];
                    break;
                }
            }
            
            if (!isMajority) {
                for (int i=0; i<3; ++i) {
                    if (eles[i] == null || count[i] == 0) {
                        eles[i] = num;
                        count[i] = 1;
                        isMajority = true;
                        break;
                    }
                }
            }
            
            if (!isMajority) {
                for (int i=0; i<3; ++i)
                    --count[i];
            }
        }
        
        for (int i=0; i<3; ++i)
            count[i] = 0;
        
        for (int num: nums) {
            for (int i=0; i<3; ++i) {
                if (eles[i] != null && eles[i] == num)
                    ++count[i];
            }
        }
        List<Integer> res = new LinkedList<Integer>();
        for (int i=0; i<3; ++i) {
            if (count[i] > nums.length/3)
                res.add(eles[i]);
        }
        return res;
    }
}