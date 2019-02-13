/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    class helper {
        TreeNode node;
        int depth;
        helper(TreeNode n, int d) {
            node = n;
            depth = d;
        }
    }
    public List<Integer> rightSideView(TreeNode root) {
        int maxD = -1;
        helper temp;
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
        Queue<helper> queue = new LinkedList<helper>();
        queue.add(new helper(root, 0));
        while (queue.size() != 0) {
            temp = queue.remove();
            if (temp.node != null) {
                maxD = Math.max(maxD, temp.depth);
                map.put(temp.depth, temp.node.val);
                queue.add(new helper(temp.node.left, temp.depth + 1));
                queue.add(new helper(temp.node.right, temp.depth + 1));
            }
        }
        
        List<Integer> view = new LinkedList<Integer>();
        for (int i = 0; i<=maxD; ++i) {
            view.add(map.get(i));
        }
        return view;
    }
}