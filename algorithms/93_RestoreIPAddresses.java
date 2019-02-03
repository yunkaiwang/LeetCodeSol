class Solution {
    public List<String> restoreIpAddresses(String s) {
        List<String> res = new LinkedList<String>();
        if (s.length() < 4) {
            return res;
        }
        DFS(s, "", 0, res);
        return res;
    }
    
    public void DFS(String remaining, String ip, int count, List<String> l) {
        if (count == 4) {
            if (remaining.length() == 0) {
                l.add(ip.substring(1));
            }
            return;
        }

        int limit = Math.min(remaining.length() + 1, 4);
        for (int i = 1; i < limit; ++i) {
            if (remaining.charAt(0) == '0' && i > 1) {
                return;
            }
            if (Integer.parseInt(remaining.substring(0, i)) < 256) {
                DFS(remaining.substring(i), ip + "." + remaining.substring(0, i), count+1, l);
            }
        }
    }
}