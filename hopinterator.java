/**. 
 * Implement an iterator that hops specified number of times and then returns the next
 * element after the hop. Note: the iterator always returns the first element as
 * it is, and starts hopping only after the first element.. 
 *
 * Examples:
 *
 * If the original iterator returns: [1, 2, 3, 4, 5] in order, then the hopping.
 * iterator will return [1, 3, 5] in order when the hop value is 1.
. more info on 1point3acres.com *
 * If the original iterator returns: [1, 2, 3, 4, 5] in order, then the hopping
 * iterator will return [1, 4] in order when the hop value is 2..
 *
 * If the original iterator returns: [1, 2, 3, 4, 5] in order, then the hopping.
 * iterator will return [1, 5] in order when the hop value is 3.
 * 
 * Methods expected to be implemented:
 *  
 * public class HoppingIterator<T> implements Iterator<T> {
 *                 public HoppingIterator(Iterator<T> iterator, int numHops) {...}
 *                 public boolean hasNext() {...}
 *                 public T next() {...}
 * }
 */
public class HoppingIterator<T> implements Iterator<T> {
	int numHops;
	Iterator<T> iterator;
	boolean start = true;
	boolean has_next_called = false;
	public HoppingIterator(Iterator<T> iterator, int numHops) {
		this.numHops = numHops;
		this.iterator = iterator;
	}
	public boolean hasNext() {
		has_next_called = true;
		if(start){
			start = false; // for the first element, do not hop
			return iterator.hasNext();
		}
		for(int i = 0;i<numHops;i++){
			if(iterator.hasNext())
				iterator.next();
			else
				return false;
		}
		return iterator.hasNext();
	}
	public T next() {
		if(!has_next_called)
			hasNext()
		has_next_called = false;
		return iterator.next();
	}
 }