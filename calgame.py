from flask import Flask, render_template, request
from random import randint 

app = Flask(__name__)

@app.route('/')
def index():
    a = randint(1,100)
    b = randint(1,100)
    return render_template('index.html',
        a=a, 
        b=b
    )

@app.route('/check', methods=['POST'])
def check_answer():
    a = int(request.form.get('a','0'))
    b = int(request.form.get('b','0'))
    try :
            answer = int(request.form.get('answer','0'))
            if a + b == answer:
                cresult = 'ขอแสดงความยินดี คุณตอบถูก!'
            else:
                cresult = f'เสียใจ คุณตอบผิด!คำตอบที่ถูกต้องคือ {a} + {b} = {a+b}'
    except ValueError:
            cresult = 'ใส่คำตอบเป็นตัวเลขจำนวนเต็ม'
    
    return render_template('result.html', result=cresult)

app.run(debug=True, port=8000)

