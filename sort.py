import json
filename = 'country.json'


json_data=open(filename).read()
json_object = json.loads(json_data)
json_sorted_object = sorted(json_object, key=lambda v: v, reverse=False)

with open('output.json', 'w') as outfile:
    outfile.write('var jsonDataCountry = ')
    json.dump(json_sorted_object, outfile)
    outfile.write(';')
