class Solution:
	# @param {integer[]} nums
	# @return {integer}
	def maxSubArray(self, nums):
		if(len(nums)==0):
			return nums
		total = 0
		max = nums[0]
		start = nums[0]
		for i,num in enumerate(nums):
			total += num
			if total >= 0:
				if max < total:
					max = total
			else:
				if max < num:
					max = num 
				start = i
				total = 0
		# find the end index
		total = 0
		end = start
		for i,num in enumerate(nums[start+1:]):
			total += num
			if(total == max):
				end = i
				break
		print(max)
		print (start,end+start)
		return nums[start+1:end+1+start+1]
s = Solution()
print s.maxSubArray([-2,-1])