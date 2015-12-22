class Solution(object):
	def rotate(self, nums, k):
		l = len(nums)
		k = k%l
		self.nums = nums
		self.reverse2(0,l-k)
		self.reverse2(l-k,l)
		self.reverse2(0,l)
	# reverse the subarray
	def reverse(self,start,end):
		self.nums[start:end] = self.nums[start:end][::-1]
	def reverse2(self,start,end):
		end -=1
		while start < end:
			self.nums[start],self.nums[end] = self.nums[end],self.nums[start]
			start+=1
			end-=1
		print self.nums
s = Solution()
nums = [1,2,3,4,5,6,7]
for x in xrange(3,4):
	s.rotate(nums,x)
	print nums