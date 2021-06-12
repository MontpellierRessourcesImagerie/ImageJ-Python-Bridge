# IJPB - ImageJ Python Bridge

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
