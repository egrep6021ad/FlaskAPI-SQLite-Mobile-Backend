from replit import db
import datetime
import os.path
from itertools import count
# creates replit-db keys
iterator = (count(start=0, step=1))
def sheet_builder():
    x = str(datetime.datetime.today())
    x = x[5:10]
    sheet_name = x + ".csv"
    f = open("./templates/" + sheet_name, "w")
    keys = db.keys()
    f.write("%s, \n" % x)
    temp = ''
    y = 1
    for i in keys:
        for j in db[i]:
            temp = j['username']
            f.write("%s,\t" % j['username'])
            f.write("%s,\t" % j['exercise'])
            f.write("%s,\t" % j['weight'])
            f.write("%s,\t" % j['repitions'])
            f.write("%s,\n" % j['time'])
            y = y + 1
    f.write("%s\t" % temp)
    f.close()