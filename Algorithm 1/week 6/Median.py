import heapq
fname = "Median.txt"
#fname = "test.txt"
#fname = "test1.txt"
h_min = []
h_max = []
res = 0
with open(fname,"r") as f :
	count = 0
	tmp1,tmp2 = int(f.readline()),int(f.readline())
	heapq.heappush(h_min,-min([tmp1,tmp2]) )
	heapq.heappush(h_max,max([tmp1,tmp2]))
	#print (h_min) , (h_max)
	med = min([tmp1,tmp2]) 
	res = tmp1+tmp2
	res %= 10000
	for line in f :	
		tmp = int(line)
		#print tmp
		if tmp > med :
			heapq.heappush(h_max,tmp)
			#print tmp,med,"max"
		else :
			heapq.heappush(h_min,-tmp)
			#print tmp,med,"min"

		if len(h_min) - len(h_max) >= 2 :
			tmp = -heapq.heappop(h_min)
			heapq.heappush(h_max,tmp)
		elif len(h_min) - len(h_max) <= -1 :
			tmp = heapq.heappop(h_max)
			heapq.heappush(h_min,-tmp)			
		med = -min(h_min)
		res = res+med
		#res %= 10000
		#print med
		#count += 1
		#if count >= 10 :
			#break

#print len(h_min),len(h_max)
#print (h_min) , (h_max)
print res
