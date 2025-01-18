import json

json_data = '{"name": "john","age": 30, "city":"bhawanipatna"}'


data = json.loads(json_data)

# print(data)

# print(data['name'])
# print(data['age'])
# print(data['city'])

# # modified json data 

data['country'] = 'india'
# data['age'] = 24

# # print(data)

# update_json_data = json.dumps(data)

# print(update_json_data)

# write the data to a json file named 'output.json'

with open('output.json','w') as file:
    json.dump(data,file)
with open('output.json','r') as file:
    x = json.load(file)
print(x)

