class Solution(object):
	def subsetsWithDup(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[List[int]]
		"""
		def subset(subnums,sol):
			if not len(subnums):
				return
			for i,num in enumerate(subnums):
				if i>0:
					if num == subnums[i-1]:
						continue
				sol.append(num)
				if len(sol):
					self.ret.append(sol[:])
				subset(subnums[i+1:],sol)
				sol.pop()

		self.ret = []
		nums.sort()
		subset(nums,[])
		# self.ret =  [x.split("#") for x in self.ret]
		# return [map(int,x) for x in self.ret] +[[]]
		return self.ret+[[]]
s = Solution()
nums = [1,1,1,1]
print s.subsetsWithDup(nums)

