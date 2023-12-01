import csv
import json

# Open the CSV file in Gujarati text encoding and read the data
with open('sheet1.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    headers = next(reader)
    rows = []
    for row in reader:
        row_data = {}
        for i, value in enumerate(row):
            row_data[headers[i]] = value
        rows.append(row_data)

# Convert the data to JSON format
json_data = json.dumps(rows, ensure_ascii=False)

# Write the JSON data to a file
with open('question.json', 'w', encoding='utf-8') as jsconfig:
    jsconfig.write(json_data)