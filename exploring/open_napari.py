import subprocess
import sys
from ij import IJ
from threading import Thread
import time

history = []
process = None

def start():
	global history, process
	history = []
	process = subprocess.Popen(['/home/baecker/anaconda3/envs/napari/bin/python3 -i -u'],
	                       shell=True,
	                       stdin=subprocess.PIPE,
	                       stdout=subprocess.PIPE,
	                       stderr=subprocess.PIPE)
	process.daemon = True
	                       
def run(command):
	global history, process
	process.stdin.write(command + "\n")
	process.stdin.flush()   	
	history.append(command)

def stop():
	global history, process
	result = process.communicate()
	out = "".join(list(result[::-1]))
	i = 1
	for command in history:
		out = out.replace("In ["+str(i)+"]:", "In ["+str(i)+"]: " + command + "\n")
		i = i + 1
	IJ.log(out)

start()
run("from skimage import data")
run("import napari")
run("from PyQt5 import QtCore")
run("viewer = napari.view_image(data.astronaut(), rgb=True)")
# run("QtCore.QTimer.singleShot(0, napari.view_image(data.astronaut(), rgb=True))")

