from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return 'This is home page for no path, <h1> Welcome Home</h1>'

@app.route('/about')
def about():
    return '<h1>This is my about page</h1>'

@app.route('/error')
def f_error():
    return '<h1>Either you run into an error or you are not authorized.</h1>'

@app.route('/hello')
def hello():
    name = 'Benjamin'
    return f'<h1>Hello, {name}! </h1>'

@app.route('/admin')
def admin():
    return redirect(url_for('f_error'))
    # u have to redirect to the corresponding function name! not the /route name

@app.route('/<name>')
def greet(name):
    greet_format = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Greeting Page</title>
</head>
<body>
    <h1>Hello, { name }!</h1>
    <h1>Welcome to my Greeting Page</h1>
</body>
</html>
    """
    return greet_format

@app.route('/greet_admin')
def greet_admin():
    return redirect(url_for('greet', name='Master Admin!!!'))

# this part will not work unless u comment 27-41 lines
# @app.route('/<dyn_name>')
# def greeting(dyn_name):
#     return render_template('greet.html', name=dyn_name)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
