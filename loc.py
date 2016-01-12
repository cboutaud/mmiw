import csv

inputfile = open('mmiw.csv', 'rU')
csv_reader = csv.DictReader(inputfile)

inputfile2 = open('census.csv', 'rU')
csv_reader2 = list(csv.DictReader(inputfile2))

#encoding verification
# with open('census.csv') as f:
#     for line in f:
#         print repr(line)
# data = open('census.csv', 'rb').read()
# print data.find('\x00')
# print data.count('\x00')

count = 0
countthis = 0

for row in csv_reader:
	loc = row['loc']
	if loc == "Edmonton":
		countthis +=1
	for row in csv_reader2:
		found = False
		if row['Geographic name'] == loc:
			print(row['Geographic type'])
			found = True
			break
	if not found:
		print '-'
		count +=1

print(count)
print(countthis)