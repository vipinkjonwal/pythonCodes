from pycricbuzz import Cricbuzz
import json
from pprint import  pprint

f = open('output.txt','w')
c = Cricbuzz()
matches = c.matches()

for i in range(len(matches)):
    pprint(matches)

# print(json.dumps(matches,indent=4),file=f)