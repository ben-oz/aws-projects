from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def head():
    #first = 'This is my first condition in flask'
    first = ''
    return render_template('index.html', message=first)


@app.route('/page1')
def my_list():
    names = ["Peter Parker", "Bruce Wayne", "Tony Stark"]
    return render_template('body.html', object=names)






if __name__ == '__main__':
    #app.run(debug=True)
    app.run(host='0.0.0.0', port=80)

