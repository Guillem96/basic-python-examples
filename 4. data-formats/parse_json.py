import json

# company = json.load(open('sample.json'))

# for employee in company['employees']:
#     print("Name:", employee['firstName'], 
#           employee['lastName'])

# pet = {'name': 'milu', 'color': 'white'}

# f = open('pet.json', 'w')
# json.dump(pet, f)
# f.close()

numbers = list(range(10))

number_json_formatted = json.dumps(numbers)
print(number_json_formatted, type(number_json_formatted))