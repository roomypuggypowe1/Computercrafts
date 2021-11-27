from flask import Flask,request,send_file, render_template

app = Flask(__name__)
commands = []
@app.route('/')
def main ():
  return render_template("test.html")


@app.route("/letter")
def letter():
  return "these are not numbers"
#all movements
@app.route("/forward")
def forward():
  commands.append ("forward")
  return render_template("test.html")

@app.route("/backwords")
def backwords():
  commands.append ("backwords")
  return render_template("test.html")

@app.route("/left")
def left():
  commands.append ("left")
  return render_template("test.html")

@app.route("/right")
def right():
  commands.append ("right")
  return render_template("test.html")

@app.route("/up")
def up():
  commands.append ("up")
  return render_template("test.html")

@app.route("/down")
def down():
  commands.append ("down")
  return render_template("test.html")
#ends  here for movements
@app.route("/turtle")
def urtle():
  if len (commands)== 0:
    return "stupid"
  return commands.pop(0)

  
app.run(host="0.0.0.0",port = 5000,debug = True)
"""
@app.route("/insert text")
def insert direction():
  commands.append ("insert what to check")
  return render_template("test.html")
"""
