import subprocess
import sys
from ij import IJ
from threading import Thread
import time

def deal_with_stdout(process):
	while(True):
		for line in process.stdout:
			print(line)

def run(command, process, history):
	process.stdin.write(command + "\n")
	process.stdin.flush()   	
	history.append(command)
	
history = []
python = subprocess.Popen(['/home/baecker/anaconda3/bin/ipython3 -i'],
                       shell=True,
                       stdin=subprocess.PIPE,
                       stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE)
# t = Thread(target=deal_with_stdout, args=[python])
# t.setDaemon(True)
# t.start()                       
run("a = 2", python, history)
run("4 * a", python, history)                 
run("print('Hello')", python, history)      
# run("exit", python, history)          
# time.sleep(2)   
result = python.communicate()
out = "".join(list(result[::-1]))
i = 1
for command in history:
	out = out.replace("In ["+str(i)+"]:", "In ["+str(i)+"]: " + command + "\n")
	i = i + 1

IJ.log(out)
# t.join()
