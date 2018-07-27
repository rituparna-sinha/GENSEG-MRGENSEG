import pysam
import csv
over=0
samfile = pysam.AlignmentFile("sorted.bam", "rb" )
for pileupcolumn in samfile.pileup("22", 16050046 , 51244556):
    over=pileupcolumn.n
    if over>0:
        break
start=pileupcolumn.pos

with open('test1.csv','w') as f:
    thewriter=csv.writer(f)
    for pileupcolumn in samfile.pileup("22", start, 51244556):
    	a=t=g=c=0
    
    	for pileupread in pileupcolumn.pileups:
        	if not pileupread.is_del and not pileupread.is_refskip:
        	    v=pileupread.alignment.query_sequence[pileupread.query_position]
        	    if v=='A':
        	        a=a+1  
        	    elif v=='T':
        	        t=t+1
        	    elif v=='G':
        	        g=g+1
        	    else:
        	        c=c+1
	m=max(a,t,g,c)
        thewriter.writerow([pileupcolumn.pos,pileupcolumn.n,m])


