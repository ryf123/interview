class Solution(object):
	def swap(self,i,j):
		temp = self.nums[i]
		self.nums[i] = self.nums[j]
		self.nums[j] = temp
	def wiggleSort(self, nums):
		"""
		:type nums: List[int]
		:rtype: void Do not return anything, modify nums in-place instead.
		"""
		self.nums = nums
		l = len(nums)
		nums.sort()
		half = l/2
		half = half + 0 if l%2 == 0 else half + 1
		smaller = nums[:half]
		larger = nums[half:]
		ret = []
		flag = True
		while len(smaller)>0 or len(larger) >0:
			if len(smaller) > 0 and flag:
				ret.append(smaller.pop())
			elif len(larger)>0 and not flag:
				ret.append(larger.pop())
			flag = not flag
		for i in xrange(len(nums)):
			nums[i] = ret[i]
	def wiggleSort1(self, nums):
	    nums.sort()
	    half = len(nums[::2])
	    nums[::2], nums[1::2] = nums[:half][::-1], nums[half:][::-1]
s = Solution()
nums = [1,2,3,4,5]
# nums = [1,2,3]
# nums = [1,5,1,1,6,4]
# nums = [1,3,2,2,3,1]
# nums = [1,1,2,2,1]
# nums = [5,3,1,2,6,7,8,5,5]
# nums = [4,5,5,6]
s.wiggleSort(nums)
print nums