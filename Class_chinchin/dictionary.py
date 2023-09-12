import json
accounts_dict = {'accounts': [
  {'account': 100, 'name': 'jones', 'balance': 345.67},
  {'account': 200, 'name': 'Doe', 'balance': 345.67}]
}

with open('accounts.json', 'w') as accounts:
  json.dump(accounts_dict, accounts)

with open('accounts.json', 'r') as accounts:
  accounts_json = json.load(accounts)

with open('accounts.json', 'r') as accounts:
  print(json.dumps(json.load(accounts), indent=4))



