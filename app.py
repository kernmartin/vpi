from flask import Flask, render_template
import os, os.path, glob, requests, shutil, sys
app = Flask(__name__)
app.config.update(
    DEBUG=True,
    TEMPLATES_AUTO_RELOAD=True,
)

@app.route("/")
def home():
  return render_template("index.html")

@app.route("/cuemode")
def cuemode():
  return render_template("cuemode.html")

@app.route("/cueeditmode")
def cueeditmode():
  return render_template("cueeditmode.html")

@app.route('/move/<move>')
def move(move):
    msgFromClient       = move
    bytesToSend         = str.encode(msgFromClient)
    serverAddressPort   = ("10.0.0.12", 8888)
    bufferSize          = 1024
    UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    UDPClientSocket.sendto(bytesToSend, serverAddressPort)
    x=10
    return redirect(url_for('index'))

@app.route('/readfile/<thefile>')
def readfile(thefile):
    filenr = thefile
    thefile = "./static/cue.txt"
    file1 = open(thefile, 'r')
    Lines = file1.readlines()
    msgl = Lines[int(filenr)]

    return render_template('edit.html', msg=msgl, txtfile=filenr)


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
