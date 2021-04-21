class Solution {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> lists = new LinkedList<List<Integer>>();
        if (numRows == 0) return lists;
        List<Integer> list = new LinkedList<Integer>();
        list.add(1);
        lists.add(list);
        
        for (int i = 1; i < numRows; ++i) {
            list = new LinkedList<Integer>();
            list.add(1);
            for (int j = 1; j < i; ++j) {
                list.add(lists.get(i-1).get(j-1) + lists.get(i-1).get(j));
            }
            list.add(1);
            lists.add(list);
        }
        return lists;
    }
}