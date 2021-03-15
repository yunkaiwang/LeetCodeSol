class MyQueue {
    /**
     * amortized O(1) per operation
     */
    Stack<Integer> s1;
    Stack<Integer> s2;
    int top;
    
    /** Initialize your data structure here. */
    public MyQueue() {
        s1 = new Stack<Integer>();
        s2 = new Stack<Integer>();
        top = -1;
    }
    
    /** Push element x to the back of queue. */
    public void push(int x) {
        if (s1.empty())
            top = x;
        s1.push(x);
    }
    
    /** Removes the element from in front of queue and returns that element. */
    public int pop() {
        if (s2.empty()) {
            while (!s1.empty())
                s2.push(s1.pop());
        }
        return s2.pop();
    }
    
    /** Get the front element. */
    public int peek() {
        if (!s2.empty())
            return s2.peek();
        return top;
    }
    
    /** Returns whether the queue is empty. */
    public boolean empty() {
        return s1.empty() && s2.empty();
    }
}

class MyQueue {
    /**
     * O(n) push, O(1) pop
     */
    Stack<Integer> s;
    
    /** Initialize your data structure here. */
    public MyQueue() {
        this.s = new Stack<Integer>();
    }
    
    /** Push element x to the back of queue. */
    public void push(int x) {
        Stack<Integer> newS = new Stack<Integer>();
        while (!s.empty())
            newS.push(s.pop());
        s.push(x);
        while (!newS.empty())
            s.push(newS.pop());
    }
    
    /** Removes the element from in front of queue and returns that element. */
    public int pop() {
        return s.pop();
    }
    
    /** Get the front element. */
    public int peek() {
        return s.peek();
    }
    
    /** Returns whether the queue is empty. */
    public boolean empty() {
        return s.empty();
    }
}


 