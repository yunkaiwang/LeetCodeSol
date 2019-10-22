import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

class Solution {
    public List<Integer> powerfulIntegers(int x, int y, int bound) {
        Set<Integer> ans = new HashSet<Integer>();
        if (x>y) {
            int temp = y;
            y = x;
            x = temp;
        }
        int j = 0;
        int y_j = 1;
        while (y_j < bound) {
            loop(x, y, 0, 1, y_j, bound, ans);
            y_j *= y;
            if (y_j == 1) 
                break;
        }
        
        return new ArrayList(ans);
    }
    
    public void loop(int x, int y, int i, int x_i, int y_j, int bound, Set<Integer> currentList) {
        if (x_i + y_j <= bound) {
            currentList.add(x_i + y_j);
            if (x != 1)
                loop(x, y, i+1, x_i * x, y_j, bound, currentList);
        }
    }
}