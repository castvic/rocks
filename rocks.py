from flask import Flask, jsonify, make_response, request
import functions

example_1='''. .
. .
 :T.
. .
 .'''

print(example_1)
col1 = []
col2 = []
col3 = []
col4 = []
world = [col1, col2, col3, col4]

app = Flask(__name__)


#Handle Get Requests
@app.route('/',methods =['GET'])
def hello():
    return "Hello world!"


#Handle Post Requests
@app.route('/',methods = ['POST'])
def initialize():
    return "POST"

#Handle Put Requests
@app.route('/',methods = ['PUT'])
def update():
    req = request.get_json()
    input = req['rocks']
    world = convert_to_world(input, world)
    print(input)
    return "PUT"


#Handle Delete Requests
@app.route('/',methods = ['DELETE'])
def delete():
    return "DELETE"

if __name__ == '__main__':
    app.run()