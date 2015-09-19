class Solution:
	# @param {integer[]} nums
	# @return {integer[][]}
	def permuteUnique(self, nums):
		results = []
		def permutate(excludenums):
			excludenums.sort()
			ra = []
			l = len(excludenums)
			if l == 1:
				return [excludenums]
			for i,num in enumerate(excludenums):
				if i > 0:
					if excludenums[i] == excludenums[i-1]:
						continue
				# print (i,nums[:i],nums[i+1:])
				rets =permutate(excludenums[:i]+excludenums[i+1:])
				#print rets
				temp =  [[num] + ret for ret in rets]
				if temp not in ra:
					ra += temp 
			return ra
		results = permutate(nums)
		return results
s = Solution()
ret = s.permuteUnique([1,0,-1,0])
print ret
