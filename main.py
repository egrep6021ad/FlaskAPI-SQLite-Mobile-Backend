from flask import Flask, jsonify, request
from flask_cors import CORS
from threading import Thread
from replit import db
from itertools import count
from markupsafe import escape
app = Flask('')
CORS(app)
iterator = (count(start=0, step = 1))

@app.route('/')	
def home():
	return f"the index is: {escape(iterator)}... if you dont like it, then get the fuck out of here.{escape(db.keys())}"

@app.route('/api/', methods=["GET"], strict_slashes=False)
def GET():
  string =''
  dict = {}
  keys = db.keys()
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
  string += str(dict)
  return string
# could be smarter to add the stuff to the dict as it comes in rather than when requested outbound
@app.route('/api/', methods=["POST"], strict_slashes=False)
def POST():
  body = request.get_json("body")
  db[next(iterator)] = body
  return "wtf_mane"

def run():
	app.run(host='0.0.0.0',port=7000)

t = Thread(target=run)
t.start()