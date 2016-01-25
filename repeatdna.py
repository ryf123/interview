from collections import Counter
class Solution:
	# @param {string} s
	# @return {string[]}
	def findRepeatedDnaSequences(self, s):
		l = len(s)
		d = Counter()
		ret = []
		for i in range(0,l-9):
			d[s[i:i+10]] +=1
		for key in d:
			if d[key] >1:
				ret.append(key)
		return ret
s = Solution()
st = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
print s.findRepeatedDnaSequences(st)