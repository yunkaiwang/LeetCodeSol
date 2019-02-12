class Solution {
    public int minimumTotal(List<List<Integer>> triangle) {
        if (triangle == null || triangle.size() == 0)
            return 0;
        
        List<Integer> dp = triangle.get(triangle.size() - 1);
        List<Integer> curr;
        
        for (int i=triangle.size()-2; i > -1; --i) {
            curr = triangle.get(i);
            for (int j = 0; j<curr.size(); ++j) {
                dp.set(j, Math.min(dp.get(j), dp.get(j+1))+curr.get(j));
            }
        }
        return dp.get(0);
    }
}