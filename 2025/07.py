import sys

mat = []
with open(sys.argv[1]) as fp:
	for line in fp:
		line = line.rstrip()
		mat.append(line)

beams = set()
start = mat[0].index('S')
beams.add(start)
total = 0
for row in mat[1:]:
	if '^' not in row: continue
	splitters = set()
	for i, c in enumerate(row):
		if c == '^': splitters.add(i)
	new_beams = set()
	for beam in beams & splitters:
		new_beams.add(beam -1)
		new_beams.add(beam +1)
		total += 1
	old_beams = beams - new_beams - splitters
	beams = new_beams | old_beams
print(total)
