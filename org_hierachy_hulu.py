class Org_Hierachy:
	def read_input(self,s):
		self.manage = {}
		self.profile = {}
		self.CEO = ""
		for row in s.split("--"):
			[name,manager,title,year] = row.split(",")
			self.profile[name] = {}
			self.profile[name]["title"] = title
			self.profile[name]["year"] = year
			if self.isCEO(manager):
				self.CEO = name
			else:
				if manager not in self.manage:
					self.manage[manager] = [name]
				else:
					self.manage[manager].append(name)

	def isCEO(self,name):
		'''
			if someone is CEO, will start from CEO
		'''
		return name == "NULL"

	def process(self,s):
		self.read_input(s)
		return self.dfs(self.CEO,0)

	def Print(self,name,print_level):
		return "-"*print_level + name + " ({}) ".format(self.profile[name]["title"]) + str(self.profile[name]["year"]) + "\n"

	def dfs(self,name,print_level):
		'''
			print hierachy using dfs
		'''
		content = self.Print(name,print_level)
		if name in self.manage:
			for child in sorted(self.manage[name]):
				content += self.dfs(child,print_level+1)
		return content

def saveFile(content,filename="org_chart.out"):
	with open (filename,'w') as f:
		f.write(content)

def main(filename):
	o = ""
	with open (filename,'r') as f:
		lines = f.readlines()
		if len(lines) > 0:
			n = int(lines[0])
			assert(n == len(lines) - 1)
			oh = Org_Hierachy()
			for i in xrange(1,n+1):
				o +=  "Case #{}\n".format(str(i))
				o += oh.process(lines[i].strip())
	saveFile(o)

if __name__ == '__main__':
	filename = "org_chart.in"
	main(filename)