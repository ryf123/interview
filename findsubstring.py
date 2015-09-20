class Solution:
	# @param {string} s
	# @param {string[]} words
	# @return {integer[]}
	def findSubstring(self, s, words):
		ret = []
		nw = len(words)
		if nw == 0:
			return ret
		wl = len(words[0])
		i,l = 0,len(s)
		wordsdict = {}
		hashsumtotal = 0
		for word in words:
			if word in wordsdict:
				wordsdict[word] +=1
			else:
				wordsdict[word] = 1
			hashsumtotal += hash(word)
			# print hash(word)
		hashtable = [0]*l
		for i,c in enumerate(s):
			hashtable[i] = hash(s[i:i+wl])
		ret = []
		# print hashtable
		i=0
		while i<l-nw*wl+1:
			# print hashtable[i:i+nw*wl:wl]
			if sum(hashtable[i:i+nw*wl:wl]) != hashsumtotal:
				i+=1
				continue
			j=i
			tempdict = wordsdict.copy()
			wordcount = 0
			while j+wl <= l and wordcount<nw and s[j:j+wl] in wordsdict:

				subword = s[j:j+wl]
				# print subword
				wordcount +=1
				if subword in tempdict:
					tempdict[subword] -=1
					if tempdict[subword] < 0:
						break
				if wordcount == nw:
					ret.append(i)
					break
				j+=wl
				# print s[j:j+wl],tempdict
			i+=1
			# print wordcount
		return ret
sl = Solution()
s = "barfoothefoobarman"
words = ["foo", "bar"]
# print sl.findSubstring(s,words)
# print len(s),len(words)* len(words[0])
# i = 0
# d = {}
# while i< len(words):
# 	# print words[i]
# 	if words[i] in d:
# 		d[words[i]] +=1
# 	else:
# 		d[words[i]] =1
# 	i+=1
# print d
s,words = "wordgoodgoodgoodbestword",["word","good","best","good"]
print sl.findSubstring(s,words)