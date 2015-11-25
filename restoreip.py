class Solution(object):
	def restoreIpAddresses(self, s):
		"""
		:type s: str
		:rtype: List[str]
		"""
		pattern = "^\d$|^[1-9]\d$|^1\d\d$|^2[0-4][0-9]$|^25[0-5]$"
				  # "^\d$|^[1-9]\d$|^1\d\d$|^2[0-5][0-5]$"
		def match(ips):
			if len(ips) >1 and ips[0] == "0":
				return False
			if len(ips) >3:
				return False
			num = int(ips)
			return True if num>=0 and num<=255 else False
		def breakip(ips,sol):
			# print sol
			if len(sol) > 4:
				return False
			if len(ips) == 0 and len(sol) ==4:
				# print sol
				self.ret.append(".".join(sol))
			for i in xrange(len(ips)):
				if match(ips[:i+1]):
					sol.append(ips[:i+1])
					# print len(sol)
					breakip(ips[i+1:],sol)
					sol.pop()
				if i == 2:
					break
			return False
		self.ret = []
		breakip(s,[])
		return self.ret
s = Solution()
# print s.restoreIpAddresses("172162541")
print s.restoreIpAddresses("001001")
