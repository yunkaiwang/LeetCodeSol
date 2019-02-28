// Java Iterator interface reference:
// https://docs.oracle.com/javase/8/docs/api/java/util/Iterator.html
class PeekingIterator implements Iterator<Integer> {
    Iterator<Integer> it;
    Integer lastInt;
    
	public PeekingIterator(Iterator<Integer> iterator) {
	    // initialize any member here.
	    it = iterator;
        lastInt = null;
	}

    // Returns the next element in the iteration without advancing the iterator.
	public Integer peek() {
        if (lastInt != null)
            return lastInt;
        lastInt = it.next();
        return lastInt;
	}

	// hasNext() and next() should behave the same as in the Iterator interface.
	// Override them if needed.
	@Override
	public Integer next() {
	    if (lastInt != null) {
            Integer temp = lastInt;
            lastInt = null;
            return temp;
        }
        return it.next();
	}

	@Override
	public boolean hasNext() {
	    return it.hasNext() || lastInt != null;
	}
}