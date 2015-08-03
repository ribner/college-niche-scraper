import csv
import json
from fuzzywuzzy import fuzz
import pprint
import re

def fuzzy_match(college_niche_row, admithub_name, highest_match):
	higher = False
	college_niche_name = college_niche_row[1]
	if fuzz.ratio(re.sub(r"-", " ",college_niche_name.lower() ), re.sub(r"-", " ", admithub_name.lower() ) ) > highest_match:
		highest_match = fuzz.ratio(re.sub(r"-", " ",college_niche_name.lower() ), re.sub(r"-", " ", admithub_name.lower() ) )
		higher = True
	return highest_match, higher

original_list = ''
with open('master-list-with-related-school-ids.json') as data_file:    
    original_list = json.load(data_file)

with open('college-niche-multi-row.csv') as csvfile:
	college_niche_urls = csv.reader(csvfile)
	for row in college_niche_urls:
		highest_match = 92
		best_match = ''
		id_name = ''
		for key in original_list:
			highest_match, higher  = fuzzy_match(row, original_list[key]['name'], highest_match)
			if higher == True:
				best_match = key
				id_name = original_list[key]['name']
				print row[1]
				print original_list[key]['name']
				print highest_match
		if highest_match > 92:
			with open('college-niche-multi-row-with-id.csv', 'a') as csvfile:
				writer = csv.writer(csvfile)
				writer.writerow([row[0], row[1], best_match, id_name, highest_match ])




# for key in  original_list:
# 	original_school_no_dash = re.sub(r"-", " ", original_list[key]['name'].lower())
# 	highestMatch = 90
# 	highestSchool = ''
# 	highestUrl
# 	print original_school_no_dash
# 	with open('college-niche-multi-row.csv') as csvfile:
# 		filereader = csv.reader(csvfile)
# 		for row in filereader:
# 			if fuzz.ratio(row[1].lower(), original_school_no_dash ) > highestMatch :
# 				highestMatch = fuzz.ratio(row[1].lower(), original_school_no_dash )
# 				highestSchool = row[1].lower()
# 				highestUrl = row[0]
# 	with open('college-niche-multi-row-temp-for-revision.csv', 'a') as csvfile:
# 		writer = csv.writer(csvfile)
# 		writer.writerow([original_school_no_dash, highestSchool, highestMatch, highestUrl, key ])
	

