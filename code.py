import csv

inputfile = open('mmiw.csv', 'rU')
csv_reader = csv.DictReader(inputfile)

inputfile2 = open('code.csv', 'rU')
csv_reader2 = list(csv.DictReader(inputfile2))

#encoding verification
# with open('code.csv') as f:
#     for line in f:
#         print repr(line)
# data = open('code.csv', 'rb').read()
# print data.find('\x00')
# print data.count('\x00')

count = 0

for row in csv_reader:
	acc = row['acc']
	for row in csv_reader2:
		found = False
		if row['code'] == acc:
			print(row['long'])
			found = True
			break
	if not found:
		print '-'
		count +=1

print(count)