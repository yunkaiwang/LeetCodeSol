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
    public List<List<Integer>> levelOrderBottom(TreeNode root) {
        List<List<Integer>> lists = new LinkedList<List<Integer>>();
        levelOrder(root, lists, 1);
        return lists;
    }
    
    public void levelOrder(TreeNode root, List<List<Integer>> lists, int currentLevel) {
        if (root == null) return;
        else if (currentLevel > lists.size()) {
            List<Integer> list = new LinkedList<Integer>();
            lists.add(0, list);
        }
        lists.get(lists.size() - currentLevel).add(root.val);
        levelOrder(root.left, lists, ++currentLevel);
        levelOrder(root.right, lists, currentLevel);
    }
}