def isBadVersion(n):
	if n >= 2:
		return True
	else:
		return False
class Solution(object):

	def firstBadVersion(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		l = n
		start,end = 1,l
		mid = (start+end)/2
		while not (isBadVersion(mid) and isBadVersion(mid-1) == False):
			# if start==end and start == 0:
			# 	return 0
			# print start,end,mid
			if isBadVersion(mid):
				end = mid-1
			else:
				start = mid+1
			mid = (start+end)/2
			if mid == 1:
				if isBadVersion(mid):
					return 1
				else:
					return -1
		return mid
s = Solution()
print s.firstBadVersion(3)

