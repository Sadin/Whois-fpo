import json, requests, pprint

name = raw_input('Enter a name: ')

fas_request = requests.get('https://badges.fedoraproject.org/user/{}/json'.format(name))

pprint.pprint(fas_request.json())
