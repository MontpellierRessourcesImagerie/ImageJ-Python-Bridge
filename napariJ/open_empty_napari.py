from ijpb.fiji.IPythonProxy import IPythonProxy

p = IPythonProxy()
p.run("import napari")
p.run("from PyQt5 import QtCore")
p.run("viewer = napari.Viewer()")
# p.run("QtCore.QTimer.singleShot(0, napari.view_image(data.astronaut(), rgb=True))")
p.disconnect()
