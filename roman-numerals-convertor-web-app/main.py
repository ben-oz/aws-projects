# This program may not work properly if Python version is less than  3.7

from RN_Constants import *
from flask import Flask, render_template, request

app = Flask(__name__)

print(TEXT_START)

def converter(arg_input):
    result = ''
    try:
        user_input = int(arg_input)

    except ValueError:
        result = 'Input not valid'

    else:
        if not 1 <= user_input <= 3999:
            result = 'Input not valid'
            
        else:
            divisors = LETTERS.keys()
            in_roman_list = []
            remainder = user_input
            
            for divisor in divisors:
                quotient = remainder // divisor
                [in_roman_list.append(LETTERS[divisor]) for _ in range(quotient)]
                remainder = remainder % divisor

            in_roman = ''.join(in_roman_list)
            
            for k, v in SPECIAL_NUMBERS.items():
                in_roman = in_roman.replace(k ,v)
                
            result = in_roman
    
    return result


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        user_input_raw = request.form['number']
        result = converter(user_input_raw)
        if result == 'Input not valid':
            return render_template('index.html', not_valid=True, developer_name="Benjamin")
        return render_template('result.html', developer_name="Benjamin", number_decimal=user_input_raw, number_roman=result)
    else:
        return render_template('index.html', not_valid=False, developer_name="Benjamin")




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
