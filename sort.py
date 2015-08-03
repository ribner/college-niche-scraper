import csv
import json

with open('college-niche-multi-row-with-id-edited.csv') as csvfile:
	previous = ''
	college_niche_urls = csv.reader(csvfile)
	for row in college_niche_urls:
		if row[0] != previous:
			with open('college-niche-multi-row-with-id-no-duplicate.csv', 'a') as csvfile:
				writer = csv.writer(csvfile)
				writer.writerow([row[0], row[1], row[2], row[3], row[4] ])
		previous = row[0]