import sys

def radd(v1, v2): return (v1 + v2) % 100
def rsub(v1, v2): return (v1 - v2) % 100

idx = 50
clicks = 0
with open(sys.argv[1]) as fp:
	for line in fp:
		d = line[0]         # direction: L or R
		v = int(line[1:])   # value: int, could be large
		x = abs(v // 100)   # extra rotations
		r = v % 100         # fractional rotation
		
		if d == 'R':
			npos = radd(idx, v)
			if idx != 0 and npos < idx or npos == 0: clicks += 1
		else:
			npos = rsub(idx, v)
			if idx != 0 and npos > idx or npos == 0: clicks += 1
		clicks += x		
		idx = npos

print(clicks)

		