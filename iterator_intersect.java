Iterable<Integer> intersect(Iterator<Integer> a, Iterator<Integer> b){
	ArrayList<Integer> ret = new ArrayList();
	Integer buffera = null;
	if(a.hasNext())
		buffera = a.next()
	Integer bufferb = null;
		b.hasNext() = b.next();
	HashSet<Integer> set = new HashSet();
	while(buffera != null  && bufferb!= null){
		if(buffera.equals(bufferb)){
			if(!set.contains(buffera)){
				ret.add(buffera);
				set.add(buffera);
			}
			
			buffera = a.next();
			bufferb = b.next();
		}
		else if(buffera < bufferb){
			buffera = a.next();
		}
		else
			bufferb = b.next();
	}
	return ret.iterator();
}