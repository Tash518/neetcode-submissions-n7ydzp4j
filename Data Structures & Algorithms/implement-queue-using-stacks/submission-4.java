class MyQueue {
    private Stack<Integer> stackin;
    private Stack<Integer> stackout;

    public MyQueue() {
        stackin = new Stack<>();
        stackout = new Stack<>();
        
    }
    
    public void push(int x) {
        stackin.push(x);
        
    }
    
    public int pop() {
        if(stackout.isEmpty()){
            while(!stackin.isEmpty()){
                stackout.push(stackin.pop());
            }
        }
        return stackout.pop();
    }
    
    public int peek() {
        if(stackout.isEmpty()){
            while(!stackin.isEmpty()){
                stackout.push(stackin.pop());
            }
        }
        return stackout.peek();    
    }
    
    public boolean empty() {
        return (stackin.isEmpty() && stackout.isEmpty());
    }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue obj = new MyQueue();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.peek();
 * boolean param_4 = obj.empty();
 */