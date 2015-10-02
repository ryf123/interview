class Solution(object):
	def singleNumber(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		i,l = 1,len(nums)
		totalxor = nums[0]
		while i<l:
			totalxor ^= nums[i]
			i+=1
		lastbitnum = 1
		while lastbitnum&totalxor == 0:
			lastbitnum<<=1
		total1,total2 = None,None
		for num in nums:
			if num&lastbitnum:
				if total1 != None:
					total1 ^= num
				else:
					total1 = num
			else:
				if total2 != None:
					total2 ^=num
				else:
					total2 = num
		return [total1,total2]
s = Solution()
nums = [1, 2, 1, 3, 2, 5]
print s.singleNumber(nums)
