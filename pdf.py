import csv
import json

# Open the CSV file in Gujarati text encoding and read the data
with open('sheet1.csv', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    rows = list(reader)

# Convert the data to JSON format
json_data = json.dumps(rows ,ensure_ascii=False)

# Write the JSON data to a file
with open('data.json', 'w', encoding='utf-8') as jsconfig:
    jsconfig.write(json_data)