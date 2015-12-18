class Solution(object):
	def nthSuperUglyNumber(self, n, primes):
		"""
		:type n: int
		:type primes: List[int]
		:rtype: int
		"""
		stack = [1]
		l = len(primes)
		assert(l!=0)
		pointers = l*[0]
		while n>1:
			minnum = stack[pointers[0]]*primes[0]
			for i,p in enumerate(pointers):
				minnum = min(stack[p]*primes[i],minnum)
			for i,p in enumerate(pointers):
				if minnum == stack[p]*primes[i]:
					pointers[i] +=1
			stack.append(minnum)
			n-=1
		return stack[-1]
primes = [2, 7, 13, 19]
count = 1
s = Solution()
for num in [1, 2, 4, 7, 8, 13, 14, 16, 19, 26, 28, 32]:
	assert(s.nthSuperUglyNumber(count,primes) == num)
	count+=1