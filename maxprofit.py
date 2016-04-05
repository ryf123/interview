class Solution:
	# @param {integer[]} prices
	# @return {integer}
	def maxProfit(self, prices):
		n = len(prices)
		if n==0:
			return 0
		current_min = prices[0]
		ret = 0
		for i in xrange(1,n):
			ret = max(prices[i]-current_min,ret)
			current_min = min(prices[i],current_min)
		return ret
s = Solution()
prices = [6,1,3,2,4,7]
# prices = [1,2,4]
print s.maxProfit(prices)