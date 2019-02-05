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
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        /**
        very similar to last question, just add one extra variable to the function call to know whether you reached a level where you should 'zigzag', if so, then you add the element to the front of the list instead of the end
         */
        List<List<Integer>> lists = new LinkedList<List<Integer>>();
        levelOrder(root, lists, 1, false);
        return lists;
    }
    
    public void levelOrder(TreeNode root, List<List<Integer>> lists, int currentLevel, boolean zigzag) {
        if (root == null) return;
        else if (currentLevel > lists.size()) {
            List<Integer> list = new LinkedList<Integer>();
            lists.add(list);
        }
        if (zigzag)
            lists.get(currentLevel-1).add(0, root.val);
        else 
            lists.get(currentLevel-1).add(root.val);
        levelOrder(root.left, lists, ++currentLevel, !zigzag);
        levelOrder(root.right, lists, currentLevel, !zigzag);
    }
}