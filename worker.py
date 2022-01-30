from replit import db

keys = db.keys()
print(keys)

for i in keys:
  for j in db[i]:
    print('exercise:', j['exercise'])
    print('weight:', j['weight'])
    print('repitions:', j['repitions'])
    print('time:', j['time'])
    print('\n')

dict = {}
k =0
for i in keys:
  for j in db[i]:
    dict.update( {
      i : {
       j['exercise'],
       j['weight'],
       j['repitions'],
       j['time']
      }
    } )

print(dict)
