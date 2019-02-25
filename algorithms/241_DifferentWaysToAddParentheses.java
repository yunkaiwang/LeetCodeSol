class Solution {
    HashMap<String, List<Integer>> map = new HashMap<String, List<Integer>>();
    public List<Integer> diffWaysToCompute(String input) {
        if (this.map.containsKey(input))
            return map.get(input);
        
        List<Integer> res = new LinkedList<Integer>();
        for (int i=0; i<input.length(); ++i) {
            char c = input.charAt(i);
            if (c == '+' || c == '-' || c == '*') {
                List<Integer> left = diffWaysToCompute(input.substring(0, i));
                List<Integer> right = diffWaysToCompute(input.substring(i+1));
                for (int l: left) {
                    for (int r:right) {
                        if (c == '+')
                            res.add(l+r);
                        else if (c == '-')
                            res.add(l-r);
                        else
                            res.add(l*r);
                    }
                }
            }
        }
        if (res.isEmpty())
            res.add(Integer.parseInt(input));
        map.put(input, res);
        return res;
    }
}