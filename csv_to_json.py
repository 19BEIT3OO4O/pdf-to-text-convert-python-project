import csv 
import json

with open('sheet1.csv') as f:
    reader = csv.reader(f)
    question = []
    for row in reader:
        Prompt, Completion_structure,Completion_text, optionA, Answer,Solution = row
        sheet1.append({
            'Prompt': Prompt,
            'Completion_structure': question_No,
            'Completion_text': question_text,
            'optionA':option,
            'optionB':option,
            'optionC':option,
            'optionD':option,
            'Answer': answer,
            'Solution': Solution
        })

with open('quesstion.json', 'w') as f:
    json.dump(sheet1, f, indent=4)