class Wrapper{
	int val;
	int array_index;
	Wrapper(int val,int array_index){
		this.val = val;
		this.array_index = array_index;
	}
}
int mindist(int[] A,int[] B,int[] C){
	int i=0,j=0,k=0;
	int min = Integer.MAX_VALUE;
	int la = A.length;
	int lb = B.length;
	int lc = C.length;
	PriorityQueue<Wrapper> pq = new PriorityQueue(new Comparator<Wrapper>(){
		public int compare(Wrapper w1,Wrapper w2){
			return w1.val - w2.val;
		}
	});
	pq.offer(new Wrapper(A[0],0));// assume array size > 0
	pq.offer(new Wrapper(B[0],1));
	pq.offer(new Wrapper(C[0],2));
	min = Math.max(Math.abs(C[k] - A[i]),Math.max(Math.abs(A[i] - B[j]),Math.abs(B[j] - C[k])))

	while(pq.size() > 0){
		Wrapper w = pq.poll();
		if(w.array_index == 0){
			i++;
			if(i<la){
				w.val = A[i];
				pq.offer(w);
			}
		}
		else if(w.array_index == 1){
			j++;
			if(j<lb){
				w.val = A[j];
				pq.offer(w);
			}
		}
		else if(w.array_index == 2){
			k++;
			if(k<lc){
				w.val = A[k];
				pq.offer(w);
			}
		}
		min = Math.min(min,Math.max(Math.abs(C[k] - A[i]),Math.max(Math.abs(A[i] - B[j]),Math.abs(B[j] - C[k]))) )

	}
	return min;
}