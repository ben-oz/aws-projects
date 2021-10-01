from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World from Flask!!!!"

@app.route('/second')
def second():
    return "La bize her yer Angara!!"

@app.route('/third/subthird')
def third():
    return 'This is the subpage of third page'

@app.route('/forth/<string:id>')     #kullanicidan girdi alicaz bu sefer 
def forth(id):
    return f'Id number of this page is {id}'





if __name__ == '__main__':
    app.run(debug=True, port=2000)  #port vermezesn default 5000 de calisir

# if this code will be run on EC2:
# if __name__ == '__main__':
#     app.run(host='0.0.0.0', debug=True, port=80)  #port 80 must be allower on security group
#
