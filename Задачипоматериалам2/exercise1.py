n = int(input())
my = []
for i in range(n):
    x = input().split(';')
    my.extend([x])
q = {}
for i in range(len(my)):
    row = i+1
    foo = []
    for j in range(len(my[i])):
        foo.extend([my[i][0], my[i][2]])
        if j % 2 == 0 and my[i][j] in q and my[i][j] != foo[1]:
            if my[i][0] not in q:
                q.update({my[i][0]:{'games': 0, 'wins':0, 'equals':0, 'lose':0, 'points': 0}})
            if my[i][2] not in q:
                q.update({my[i][2]:{'games': 0, 'wins':0, 'equals':0, 'lose':0, 'points': 0}})
            if int(my[i][1]) > int(my[i][3]):
                q[my[i][0]]['games'] += 1
                q[my[i][0]]['wins'] += 1
                q[my[i][0]]['points'] = q[my[i][0]]['wins'] * 3 + q[my[i][0]]['equals'] * 1 + q[my[i][0]]['lose'] * 0

                q[my[i][2]]['games'] += 1
                q[my[i][2]]['wins'] += 0
                q[my[i][2]]['lose'] += 1    
                q[my[i][2]]['points'] = q[my[i][2]]['wins'] * 3 + q[my[i][2]]['equals'] * 1 + q[my[i][2]]['lose'] * 0
            if int(my[i][1]) < int(my[i][3]):
                q[my[i][2]]['games'] += 1
                q[my[i][2]]['wins'] += 1
                q[my[i][2]]['points'] = q[my[i][2]]['wins'] * 3 + q[my[i][2]]['equals'] * 1 + q[my[i][2]]['lose'] * 0

                q[my[i][0]]['games'] += 1
                q[my[i][0]]['wins'] += 0
                q[my[i][0]]['lose'] += 1    
                q[my[i][0]]['points'] = q[my[i][0]]['wins'] * 3 + q[my[i][0]]['equals'] * 1 + q[my[i][0]]['lose'] * 0
            if int(my[i][1]) == int(my[i][3]):
                q[my[i][2]]['games'] += 1
                q[my[i][2]]['equals'] += 1
                q[my[i][2]]['points'] = q[my[i][2]]['wins'] * 3 + q[my[i][2]]['equals'] * 1 + q[my[i][2]]['lose'] * 0

                q[my[i][0]]['games'] += 1 
                q[my[i][0]]['equals'] += 1 
                q[my[i][0]]['points'] = q[my[i][0]]['wins'] * 3 + q[my[i][0]]['equals'] * 1 + q[my[i][0]]['lose'] * 0
            
        if j % 2 == 0 and my[i][j] not in q:
            if my[i][0] not in q:
                q.update({my[i][0]:{'games': 0, 'wins':0, 'equals':0, 'lose':0, 'points': 0}})
            if my[i][2] not in q:
                q.update({my[i][2]:{'games': 0, 'wins':0, 'equals':0, 'lose':0, 'points': 0}})
            if int(my[i][1]) > int(my[i][3]):
                q[my[i][0]]['games'] += 1
                q[my[i][0]]['wins'] += 1
                q[my[i][0]]['points'] = q[my[i][0]]['wins'] * 3 + q[my[i][0]]['equals'] * 1 + q[my[i][0]]['lose'] * 0

                q[my[i][2]]['games'] += 1
                q[my[i][2]]['wins'] += 0
                q[my[i][2]]['lose'] += 1    
                q[my[i][2]]['points'] = q[my[i][2]]['wins'] * 3 + q[my[i][2]]['equals'] * 1 + q[my[i][2]]['lose'] * 0
            if int(my[i][1]) < int(my[i][3]):
                q[my[i][2]]['games'] += 1
                q[my[i][2]]['wins'] += 1
                q[my[i][2]]['points'] = q[my[i][2]]['wins'] * 3 + q[my[i][2]]['equals'] * 1 + q[my[i][2]]['lose'] * 0
                
                q[my[i][0]]['games'] += 1
                q[my[i][0]]['wins'] += 0
                q[my[i][0]]['lose'] += 1    
                q[my[i][0]]['points'] = q[my[i][0]]['wins'] * 3 + q[my[i][0]]['equals'] * 1 + q[my[i][0]]['lose'] * 0
            if int(my[i][1]) == int(my[i][3]):
                q[my[i][2]]['games'] += 1
                q[my[i][2]]['equals'] += 1
                q[my[i][2]]['points'] = q[my[i][2]]['wins'] * 3 + q[my[i][2]]['equals'] * 1 + q[my[i][2]]['lose'] * 0

                q[my[i][0]]['games'] += 1 
                q[my[i][0]]['equals'] += 1 
                q[my[i][0]]['points'] = q[my[i][0]]['wins'] * 3 + q[my[i][0]]['equals'] * 1 + q[my[i][0]]['lose'] * 0
        if j % 2 == 0 and my[i][j] in q and my[i][j] == foo[1]:
            pass

for i , j in q.items():
    print(i+':', end ='')
    print(q[i].get('games'),q[i].get('wins'), q[i].get('equals'), q[i].get('lose'), q[i].get('points'),end = '\n')