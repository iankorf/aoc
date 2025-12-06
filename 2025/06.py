import sys

mat = []
opline = None
with open(sys.argv[1]) as fp:
	for line in fp:
		if line.startswith('*') or line.startswith('+'):
			opline = line
		else:
			mat.append(line)
opline += ' ' # it's shorter by one

total = 0
for i in range(len(opline)):
	if opline[i] == ' ': continue

	nextop = len(opline)
	for j in range(i+1, len(opline)):
		if opline[j] == ' ': continue
		nextop = j
		break

	vals = []
	for k in range(i, nextop-1):
		t = ''
		for j in range(len(mat)):
			t += mat[j][k]
		vals.append(t)
	ivals = [int(v) for v in vals]
	
	if opline[i] == '+':
		st = sum(ivals)
	else:
		st = 1
		for v in ivals: st *= v
	total += st
print(total)
