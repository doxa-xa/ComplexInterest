from flask import Flask, render_template,request
import datetime as dt
from complex_interest import ComplexInterest
app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        form = request.form
        period = (dt.datetime.strptime(form['from'],'%Y-%m-%d'),dt.datetime.strptime(form['to'],'%Y-%m-%d'))
        investment = int(form['investment'])
        interest = int(form['interest'])/100
        cx_interest = ComplexInterest(investment,period,interest)
        return render_template('result.html',data = cx_interest.report())
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)