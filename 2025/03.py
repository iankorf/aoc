import sys

total = 0
with open(sys.argv[1]) as fp:
	for line in fp:
		seq = line.rstrip()
		i = 0
		built = ''
		while len(built) < 12:		
			mln = '0'
			for j in range(i, len(seq)):
				c = seq[j]
				if c > mln and j < len(seq) - 12 + len(built) +1:
					mln = c			
			built += mln
			i = seq.index(mln, i) + 1
		total += int(built)
print(total)