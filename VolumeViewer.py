import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons
#import matplotlib.image as mpimg
import numpy as np

#####################################
# Volume Viewer in each dimension
# - Dakai Zhou
#######################################

def VolumeViewer(vol):

    if not len(vol.shape) == 3:
        raise ValueError("Please input 3D data.")

    fig = plt.figure()

    # 1st Dimension
    ax1 = plt.subplot(131)
    img1 = vol[0, :, :]
    l1 = ax1.imshow(img1, cmap = plt.cm.gray, vmin = np.min(vol), vmax = np.max(vol))
    axcolor = 'lightgoldenrodyellow'

    # 2nd Dimension
    ax2 = plt.subplot(132)
    img2 =  vol[:, 0, :]
    l2 = ax2.imshow(img2, cmap = plt.cm.gray, vmin = np.min(vol), vmax = np.max(vol))

    # 3nd Dimension
    ax3 = plt.subplot(133)
    img3 =  vol[:, :, 0]
    l3 = ax3.imshow(img3, cmap = plt.cm.gray, vmin = np.min(vol), vmax = np.max(vol))

    axslice1 = plt.axes([0.25, 0.2, 0.65, 0.03], facecolor = axcolor)
    axslice2 = plt.axes([0.25, 0.15, 0.65, 0.03], facecolor = axcolor)
    axslice3 = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor = axcolor)

    slider1 = Slider(axslice1, 'Slider1', 0, vol.shape[0]-1, valinit = 0, valstep = 1)
    slider2 = Slider(axslice2, 'Slider2', 0, vol.shape[1]-1, valinit = 0, valstep = 1)
    slider3 = Slider(axslice3, 'Slider3', 0, vol.shape[2]-1, valinit = 0, valstep = 1)

    def update1(val):
        idx1 = int(round(slider1.val))
        img1 = vol[idx1, :, :]
        l1.set_data(img1)
        fig.canvas.draw()
        
    def update2(val):
        idx2 = int(round(slider2.val))
        img2 = vol[:, idx2, :]
        l2.set_data(img2)
        fig.canvas.draw()

    def update3(val):
        idx3 = int(round(slider3.val))
        img3 = vol[:, :, idx3]
        l3.set_data(img3)
        fig.canvas.draw()

    slider1.on_changed(update1)
    slider2.on_changed(update2)
    slider3.on_changed(update3)

    plt.show()
