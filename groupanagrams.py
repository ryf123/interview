class Solution:
	# @param {string[]} strs
	# @return {string[][]}
	def groupAnagrams(self, strs):
		ret = []
		stringdict = {}
		for s  in strs:
			anagram = "".join(sorted(s))
			print anagram
			if anagram not in stringdict:
				stringdict[anagram] = [s]
			else:
				stringdict[anagram].append(s)
		for key in stringdict:
			ret.append(sorted(stringdict[key]))
		return ret
s = Solution()
print s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])