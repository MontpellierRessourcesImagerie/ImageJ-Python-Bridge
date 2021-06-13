from ijpb.fiji.IPythonProxy import IPythonProxy

p = IPythonProxy()
p.run("from ij import IJ")
p.run("a = 3")
p.run("print(a)", wait=True)
p.run("a = a+3")
p.run("print(a)", wait=True)
p.run('print("Hello")', wait=True)
p.run('IJ.setProperty("py_res", a)')

p.disconnect()