class Solution:
	# @param {string} s1
	# @param {string} s2
	# @param {string} s3
	# @return {boolean}
	def isInterleave(self, s1, s2, s3):
		l1 = len(s1)
		l2 = len(s2)
		p1 = 0
		p2 = 0
		for s in s3:
			if p1 < l1:
				c1 = s1[p1]
			else:
				c1 = ""
			if p2 < l2:
				c2 = s2[p2]
			else:
				c2 = ""
			print s,c1,c2,p1,p2
			if c1 == s:
				p1+=1
			elif c2==s:
				p2+=1
			else:
				return False
		return True
s = Solution()
s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"
print s.isInterleave(s1,s2,s3)

			
