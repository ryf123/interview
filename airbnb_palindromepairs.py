class Solution(object):
	def isPalindrome(self,word):
		return word == word[::-1]
	def generatePairs(self,index1,index2):
		s = "{},{}".format(str(index1),str(index2))
		return s
	def palindromePairs(self, words):
		"""
		:type words: List[str]
		:rtype: List[List[int]]
		"""
		ret = []
		d = {}
		pairs = {}
		for i,word in enumerate(words):
			d[word] = i

		for word in words:
			for i in xrange(0,len(word)+1):
				first_rev = word[:i][::-1]
				
				if first_rev in d and self.isPalindrome(word[i:])  and d[first_rev] != d[word]:
					pair = self.generatePairs(d[word],d[first_rev])
					if pair not in pairs:
						ret.append([d[word],d[first_rev]])
						pairs[pair] = True

 				second_rev = word[i:][::-1]
 				
				if second_rev in d and self.isPalindrome(word[:i]) and d[second_rev] != d[word]:
					pair = self.generatePairs(d[second_rev],d[word])
					if pair not in pairs:
						ret.append([d[second_rev],d[word]])
						pairs[pair] = True
		return ret
s = Solution()
words = ["bat", "tab", "cat"]
print s.palindromePairs(words)