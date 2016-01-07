import json

mmiw_cases = json.load(open('mmiw_cases.json'))

for case in mmiw_cases:
	line = case['first_name'] + ',' + case['last_name'] + ',' + case['province_missing_murdered'] + ',' + case['loc_last_known'] + ',' + case['loc_last_known_acc']
	line2 = case['first_name'] + ',' + case['last_name'] + ',' + case['province_missing_murdered'] + ',' + case['loc_missing'] + ',' + case['loc_missing_acc']
	line3 = case['first_name'] + ',' + case['last_name'] + ',' + case['province_missing_murdered'] + ',' + case['loc_found'] + ',' + case['loc_found_acc'] 
	if case['loc_last_known'] != ("" or "N/A"):
		print line
	elif case['loc_missing'] != ("" or "N/A"):
		print line2
	else:
		print line3