import itertools
import sys


total = 0
with open(sys.argv[1]) as fp:
	for line in fp:
		s = line.rstrip()
		
		# create data structure of counts of each numeral to the right
		# that still leaves room to make 12 chars
		right = []
		for i in range(len(s) -11):
			counts = {}
			for n, c in enumerate('123456789'):
				last_idx = s.rindex(c)
				if last_idx == -1: continue
				x = s[i:last_idx+1]
				y = x.count(c)
#				print(c, y, x)
				if y > 0: counts[c] = y
			right.append(counts)

		# build better strings than last
		maxs = s[-12]
		build = ''
		pos = 0
		while len(build) != 12:
			maxn = 0
			for n, c in enumerate('987654321'):
				if c not in right[pos]: continue
				
		
		
			print(right[pos])
			n = max(right[pos].keys())
			pos = s[pos:].find(n)
			
			
			build += n
			print(build, pos)
			
		
		sys.exit()