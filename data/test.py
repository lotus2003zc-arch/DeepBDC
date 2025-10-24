import json

data = 'E:\Downloads' + r'\base.json'
with open(data, 'r') as f:
    meta = json.load(f)
print(meta)