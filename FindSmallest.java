List<Integer> find(Iterator<Integer> iterator,int k){
	PriorityQueue<Integer> pq = new PriorityQueue(new Comparator<Integer>(){
		public int compare(Integer i1,Integer i2){
			return i2 - i1;
		}
	});
	while(iterator.hasNext()){
		int num = iterator.next();
		pq.offer(num);
		if(pq.size() > k)
			pq.poll();
	}
	ArrayList<Integer> ret = new ArrayList();
	while(pq.size() > 0){
		ret.add(pq.poll());
	}
	return ret;
}