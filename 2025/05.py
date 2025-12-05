import sys

def find_overlaps(feats):
	for i in range(len(feats)):
		for j in range(i+1, len(feats)):
			a, b = feats[i]
			c, d = feats[j]
			if a >= c and a <= d: return i, j
			if b >= c and b <= d: return i, j
			if c >= a and c <= b: return i, j
			if d >= a and d <= b: return i, j
	return None, None

features = []
with open(sys.argv[1]) as fp:
	for line in fp:
		if line == '\n': break
		beg, end = line.split('-')
		beg = int(beg)
		end = int(end)
		if end < beg: sys.exit('you bastards')
		features.append( (beg,end) )

while True:
	i, j = find_overlaps(features)
	if i is None: break
	b1, e1 = features[i]
	b2, e2 = features[j]
	beg = min(b1, b2)
	end = max(e1, e2)
	features[i] = (beg, end)
	features.pop(j)

total = 0
for beg, end in features: total += end - beg + 1
print(total)
