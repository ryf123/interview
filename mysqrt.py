class Solution(object):
	def mySqrt(self, x):
		"""
		:type x: int
		:rtype: int
		"""
		def findsqrt(start,end,target):

			if start*start <= target and end*end >= target:
				mid = (start+end)/2
				sqrt = mid*mid
				if sqrt == target:
					return mid
				elif sqrt > target:
					return findsqrt(start,mid-1,target)
				else:
					return findsqrt(mid+1,end,target)
				return 0
			elif end*end < target:
				return end
			else:
				return start-1
		return findsqrt(1,x,x)
s = Solution()
for i in xrange(50):
	print i,s.mySqrt(i)