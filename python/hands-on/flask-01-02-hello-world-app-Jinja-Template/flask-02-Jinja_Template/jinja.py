from flask import Flask, render_template       #flask moduliunden render_teplate import ediyoruz. 

app = Flask(__name__)

@app.route('/') 
def head():
    return render_template('index.html', number1=200, number2=400)     #return ederken render_template fonksiyonunu cagirip
                                                    # degiskenlerimizi parametre olarak veroyiruz

@app.route('/multiplier')
def number():
    var1, var2 = 30, 70
    return render_template('body.html', num1=var1, num2=var2, multiplication=var1*var2)


if __name__ == '__main__':
    app.run(debug=True)

#if this code will be run on ec2:
# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=80, debug=True) #but inbound port 80 must be allowed on sec grp


