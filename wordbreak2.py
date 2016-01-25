class Solution:
	# @param s, a string
	# @param wordDict, a set<string>
	# @return a boolean
	def wordBreak(self, s, wordDict):
		def findsubstring(s,wordarray):
			if s in self.m:return self.m[s]
			ret = []
			l = len(s)
			i = l-1
			if s in wordarray:
				ret.append(s)
			while i>=0:
				if s[i:] in wordarray:
					res = findsubstring(s[:i],wordarray)
					for i,r in enumerate(res):
						res[i] += " "+s[i:]
					ret.append(res)
				i-=1
			self.m[s] = list(ret)
			return ret
		self.m = {}
		wordarray = {}
		for word in wordDict:
			wordarray[word] = True
		return findsubstring(s,wordarray)
s = Solution()
print s.wordBreak("catsanddog",["cat","sand","dog","cats","and"])