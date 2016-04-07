import heapq
class Solution(object):
	def nthSuperUglyNumber(self, n,primes):
		"""
		:type n: int
		:type primes: List[int]
		:rtype: int
		"""
		stack = [1]
		l = len(primes)
		assert(l!=0)
		pointers = l*[0]
		pq = []
		for i,prime in enumerate(primes):
			heapq.heappush(pq,(prime,i))
		while n>1:
			minnum,i = heapq.heappop(pq)
			stack.append(minnum)
			while len(pq) != 0:
				num,j =  heapq.heappop(pq)
				if num == minnum:
					pointers[j] += 1
					p = pointers[j]
					heapq.heappush(pq,(primes[j] * stack[p],j))
				else:
					heapq.heappush(pq,(num,j))
					break
			pointers[i] += 1
			p = pointers[i] 
			# print p,stack
			heapq.heappush(pq,(primes[i] * stack[p],i))
			
			n-=1
			# print stack,pq,pointers[0]
		return stack[-1]
primes = [2, 7, 13, 19]
count = 1
s = Solution()
for num in [1, 2, 4, 7, 8, 13, 14, 16, 19, 26, 28, 32]:
	print num
	assert(s.nthSuperUglyNumber(count,primes) == num)
	count+=1