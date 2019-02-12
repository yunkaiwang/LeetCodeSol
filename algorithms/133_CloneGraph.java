/**
 * Definition for undirected graph.
 * class UndirectedGraphNode {
 *     int label;
 *     List<UndirectedGraphNode> neighbors;
 *     UndirectedGraphNode(int x) { label = x; neighbors = new ArrayList<UndirectedGraphNode>(); }
 * };
 */
public class Solution {
    /**
     * Has to use O(n) space here since there is no way we can store the new node somewhere so that we know which original node it correspond to in the original graph
     */
    HashMap<UndirectedGraphNode, UndirectedGraphNode> map = new HashMap<UndirectedGraphNode, UndirectedGraphNode>();
    public UndirectedGraphNode cloneGraph(UndirectedGraphNode node) {
        if (node == null) return node;
        UndirectedGraphNode copy = new UndirectedGraphNode(node.label);
        
        map.put(node, copy);
        for (UndirectedGraphNode neighbor : node.neighbors) {
            copy.neighbors.add(map.containsKey(neighbor) ? map.get(neighbor) : cloneGraph(neighbor));
        }
        return copy;
    }
}