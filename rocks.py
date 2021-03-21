#Main Application to handle the various HTTP methods using Flask
#
# TODO Handle race conditions for simultaneous requests
# TODO Implement performance metrics
from flask import Flask, jsonify, make_response, request
from functions import convert_to_world, apply_gravity, world_to_string, stack_worlds
global world_index
global worlds

col1 = []
col2 = []
col3 = []
col4 = []
world = [col1, col2, col3, col4]
worlds = []
world_index = -1



app = Flask(__name__)



#Handle Get Requests
@app.route('/',methods =['GET'])
def get():
    global worlds
    req = request.get_json()
    print(req)
    input = int(req['world'])
    world_text=world_to_string(worlds(world_index))

    response = jsonify(
        id = input,
        text = world_text
    )
    return response
#Handle Post Requests - Assume "POST" sets initial state of a 
#   world by taking an input, applying gravity, and returning
#   the resultant world
@app.route('/',methods = ['POST'])
def initialize():
    global worlds
    global world_index
    # handle input
    req = request.get_json()
    input = req['rocks']
    # create a new world index
    world_index += 1
    #process input
    world = convert_to_world(input)
    world = apply_gravity(world)
    worlds.append(world)
    #format output
    return_text = world_to_string(worlds[world_index])
    response = jsonify(
        data = return_text,
        id = world_index
    )

    return return_text

#Handle Put Requests - Assume "PUT" is an update that drops a
#   world on top of the existing world in memory, processes
#   gravity and returns the new world
@app.route('/',methods = ['PUT'])
def update():
    global worlds
    req = request.get_json()
    input = req['rocks']
    world_index_update = int(req['world'])
    new_input = convert_to_world(input)
    new_world = stack_worlds(worlds[world_index_update],new_input)
    new_world = apply_gravity(new_world)
    worlds[world_index_update] = new_world
    return_string = world_to_string(new_world)
    return return_string


#Handle Delete Requests - remove the given world from memory
@app.route('/',methods = ['DELETE'])
def delete():
    global worlds
    req = request.get_json()
    input = req['world']
    globals[input] = []
    return_string = "World " + str(input) + " deleted."
    return return_string

if __name__ == '__main__':
    app.run()