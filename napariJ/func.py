from jpype import *
import jpype.imports
from jpype.types import *
import numpy as np
from ij import IJ, ImagePlus
from ij.plugin import HyperStackConverter
import napari

def displayActiveImageInNewWindow():
    image = IJ.getImage()
    cal = image.getCalibration()
    zFactor = cal.getZ(1) / cal.getX(1)
    title = image.getShortTitle()
    shift = 128
    bitDepth = image.getBitDepth()
    if bitDepth==16:
        shift = 32768
    dims = list(image.getDimensions())
    print(dims)
    isHyperStack = image.isHyperStack()
    HyperStackConverter.toStack(image)
    stackDims = list(image.getDimensions())
    dim = stackDims[3]
    if stackDims[2] == 1 and stackDims[3] == 1 and stackDims[4] > 1:
        dim = dims[4]
    pixels = np.array(image.getStack().getVoxels(0, 0, 0, stackDims[0], stackDims[1], dim, [])) + shift
    if isHyperStack:
        image2 = HyperStackConverter.toHyperStack(image, dims[2], dims[3], dims[4], "Composite");
        image.close()
        image2.show()
    viewer = napari.Viewer()
    viewer.theme = 'dark'
    colors = ['magenta', "cyan", "yellow", "red", "green", "blue"]
    for c in range(0, dims[2]):
        viewer.add_image(pixels.reshape(dims[4], dims[3], dims[2], dims[1], dims[0])[:, :, c, :, :],
                         name="C" + str(c + 1) + "-" + str(title),
                         colormap=colors[c],
                         blending='additive',
                         scale=[zFactor, 1, 1])
    viewer.dims.ndisplay = 3
    return viewer
    
def replaceImageWithActiveImage(viewer):
    for c in range(0, len(viewer.layers)):
        viewer.layers.pop(0)
    image = IJ.getImage()
    cal = image.getCalibration()
    zFactor = cal.getZ(1) / cal.getX(1)
    title = image.getShortTitle()
    shift = 128
    bitDepth = image.getBitDepth()
    if bitDepth==16:
        shift = 32768
    dims = list(image.getDimensions())
    print(dims)
    isHyperStack = image.isHyperStack()
    HyperStackConverter.toStack(image)
    stackDims = list(image.getDimensions())
    dim = stackDims[3]
    if stackDims[2] == 1 and stackDims[3] == 1 and stackDims[4] > 1:
        dim = dims[4]
    pixels = np.array(image.getStack().getVoxels(0, 0, 0, stackDims[0], stackDims[1], dim, [])) + shift
    if isHyperStack:
        image2 = HyperStackConverter.toHyperStack(image, dims[2], dims[3], dims[4], "Composite");
        image.close()
        image2.show()
    colors = ['magenta', "cyan", "yellow", "red", "green", "blue"]
    for c in range(0, dims[2]):
        viewer.add_image(pixels.reshape(dims[4], dims[3], dims[2], dims[1], dims[0])[:, :, c, :, :],
                         name="C" + str(c + 1) + "-" + str(title),
                         colormap=colors[c],
                         blending='additive',
                         scale=[zFactor, 1, 1])
    viewer.dims.ndisplay = 3
    
def screenshot(viewer):
    screenshot = viewer.screenshot(canvas_only=True)
    pixels = JInt[:](list(screenshot[:, :, 0:3].flatten()))
    image = java.awt.image.BufferedImage(screenshot.shape[1], screenshot.shape[0], java.awt.image.BufferedImage.TYPE_3BYTE_BGR)
    image.getRaster().setPixels(0,0,screenshot.shape[1], screenshot.shape[0], pixels)
    title = viewer.layers[0].name
    if 'C1-' in viewer.layers[0].name:
	    title = title.split('C1-')[1]
    ip = ImagePlus("screenshot of " + title, image)
    ip.show()
