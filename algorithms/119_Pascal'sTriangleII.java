class Solution {
    public List<Integer> getRow(int rowIndex) {
        List<Integer> lastList = new LinkedList<Integer>(), list;
        lastList.add(1);
        if (rowIndex == 0) return lastList;
        
        for (int i = 1; i < rowIndex + 1; ++i) {
            list = new LinkedList<Integer>();
            list.add(1);
            for (int j = 1; j < i; ++j) {
                list.add(lastList.get(j-1) + lastList.get(j));
            }
            list.add(1);
            lastList = list;
        }
        return lastList;
    }
}