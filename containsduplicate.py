class Solution:
	# @param {integer[]} nums
	# @param {integer} k
	# @param {integer} t
	# @return {boolean}
	def containsNearbyAlmostDuplicate(self, nums, k, t):
		if k == 0:
			if t == 0:
				return True
			return False
		l = len(nums)
		if l == 0:
			return False
		if k > l:
			return False
		for i in range(0,l-k):
			num = nums[i]
			subnum = nums[i+1:i+k+1]
			subnummin = min(subnum)
			subnummax = max(subnum)
			print subnum,nums[i]
			# if abs(nums[i] - subnummin) <= t or abs(subnummax - nums[i]) <=t:
				
			#     return True
			for j in range(i+1,i+k+1):
				if abs(num - nums[j]) <=t:
					return True
		print l-k
		print nums[l-k:]
		if max(nums[l-k:]) - min(nums[l-k:]) <= t:
			return True
		return False
s = Solution()
print s.containsNearbyAlmostDuplicate([3,6,8],3,2)