class Solution:
	# @param {string} s
	# @param {string[]} words
	# @return {integer[]}
	def findSubstring(self, s, words):
		ret = []
		if len(words) == 0:
			return ret
		wl = len(words[0]) # len of each word, since they are the same lenght
		nw = len(words) # number of words
		csl = nw*wl # concatenated string lenght = #words*wordlenght 
		sl = len(s)
		if(sl < csl):
			return ret
		d = {}
		for word in words:
			if word not in d:
				d[word] = 1
			else:
				d[word] +=1
		
		i = 0
		while( i < wl):
			left = i
			tempdict  = {}
			counter = 0
			for j in xrange(i,sl-wl+1,wl):
				substring = s[j: j+wl]
				if substring in d:
					if substring in tempdict:
						tempdict[substring] +=1
					else:
						tempdict[substring] = 1
					counter +=1
					while tempdict[substring] > d[substring]:
						tempdict[s[left:left+wl]] -=1
						left += wl
						counter -=1
					if counter == nw:
						ret.append(left)
				else:
					left = j+wl
					counter = 0
					tempdict = {}
			i+=1
		return ret

sl = Solution()
s ="barfoothefoobarman"
words = ["foo","bar"]
# s = "barfoofoobarthefoobarman"
# words = ["bar","foo","the"]
print sl.findSubstring(s,words)