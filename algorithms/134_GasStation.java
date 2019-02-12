class Solution {
    public int canCompleteCircuit(int[] gas, int[] cost) {
        /**
         * O(n) solution using constant space, remember current fuel difference, and whenver you meet a station where you cannot reach using current amount of fuel, then you know you have to start at a later gas station
         */
        int currStart = 0, currDiff = 0, totalDiff = 0;
        
        for (int i=0; i < gas.length; ++i) {
            int diff = gas[i] - cost[i];
            totalDiff += diff;
            currDiff += diff;
            
            if (currDiff < 0) {
                currStart = i + 1;
                currDiff = 0;
            }
        }
        if (totalDiff < 0)
            return -1;
        
        return currStart;
    }
}