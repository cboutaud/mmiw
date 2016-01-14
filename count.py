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
iri = 0
cy = 0
v = 0
dm = 0
c = 0
nv = 0
t = 0
sm = 0
rgm = 0
vl = 0
cv = 0
tp = 0
rm = 0
ham = 0
rv = 0
mu = 0
settype = 0
no = 0
unknown = 0

for row in csv_reader:
	typeof = row['type']
	if typeof == 'IRI':
		iri += 1
	if typeof == "CY":
		cy += 1
	if typeof == "V":
		v += 1
	if typeof == "DM":
		dm += 1
	if typeof == "C":
		c += 1
	if typeof == "NV":
		nv += 1
	if typeof == "T":
		t += 1
	if typeof == "SM":
		sm += 1
	if typeof == "RGM":
		rgm += 1
	if typeof == "VL":
		vl += 1
	if typeof == "CV":
		cv += 1
	if typeof == "TP":
		tp += 1
	if typeof == "RM":
		rm += 1
	if typeof == "HAM":
		ham += 1
	if typeof == "RV":
		rv += 1
	if typeof == "MU":
		mu += 1
	if typeof == "SET":
		settype += 1
	if typeof == "NO":
		no += 1
	if typeof == "":
		unknown += 1

print("Indian Reserve : " + str(iri))
print("City : " + str(cy))
print("Ville : " + str(v))
print("District Municipality : " + str(dm))
print("City / Cité : " + str(c))
print("Northern Village : " + str(nv))
print("Town : " + str(t))
print("Specialized Municipality : " + str(sm))
print("Regional Municipality : " + str(rgm))
print("Village : " + str(vl))
print("City / Ville : " + str(cv))
print("Township : " + str(tp))
print("Rural Municipality : " + str(rm))
print("Hamlet : " + str(ham))
print("Resort Village : " + str(rv))
print("Municipality : " + str(mu))
print("Settlement : " + str(settype))
print("Unorganized : " + str(no))
print("Unknown : " + str(unknown))