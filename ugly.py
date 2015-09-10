class Solution:
	# @param {integer} num
	# @return {boolean}
	def isUgly(self, num):
		if num <=0:
			return False
		uglys = [2,3,5]
		for ugly in uglys:
			while num%ugly == 0:
				num = num/ugly
		return True if num==1 else False
s =Solution()
print s.isUgly(1)
