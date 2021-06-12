# IJPB - ImageJ Python Bridge

# Prerequisites

* FIJI
* conda

# How to use

* clone the repository<br>``git clone https://github.com/MontpellierRessourcesImagerie/ImageJ-Python-Bridge.git``
* cd into the folder ImageJ-Python-Bridge<br>``cd ImageJ-Python-Bridge``
* create a conda environment from the ``environment.yml`` file<br>``conda env create -f environment.yml`` 
* activate the environment<br>``conda activate ijpb``
* adjust the path and memory settings in ijpb/func.py according to your FIJI version
* in startFIJI.py set the path to your FIJI-installation folder
* run a jupyter qt-console<br>``jupyter qtconsole &``
* in the console run the script that starts FIJI<br> ``run startFIJI``
* in FIJI use the IPythonProxy to run python commands

```python
p = IPythonProxy()
p.run("from ij import IJ")
p.run("a = 3")
p.run("print(a)", wait=True)
p.run("a = a+3")
p.run("print(a)", wait=True)
p.run('print("Hello")', wait=True)
p.run('IJ.setProperty("py_res", a)')
p.disconnect()
```
```
  >>>from ij import IJ
  >>>a = 3
  >>>print(a)
  3
  >>>a = a+3
  >>>print(a)
  6
  >>>print("Hello")
  Hello
  >>>IJ.setProperty("py_res", a)
```

# Under the hood

* make ImageJ communicate with python3
* use jpype to access ImageJ from python
* use the jupyter-client to access python from ImageJ
* start the jvm from an ipython 
* from ImageJ communicate over a socket with another python interpreter and use the jupter_client to communicate with the ipython that started the jvm

# Applications

* Run python gui-applications like napari from ImageJ and exchange data with them
* Use ImageJ image processing and analysis in python applications, for example napari-plugins
* Use python image and data analysis in ImageJ workflows (macros, scripts, plugins)
* Run and control the training and application of python based Deep-Learning algorithms from ImageJ

# Status

* early proof of concept
* see [jupyter_client_with_ret_.py](https://github.com/MontpellierRessourcesImagerie/ImageJ-Python-Bridge/blob/main/exploring/jupyter_client_with_ret_.py) and
* [napariJ/func.py](https://github.com/MontpellierRessourcesImagerie/ImageJ-Python-Bridge/blob/main/napariJ/func.py)

**If you want to participate in the development of IJPB on any level (design, programming, documentation, ...)  please contact [me](https://github.com/volker-baecker)**

# Next steps

* Write an object oriented jython library for the access from jython to ipython3
* Write some data converters for images and tables (checkout what has been done in pyimagej)
* showcase a tool that opens the active ImageJ image in napari
* showcase using python k-means clustering in ImageJ
* showcase using python deep-learning algs in ImageJ (use IJPB in DL4Mic)
* write a scijava scripting-language plugin for python 3 and add it to the FIJI-script editor
