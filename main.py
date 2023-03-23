from flask import Flask, render_template, request
from flask import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    h21 = request.form['h21']
    h22 = request.form['h22']
    h23 = request.form['h23']
    h11 = request.form['h11']
    h12 = request.form['h12']
    
    
    if h21=="A":
      total+= 20
    elif h21=="B":
      total += 17.5
    elif h21=="C":
      total += 15
    elif h21=="D":
      total += 12.5
    elif h21=="E":
      total += 10
    elif h21=="S":
      total += 5
    elif h21=="U":
      total += 0

    
      if h11=="A":
        total+= 10
      elif h11=="B":
        total += 8.75
      elif h11=="C":
        total += 7.5
      elif h11=="D":
        total += 6.25
      elif h11=="E":
        total += 5
      elif h11=="S":
        total += 2.5
      elif h11=="U":
        total += 0

      if h12=="A":
        total+= 10
      elif h1=="B":
        total += 8.75
      elif h11=="C":
        total += 7.5
      elif h11=="D":
        total += 6.25
      elif h11=="E":
        total += 5
      elif h11=="S":
        total += 2.5
      elif h11=="U":
        total += 0

    return render_template('result.html', total=total)
    return redirect('/result')

@app.route('/result')
def index2():
    return render_template('result.html', total=total)
  
app.run(host='0.0.0.0', port=81)
