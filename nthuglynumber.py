class Solution(object):
	def nthUglyNumber(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		d = {}
		stack = [1]
		p1,p2,p3 = 0,0,0
		i = 1
		ret = 1
		while i<n:
			u2,u3,u5 = [stack[p1]*2,stack[p2]*3,stack[p3]*5]
			cmin = min(u2,u3,u5)
			if cmin == u2:
				p1 +=1
			if cmin == u3:
				p2+=1
			if cmin == u5:
				p3+=1
			i+=1
			stack.append(cmin)
		return stack[-1]
s = Solution()
uglys = [1, 2, 3, 4, 5, 6, 8, 9, 10, 12]
for i,u in enumerate(uglys):
	# print s.nthUglyNumber(i+1),i+1,u
	assert(s.nthUglyNumber(i+1) == u)

