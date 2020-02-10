import csv
import json

csvfile = open('test.csv', 'r')
jsonfile = open('test.json', 'w')

fieldnames = ("public_address","avg_bal","avg_inc","avg_val","avg_timediff","avg_age","utility_score","risk_score","transitivity_score","importance_score")
reader = csv.DictReader( csvfile, fieldnames)
out = json.dumps( [ row for row in reader ] )
jsonfile.write(out)