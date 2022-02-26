from flask import *
import os, os.path, glob, requests, shutil, sys, socket
from zipfile import ZipFile


app = Flask(__name__)

@app.route('/')
def index():
    path = ('./static/')
    x=0
    for files in os.listdir(path):
        if files.endswith('.txt'):
            x+=1
    return render_template('index.html', msg=x)


@app.route('/cuemode')
def cuemode():
    path = ('./static/')
    x=0
    for files in os.listdir(path):
        if files.endswith('.txt'):
            x+=1
    return render_template('cuemode.html', msg=x)


@app.route('/cueeditmode')
def cueeditmode():
    x = 0
    return render_template('cueeditmode.html', msg=x)


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


if __name__ == '__main__':
    app.run(debug=True, host='localhost')
