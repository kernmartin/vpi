from flask import *
import vpimotorfunctions as motor
import os, os.path, glob, requests, shutil, sys
app = Flask(__name__)
app.config.update(
    DEBUG=True,
    TEMPLATES_AUTO_RELOAD=True,
)

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/cuemode")
def cuemode():
  return render_template("cuemode.html")

@app.route("/cueeditmode")
def cueeditmode():
  return render_template("cueeditmode.html")

@app.route('/move/<move>')
def move(move):
    return redirect(url_for('index'))

@app.route('/readfile/<thefile>')
def readfile(thefile):
    filenr = thefile
    thefile = "./static/cue.txt"
    file1 = open(thefile, 'r')
    Lines = file1.readlines()
    msgl = Lines[int(filenr)]
    return render_template('edit.html', msg=msgl, txtfile=filenr)

@app.route('/gotocue/<destination>/<direction>/<over>')
def gotocue(destination, direction, over):
    motor.calculateStepsDestination(destination, direction, over)
    return redirect(url_for('index'))
    
@app.route('/stop')
def stopMotor():
    motor.stopMotor()
    return redirect(url_for('index'))
    
@app.route('/otherdriver')
def otherdriver():
    motor.otherDriver()
    return redirect(url_for('index'))
    
@app.route('/steps/<steps>')
def steps(steps):
    motor.moveBy(int(steps))
    return redirect(url_for('index'))

@app.route('/updatefile/<thefile>/<steps>')
def updatefile(thefile, steps):

    linenr = int(thefile)
    thefile = "./static/cue.txt"
    a_file = open(thefile, "r")

    list_of_lines = a_file.readlines()
    list_of_lines[linenr] = steps + "\n"

    a_file = open(thefile, "w")
    a_file.writelines(list_of_lines)
    a_file.close()

    return redirect(url_for('cueeditmode'))

if __name__ == "__main__":
  app.run(host='0.0.0.0')
