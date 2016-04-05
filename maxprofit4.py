class Solution(object):
	# do as many as trade as possible
	def infinitTransaction(self,prices):
		l = len(prices)
		profit = 0
		for i in xrange(1,l):
			if prices[i] > prices[i-1]:
				profit += prices[i] - prices[i-1]
		return profit
	def maxProfit(self, k, prices):
		l = len(prices)
		if k > l/2:
			return self.infinitTransaction(prices)
		previous_k_profit = [0] * l # the max profit made in k-1 transcations, initially it's all 0
		for i in xrange(k):
			maxDP_price = 0 - prices[0]
			temp_previous_k = [0]
			maxProfit = 0
			for j in xrange(1,l):
				# max profit is max(dp[i-1][j],prices[j] + dp[jj] - prices[jj] for jj in range(1,j))
				# so each loop we get by max dp[jj] - prices[jj] in maxDP_price
				maxProfit = max(previous_k_profit[j],prices[j] + maxDP_price,maxProfit)
				maxDP_price = max(previous_k_profit[j] - prices[j],maxDP_price)
				# print [i,j],maxProfit,maxDP_price
				temp_previous_k.append(maxProfit)
			previous_k_profit = temp_previous_k
			# print previous_k_profit
		return previous_k_profit[-1]

s = Solution()
k,prices = 1,[10,20]
k,prices = 2,[1,2,-1,3]
k,prices = 2,[2,4,1]
print s.maxProfit(k,prices)

