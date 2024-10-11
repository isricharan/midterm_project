import json

def save(file,data):
    with open(file, 'w') as f:
        json.dump(data, f, indent=4)


json_file = 'example_orders.json'
with open(json_file,'r') as f:
    d = json.load(f)

customer = {}

for i in d:
    customer[i['phone']] = i['name']

items = {}

for j in d:
    for i in j['items']:
        if i['name'] not in items:
            items[i['name']] = {'price':i['price'],'orders':0}
        items[i['name']]['orders'] += 1

save('customers.json',customer)
save('items.json',items)