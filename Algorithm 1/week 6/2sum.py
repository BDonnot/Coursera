fname = "algo1_programming_prob_2sum.txt"
#fname = "2sum_test0.txt"
#fname = "2sum_test1.txt"
hashTable = set()
count = 0
test = set(range(-10000,10001))
with open(fname,"r") as f :
	l_count = 0
	for line in f :
		tmp = int(line)
		hashTable.add(tmp)
		test_cp = test.copy()
		for sum_2 in test_cp :
			if sum_2 != 2*tmp :
				if sum_2 - tmp in hashTable :
					count += 1
					test.remove(sum_2)
		l_count += 1
		if l_count % 1000 == 0 :
			print l_count,len(test)
print len(hashTable)

#
#
#for sum_2 in test :
#	for el in hashTable :
#		if sum_2!=2*el :
#			if sum_2 - el in hashTable :
#				count += 1
#				break
	#if count != 0 :
		#break
print count
			
