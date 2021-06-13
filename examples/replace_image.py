from ijpb.fiji.IPythonProxy import IPythonProxy

p = IPythonProxy()
p.run("from napariJ.func import *")
p.run("replaceImageWithActiveImage(viewer)")
p.disconnect()