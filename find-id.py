import csv
import json
from fuzzywuzzy import fuzz
import pprint

original_list = ''
with open('master-list-with-related-schools.json') as data_file:    
    original_list = json.load(data_file)

with open('college-niche.csv') as csvfile:
	filereader = csv.reader(csvfile, delimiter=' ', quotechar='|')
	for row in filereader:
		if row[0][0:30] != 'https://colleges.niche.comhttp':
			print row[0].split('/')[len(row[0].split('/'))-3]
			# print row[0][0:30]

# for key in  original_list:
# 	# with open('college-niche.csv') as csvfile:
# 	# 	filereader = csv.reader(csvfile, delimiter=' ', quotechar='|')
# 	# 	for row in filereader:
# 	# 		print row[0]
# 	print original_list[key]['name']