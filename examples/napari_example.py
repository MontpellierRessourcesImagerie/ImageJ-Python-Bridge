from ijpb.fiji.IPythonProxy import IPythonProxy

p = IPythonProxy()
p.run("from napariJ.func import *")
p.run("viewer = displayActiveImageInNewWindow()")
p.disconnect()