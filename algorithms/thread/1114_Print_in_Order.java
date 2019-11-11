
class Foo {
    int print_order = 0;
    
    public Foo() {
    }

    public synchronized void first(Runnable printFirst) throws InterruptedException {
        printFirst.run();
        print_order = 1;
        notifyAll();
    }

    public synchronized void second(Runnable printSecond) throws InterruptedException {
        while (print_order != 1)
            wait();
        printSecond.run();
        print_order = 2;
        notifyAll();
    }

    public synchronized void third(Runnable printThird) throws InterruptedException {
        while (print_order != 2)
            wait();
        printThird.run();
    }
}