import json
import sys



total = 0
with open(sys.argv[1]) as fp:
	for line in fp:
		seq = line.rstrip()
