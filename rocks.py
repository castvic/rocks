
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

#Handle Put Requests
@app.route('/',methods = ['PUT'])


#Handle Delete Requests
@app.route('/',methods = ['DELETE'])

if __name__ == '__main__':
    app.run()