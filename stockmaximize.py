class StockMaximize(object):
	def solve(self,n,prices):
		total = 0
		l = len(prices)
		if l==0:
			return 0
		currentmin = prices[0]
		i = 1
		while i<n:
			if prices[i] < currentmin:
				currentmin = prices[i]
			else:
				total += prices[i]-currentmin
				currentmin = prices[i]
			i+=1
		return total
s = StockMaximize()
print `s.solve(3,[3,5,2])