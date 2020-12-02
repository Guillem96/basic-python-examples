import json

company = json.load(open('sample.json'))

for employee in company['employees']:
    print(employee)
