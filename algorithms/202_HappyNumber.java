class Solution {
    public boolean isHappy(int n) {
        HashSet<Integer> visited = new HashSet<Integer>();
        
        while (n != 1) {
            if (visited.contains(n))
                return false;
            visited.add(n);
            int sum = 0;
            while (n != 0) {
                sum += Math.pow(n%10, 2);
                n/=10;
            }
            n = sum;
        }
        return true;
    }
}