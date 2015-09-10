class Solution(object):
	def compareVersion(self, version1, version2):
		"""
		:type version1: str
		:type version2: str
		:rtype: int
		"""
		v1 = version1.split(".")
		v2 = version2.split(".")
		l = min(len(v1),len(v2))
		for i in xrange(l):
			iv1,iv2 =  int(v1[i]),int(v2[i])
			if iv1 > iv2:
				return 1
			elif iv1 < iv2:
				return -1
		# print i,v2,len(v1),len(v2)
		if len(v1) == len(v2):
			return 0
		else:
			if len(v1) > len(v2):
				while i+1 < len(v1):
					i+=1
					if int(v1[i]) != 0:
						return 1
					
			else:
				while i+1 < len(v2):
					i+=1
					if int(v2[i]) != 0:
						# print v2[i]
						return -1
			return 0
s = Solution()
print s.compareVersion("0.0.1.000","0.0.1")                
