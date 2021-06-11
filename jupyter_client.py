import subprocess
import sys
from ij import IJ
from threading import Thread
import time

cont = True
out = ""
stopped = False

def deal_with_stdout(process):
	global stopped
	global cont, out
	while(not stopped):
		for line in process.stdout:
			print(line)
			out = out + line 
			cont = True

def run(command, process, history, wait=True):
	global cont, out
	cont = False
	process.stdin.write(command + "\n")
	process.stdin.flush()   	
	history.append(command)
	print(command)
	out = out + (">>>" + command + "\n")
	if not wait:
		return
	while not cont:
		time.sleep(0.02)

def kRun(command, process, history, wait=True):
	global cont, out
	cont = False
	process.stdin.write("msgid = kc.execute('"+command+"')\n")
	process.stdin.flush()   	
	history.append(command)
	print(command)
	out = out + (">>>" + command + "\n")
	if not wait:
		return
	while not cont:
		time.sleep(0.02)

def connect():
	history = []
	python = subprocess.Popen(['/home/baecker/anaconda3/envs/napari/bin/python3 -i -u'],
	                       shell=True,
	                       stdin=subprocess.PIPE,
	                       stdout=subprocess.PIPE,
	                       stderr=subprocess.PIPE)
	t = Thread(target=deal_with_stdout, args=[python])
	t.setDaemon(True)
	t.start()       
	return t, python, history

def createKernelClient(python, history):
	connectionFile = IJ.getProperty('jupter_connection_file')
	run("from jupyter_client.blocking import BlockingKernelClient", python, history, wait=False)
	run("kc = BlockingKernelClient(connection_file='"+connectionFile+"')", python, history, wait=False)
	run("kc.load_connection_file()", python, history, wait=False)
	run("kc.start_channels()", python, history, wait=False)
	

t, python, history = connect()
createKernelClient(python, history)

kRun("from napariJ.func import *", python, history, wait=False)
kRun("displayActiveImageInNewWindow()", python, history, wait=False)
run("exit()", python, history, wait=False)
time.sleep(2)   
result = python.communicate()
i = 1
IJ.log(out)
stopped = True
t.join()
python.terminate()