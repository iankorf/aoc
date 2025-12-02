import sys

with open(sys.argv[1]) as fp:
	line = next(fp)

uids = set()
for d in line.split(','):
	lo, hi = d.split('-')
	lo = int(lo)
	hi = int(hi)
	for i in range(lo, hi+1):
		strn = f'{i}'
		strl = len(strn)
		found = set()
		for j in range(1, strl):
			if strl % j != 0: continue
			strings = set()
			for k in range(0, strl - j + 1, j):
				strings.add(strn[k:k+j])
			if len(strings) == 1: found.add(i)
		if found: uids.add(i)
print(sum(uids))
