class Solution {
    class graphNode {
        List<graphNode> neighbours;
        boolean visited;
        boolean currentVisiting;
        
        public graphNode() {
            neighbours = new LinkedList<graphNode>();
            visited = false;
            currentVisiting = false;
        }
        
        public boolean dfs() {
            if (currentVisiting)
                return false;
            
            currentVisiting = true;
            for (graphNode neighbour: neighbours) {
                neighbour.visited = true;
                if (!neighbour.dfs())
                    return false;
            }
            currentVisiting = false;
            return true;
        }
    }
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        Map<Integer, graphNode> map = new HashMap<Integer, graphNode>();
        
        for (int[] prerequisite: prerequisites) {
            graphNode head, tail;
            if ((head = map.get(prerequisite[0])) == null) {
                head = new graphNode();
                map.put(prerequisite[0], head);
            }
            if ((tail = map.get(prerequisite[1])) == null) {
                tail = new graphNode();
                map.put(prerequisite[1], tail);
            }
            head.neighbours.add(tail);
        }
        
        for (int i=0; i<numCourses; ++i) {
            if (map.get(i) != null) {
                graphNode temp = map.get(i);
                if (!temp.visited) {
                    if (!temp.dfs())
                        return false;
                }
            }
        }
        return true;
    }
}