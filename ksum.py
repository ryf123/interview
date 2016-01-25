class Solution:
	"""
	@param A: An integer array.
	@param k: A positive integer (k <= length(A))
	@param target: Integer
	@return a list of lists of integer 
	"""
	def kSumII(self, A, k, target):
		self.ret = []
		A.sort()
		self.dfs(A,k,target,[])
		return self.ret
	def dfs(self,A,k,target,path):
		# write your code here
		if target == 0 and k==0:
			print path
			return self.ret.append(path[:])
		elif target<0 or k<0:
			return
		for i,num in enumerate(A):
			path.append(num)
			self.dfs(A[i+1:],k-1,target-num,path)
			path.pop()
s = Solution()
print s.kSumII([1,2,3,4], 2, 5)