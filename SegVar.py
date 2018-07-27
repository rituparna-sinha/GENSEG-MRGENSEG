def euc_dist(p1,p2):
	dist = pow((pow((p1[1]-p2[1]),2) + pow((p1[2]-p2[2]),2)),0.5)
	return abs(dist)

fname="basemrscore.txt"
zero=-6446.54082267
f = open(fname,"r")
data=[]
for line in f:
	temp=line.strip().split(' ')
	x,y,z=float(temp[0]),float(temp[1]),float(temp[2])
	data.append([x,y,z])
n = len(data)
A = [ 0 ] * n
print "data loaded"
minw = 1000
i = 0
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
						j += 1
						count += 1
						outcount = 0
						break
					q += 1
				if q == m:
					outcount += 1
					A[m] = -2
					if outcount == 1:
						track = j
						j += 1
						count += 1
					elif outcount <= 3:
						j += 1
						count += 1
					elif outcount > 3:
						for k in range(track,j+1): A[k] = 0
						count -= 3
						if count >= minw:
							j = m = track
							print i,j
							for k in range(i,j):
								if A[k] != -2:
									A[k] = 1
							i = m
							break
						else:
							j = m = track
							for k in range(i,j):
								if A[k] != -2:
									A[k] = -1
							i = m
							break
		else:
			j += 1
			count += 1
			outcount = 0
	if j == n:
		if count >= minw:
			print i,j
			for k in range(i,j):
				if A[k] != -2:
					A[k] = 1
		else:
			for k in range(i,j):
				if A[k] != -2:
					A[k] = -1
		break
