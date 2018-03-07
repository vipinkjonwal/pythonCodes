from pycricbuzz import Cricbuzz
import json
from pprint import  pprint

f = open('output.txt','w')
c = Cricbuzz()
matches = c.matches()
scorecard = c.scorecard(18775)

# pprint(scorecard)


for i in range(len(matches)):
    print('Match: ',end='')
    print(matches[i]['mchdesc'])
    print('Result: ',end='')
    print(matches[i]['status'],end='')
    print('\n')

'''
print(json.dumps(matches,indent=4),file=f)
'''
