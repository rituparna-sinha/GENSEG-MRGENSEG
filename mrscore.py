import csv
cov = []
quant = []
coord = []
f = open('sortedcount1.csv','rb')
reader = csv.reader(f)
covmean = 0
quantmean = 0
flag = 0
f1 = open("gaps.txt" , "w")
for line in reader:
	if flag == 0:
		x = int(line[0])
		temp = x
		flag = 1
	if int(line[0]) != temp:
		diff = int(line[0]) - temp
		f1.write(str(temp - x) + ' ' + str(int(line[0])-1-x) + ' '+ str(diff) + '\n')
		for i in range(temp, int(line[0])):
			coord.append(i - x)
			cov.append(0)
			quant.append(0)
		temp = int(line[0])
	coord.append(int(line[0])-x)
	cov.append(int(line[1]))
	covmean += int(line[1])
	quant.append(int(line[2]))
	quantmean += int(line[2])
	temp += 1
f.close()
n = len(cov)
covmean = float(covmean)/n
quantmean = float(quantmean)/n
print covmean , quantmean
covsd = 0
quantsd = 0
for i in range(n):
	covsd = pow((cov[i]-covmean),2)
	quantsd = pow((quant[i]-quantmean),2)
covsd = covsd / n
quantsd = quantsd / n
covsd = pow(covsd,0.5)
quantsd = pow(quantsd,0.5)
print covsd, quantsd
f = open("basemrscore.txt", "w")

for i in range(n):
	covscore = (cov[i] - covmean)/covsd
	quantscore = (quant[i] - quantmean)/quantsd
	f.write(str(coord[i]) + ' ' + str(covscore) + ' ' + str(quantscore) + '\n')
f.close()
