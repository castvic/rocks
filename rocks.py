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
@app.route("/rocks",methods =['GET'])
def get():
    global worlds
    req = request.args.get("world")
    print(req)
    world_index = int(req)
    if len(worlds) > world_index:
        return "World does not exist"
    world_text=world_to_string(worlds[world_index])

    response = jsonify(
        world = world_index,
        rocks = world_text
    )
    return response
#Handle Post Requests - Assume "POST" sets initial state of a 
#   world by taking an input, applying gravity, and returning
#   the resultant world
@app.route('/rocks',methods = ['POST'])
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

    return world_index

#Handle Put Requests - Assume "PUT" is an update that drops a
#   world on top of the existing world in memory, processes
#   gravity and returns the new world
@app.route('/rocks',methods = ['PUT'])
def update():
    global worlds
    req = request.args.get("world")
    world_index_update = int(req)
    new_input = convert_to_world(input)
    new_world = stack_worlds(worlds[world_index_update],new_input)
    new_world = apply_gravity(new_world)
    worlds[world_index_update] = new_world
    return_string = world_to_string(new_world)
    return return_string


#Handle Delete Requests - remove the given world from memory
@app.route('/rocks',methods = ['DELETE'])
def delete():
    global worlds
    success = True
    req = request.get_json()
    input = int(req['world'])
    if len(worlds) > input:
        repsonse = jsonify(
            success = False
        )
        return response
    worlds[input] = []
    response = jsonify(
        success = success
    )
    return response

if __name__ == '__main__':
    app.run()