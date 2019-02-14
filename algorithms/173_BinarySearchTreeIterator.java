/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class BSTIterator {
    /**
     * Two solutions provided, one building the inorder traversal in-place, the other one build the in-order traversal in the constructor, so the next and hasNext function can run in O(1) time
     */
    Stack<TreeNode> stack;
    TreeNode curr;
    
    public BSTIterator(TreeNode root) {
        stack = new Stack<TreeNode>();
        curr = root;
    }
    
    /** @return the next smallest number */
    public int next() {
        if (!hasNext())
            return -1;
        
        while (curr != null) {
            stack.push(curr);
            curr = curr.left;
        }
        
        curr = stack.pop();
        int temp = curr.val;
        curr = curr.right;
        return temp;
    }
    
    /** @return whether we have a next smallest number */
    public boolean hasNext() {
        return curr != null || !stack.empty();
    }
}

/**
 * Your BSTIterator object will be instantiated and called as such:
 * BSTIterator obj = new BSTIterator(root);
 * int param_1 = obj.next();
 * boolean param_2 = obj.hasNext();
 */

/**
 * Solution 2
 */
class BSTIterator {
    List<Integer> list;
    int currIndex;
    
    public BSTIterator(TreeNode root) {
        list = new LinkedList<Integer>();
        Stack<TreeNode> stack = new Stack<TreeNode>();
        while (root != null || !stack.empty()) {
            while (root != null) {
                stack.push(root);
                root = root.left;
            }
            
            root = stack.pop();
            list.add(root.val);
            root = root.right;
        }
        currIndex = 0;
    }
    
    /** @return the next smallest number */
    public int next() {
        if (!hasNext())
            return -1;
        
        return list.remove(0);
    }
    
    /** @return whether we have a next smallest number */
    public boolean hasNext() {
        return list.size() > 0;
    }
}
