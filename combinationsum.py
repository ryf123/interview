class Solution:
	# @param {integer[]} candidates
	# @param {integer} target
	# @return {integer[][]}
	def combinationSum3(self, k, target):
		def findcombo(start,curtarget,sol,remain):
			if curtarget ==0:
				if remain == 0:
					self.ret.append(sol[:])
				return
			if remain == 0:
				return
			for i in range(start,end):
				if i> start:
					if candidates[i] == candidates[i-1]:
						continue
				if candidates[i] <= curtarget:
					sol.append(candidates[i])
					findcombo(i+1,curtarget-candidates[i],sol,remain-1)
					sol.pop(-1)
		candidates = range(1,10)
		end = 9
		self.ret = []
		findcombo(0,target,[],k)
		return self.ret
s = Solution()
print s.combinationSum3(3,9)