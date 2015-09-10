def fab(n):
	if n == 0:
		return 1
	else:
		return n*fab(n-1)
for x in xrange(20):
	ret = str(fab(x*10))
	i = len(ret)
	while (ret[i-1]) == "0":
		i-=1
	print x*10,len(ret)-i,ret
