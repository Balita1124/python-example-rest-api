#!flask/bin/python
from flask import Flask
import json
app = Flask(__name__)
from flask import Flask
from flask import request
from flask import Response

app = Flask(__name__)

@app.route('/exclure', methods=['POST'])
def post():
    #print "Content : " + str(request.headers['Content-Type'])
    #print "Json content: " + (request.json)

    #if request.headers['Content-Type'] == 'text/plain':
    #    print "Text Message: " + request.data

    #elif request.headers['Content-Type'] == 'application/json':
    #    print "JSON Message: " + json.dumps(request.json)
    resp = None
    if request and request.form and "jsonData" in request.form:
        print ("===========================================")
        print "Json data: " + str(request.form['jsonData'])
        print ("===========================================")
        data = {
            'status'  : 'success',
        }
        js = json.dumps(data)
        resp = Response(js, status=200, mimetype='application/json')
    else:
        print ("===========================================")
        print "Something went wrong"
        print ("===========================================")
        data = {
            'status'  : 'error',
        }
        js = json.dumps(data)
        resp = Response(js, status=200, mimetype='application/json')
    return resp


app.run(host='0.0.0.0', port=8080)