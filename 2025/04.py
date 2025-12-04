import sys

dirs = [
	(-1,-1), (-1,0), (-1,+1),
	( 0,-1),         ( 0,+1),
	(+1,-1), (+1,0), (+1,+1),
]

with open(sys.argv[1]) as fp:
	grid = []
	for line in fp:
		row = list(line.rstrip())
		grid.append(row)

removed = 0
last = -1
while removed != last:
	found = []
	for y in range(len(grid)):
		for x in range(len(grid[y])):
			if grid[y][x] != '@': continue
			n = 0 # neighbors
			for dy, dx in dirs:
				sy = y + dy
				sx = x + dx
				if sy < 0: continue
				if sx < 0: continue
				if sy >= len(grid): continue
				if sx >= len(grid[y]): continue
				if grid[sy][sx] == '@': n += 1
			if n <= 3: found.append( (y, x) )

	last = removed
	removed += len(found)

	g2 = [row for row in grid]
	for y, x in found: g2[y][x] = '.'
	grid = g2
		
print(removed)