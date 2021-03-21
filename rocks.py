#Main Application to handle the various HTTP methods using Flask
#
# TODO JSONIFY Responses and return appropriate types
# TODO Handle race conditions for simultaneous requests
# TODO Implement performance metrics
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
worlds[]
world_index = -1
app = Flask(__name__)


#Handle Get Requests
@app.route('/',methods =['GET'])
def hello():
    return "Hello world!"


#Handle Post Requests - Assume "POST" sets initial state of a 
#   world by taking an input, applying gravity, and returning
#   the resultant world
@app.route('/',methods = ['POST'])
def initialize():
    # handle input
    req = request.get_json()
    input = req['rocks']
    # create a new world index
    world_index += 1
    worlds[world_index]=[]
    #process input
    worlds[world_index] = convert_to_world(input)
    
    #format output
    return "POST"

#Handle Put Requests - Assume "PUT" is an update that drops a
#   world on top of the existing world in memory, processes
#   gravity and returns the new world
@app.route('/',methods = ['PUT'])
def update():
    req = request.get_json()
    input = req['rocks']
    world_index_update = req['world_index']
    worlds[world_index_update] = convert_to_world(input)
    print(input)
    return "PUT"


#Handle Delete Requests - remove the given world from memory
@app.route('/',methods = ['DELETE'])
def delete():
    return "DELETE"

if __name__ == '__main__':
    app.run()