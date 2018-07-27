#!/usr/bin/python

import sys

def euc_dist(p1,p2):
	dist = pow((pow((p1[1]-p2[1]),2) + pow((p1[2]-p2[2]),2)),0.5)
	return abs(dist)

data=[]
zero=-6446.54082267
for line in sys.stdin:
	l = line.strip().split(" ")
	x,y,z = l
	data.append([int(x), float(y), float(z)])
n = len(data)
A = [0] * n
i = 0
minw = 1000
while data[i][1] == zero: 
	i += 1
while i < n:
	d = 0
	ct = 0
	prev = data[i]
	for k in range(i+1,i+minw+1):
		if k < n:
			if data[k][1] != zero:
				d += euc_dist(prev, data[k])
				ct += 1
				prev = data[k]
		else:
			break
	if ct != 0:
		d /= ct
	count = 1
	outcount = 0
	j = i + 1
	while j < n:
		if data[j][1] != zero:
			if euc_dist(data[i], data[j]) <= d:
				j += 1
				count += 1
				outcount = 0
			else:
				m = j
				q = i + 1
				while q < m:
					if A[q] != -2 and data[q][1] != zero and euc_dist(data[q], data[m]) <= d:
						count += 1
						outcount = 0
						j += 1
						break
					q += 1
				if q == m:
					outcount += 1
					A[j] = -2
					if outcount == 1:
						track = j
						count += 1
						j += 1
					elif outcount <= 3:
						count += 1
						j += 1
					elif outcount > 3 and i == 0:
						for k in range(track,j+1): A[k] = 0
						j = track
						for k in range(i,j):
							if A[k] != -2:
								A[k] = 1
						a=str(data[0][0]) + " " + str(data[0][1]) + " " + str(data[0][2])
						for k in range(1,j):
							a = a + "," +str(data[k][0]) + " " + str(data[k][1]) + " " + str(data[k][2])
						print "{0},B\t{1}".format(data[i][0],a)
						i = track
						break
					else:
						count -= 3
						if count >= minw:
							for k in range(track,j+1): A[k] = 0
							j = track
							for k in range(i,j):
								if A[k] != -2:
									A[k] = 1
								else:
									print "{0},N\t{1}".format(data[i][0],data[k][0])
							print "{0},Y\t{1}".format(data[i][0],data[j-1][0])
							i = track
							break
						else:
							for k in range(track,j+1): A[k] = 0
							j = track
							for k in range(i,j):
								if A[k] != -2:
									A[k] = 1
							i = track
							break
		else:
			j += 1
			count += 1
			outcount = 0
	if j == n:
		for k in range(i,j):
			if A[k] != -2:
				A[k] = 1
		a=str(data[i][0]) + " " + str(data[i][1]) + " " + str(data[i][2])
		for k in range(i+1,j):
			a = a + "," +str(data[k][0]) + " " + str(data[k][1]) + " " + str(data[k][2])
		print "{0},B\t{1}".format(data[i][0],a)
		break
