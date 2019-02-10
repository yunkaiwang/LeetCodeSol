class Solution {
    public int evalRPN(String[] tokens) {
        Stack<Integer> stack = new Stack<Integer>();
        for (String s: tokens) {
            if (s.equals("+") || s.equals("-") || s.equals("*") || s.equals("/")) {
                int op1 = stack.pop();
                int op2 = stack.pop();
                if (s.equals("+"))
                    stack.push(op1 + op2);
                else if (s.equals("-"))
                    stack.push(op2 - op1);
                else if (s.equals("*"))
                    stack.push(op1 * op2);
                else
                    stack.push((int) op2 / op1);
            } else
                stack.push(Integer.parseInt(s));
        }
        return stack.pop();
    }
}