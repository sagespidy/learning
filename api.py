import  requests
import json

response = requests.get('https://api.datamuse.com/words?rel_rhy=jingle')

similar_words = json.dumps(response.json(),indent=4)

is_it_valid_dict=eval(similar_words)

for i in is_it_valid_dict:
    print(i['wordq'])

#print(is_it_valid_dict)

#print(type(similar_words),'\n',similar_words)

#print(json.dumps(response.json(),indent=4))

#for p in response.json()['people']:
#    print(str(p['name']) + str(p['craft']))

#print(json.dumps(response.json() ,indent=4) )