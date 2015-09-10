class Solution:
	# @param {string} s
	# @return {string[]}
	def findRepeatedDnaSequences(self, s):
		l = len(s)
		if l <10:
			return []
		passed = []
		ret = []
		for i in range(0,l-9):
			passed.append(s[i:i+10])
		passed.sort()
		for i,dna in enumerate(passed):
			if i == l-10:
				continue
			if dna == passed[i+1]:
				if dna not in ret:
					ret.append(dna)
		return ret
s = Solution()
st = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
print s.findRepeatedDnaSequences(st)