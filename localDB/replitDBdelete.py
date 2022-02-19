from replit import db
import os
import datetime

x = str(datetime.datetime.today())
x = x[5:10]

if os.path.exists("./templates/"+x+".html"):
  os.remove("./templates/"+x+".html")
else:
  print("The file does not exist")
keys = db.keys()
print("current keys:" + (str(keys)+'\n'))
db.clear()
keys = db.keys()
print("DELETED! updated keys:" + (str(keys)+'\n'))
