import subprocess
import sys
from ij import IJ
from threading import Thread
import time

cont = True
out = ""

def deal_with_stdout(process):
	global cont, out
	while(True):
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
	
history = []
python = subprocess.Popen(['/home/baecker/anaconda3/bin/python3 -i -u'],
                       shell=True,
                       stdin=subprocess.PIPE,
                       stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE)
t = Thread(target=deal_with_stdout, args=[python])
t.setDaemon(True)
t.start()                       
run("a = 2", python, history, wait=False)
run("4 * a", python, history)                 
run("print('Hello')", python, history)      
run("import jpype", python, history, wait=False)
run("help(a)", python, history)
run("exit()", python, history, wait=False)          
time.sleep(2)   
result = python.communicate()
i = 1
IJ.log(out)
#t.join()
