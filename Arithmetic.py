class Arithmetic(object):
	def solve(self,array):
		l = len(array)
		total = 0
		if l < 2:
			return 0
		diff = array[1] - array[0]
		i = 2
		currentlength = 2
		while i<l:
			currentdiff = array[i] - array[i-1]
			if currentdiff == diff:
				currentlength +=1
			else:
				if currentlength >=3:
					total += (currentlength-2)*(currentlength-1)/2
				diff = currentdiff
				currentlength = 2
			i+=1
		if currentlength >=3:
			total += (currentlength-2)*(currentlength-1)/2
		return total
a = Arithmetic()
assert(a.solve([-1,1,3,3,3,2,1,0]) == 5) 
assert(a.solve([1,2,3])==1)
assert(a.solve([1,2])==0)
