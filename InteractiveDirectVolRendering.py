import numpy as np
import matplotlib.pyplot as plt
import DicomSlice2Vol as DV
import DirectVolRendering as DVR


vol = DV.DicomSlice2Vol('MPRAGE_PAT2_ISO/*')
vol = np.rot90(vol,1,(0,2))
xmax = np.max(vol)
xmin = np.min(vol)
x = np.array([0, xmax])
y = np.array([-0.05, -0.05])
# convert image to with bit-depth 2^8
vol = np.round(255*(vol-xmin)/(xmax-xmin+10**-15))
xmax = np.max(vol)
# Transfer function controller
fig, ax = plt.subplots()
ax.set_ylim(-0.07,0.1)
ax.set_xlim(0, xmax)
ax.plot(x,y,':', x, [0, 0], 'black')


class InteractiveDirectVolRendering():
    def __init__(self,ax=None):
        
        if ax == None:
            self.ax = plt.gca()
        else:
            self.ax=ax
        
        # initialize the transfer function
        self.xm1 = 0.1*xmax
        self.xm2 = 0.3*xmax
        self.xm3 = 0.5*xmax
        self.xm4 = 0.7*xmax
        self.xm5 = xmax
        self.ym1 = 0
        self.ym2 = 0.01
        self.ym3 = 0.01
        self.ym4 = 0.01
        self.ym5 = 0.01
        self.marker11 = [self.ax.plot([self.xm1],[-0.05], marker="o", color="black")[0]]
        self.marker12 = [self.ax.plot([self.xm1],[self.ym1], marker="o", color="black")[0]]
        self.marker21 = [self.ax.plot([self.xm2],[-0.05], marker="o", color="blue")[0]]
        self.marker22 = [self.ax.plot([self.xm2],[self.ym2], marker="o", color="blue")[0]]
        self.marker31 = [self.ax.plot([self.xm3],[-0.05], marker="o", color="green")[0]]
        self.marker32 = [self.ax.plot([self.xm3],[self.ym3], marker="o", color="green")[0]]
        self.marker41 = [self.ax.plot([self.xm4],[-0.05], marker="o", color="red")[0]]
        self.marker42 = [self.ax.plot([self.xm4],[self.ym4], marker="o", color="red")[0]]
        self.marker51 = [self.ax.plot([self.xm5],[-0.05], marker="o", color="purple")[0]]
        self.marker52 = [self.ax.plot([self.xm5],[self.ym5], marker="o", color="purple")[0]]
        self.line = [self.ax.plot([0, self.xm1, self.xm2, self.xm3, self.xm4, self.xm5], [0, self.ym1, self.ym2, self.ym3, self.ym4, self.ym5])[0]]

        fig1, ax1 = plt.subplots()
        self.img = ax1.imshow(DVR.DirectVolRendering1(vol, self.xm1, self.xm2, self.xm3, self.xm4, self.ym1, self.ym2, self.ym3, self.ym4, self.ym5))
        self.ax1 = ax1

        self.draggable11=False
        self.draggable12=False
        self.draggable21=False
        self.draggable22=False
        self.draggable31=False
        self.draggable32=False
        self.draggable41=False
        self.draggable42=False
        self.draggable52=False

        self.c1 = self.ax.figure.canvas.mpl_connect("button_press_event", self.click)
        self.c2 = self.ax.figure.canvas.mpl_connect("button_release_event", self.release)
        self.c3 = self.ax.figure.canvas.mpl_connect("motion_notify_event", self.drag)

    def click(self,event):
        if event.button==1:
            #leftclick
            if (-0.055 <= event.ydata <= -0.045) & (self.xm1-0.01*xmax <= event.xdata <= self.xm1+0.01*xmax):
                self.draggable11 = True
            if (-0.055 <= event.ydata <= -0.045) & (self.xm2-0.01*xmax <= event.xdata <= self.xm2+0.01*xmax):
                self.draggable21 = True
            if (-0.055 <= event.ydata <= -0.045) & (self.xm3-0.01*xmax <= event.xdata <= self.xm3+0.01*xmax):
                self.draggable31 = True
            if (-0.055 <= event.ydata <= -0.045) & (self.xm4-0.01*xmax <= event.xdata <= self.xm4+0.01*xmax):
                self.draggable41 = True
            if (self.ym1-0.01 <= event.ydata <= self.ym1+0.01) & (self.xm1-0.01*xmax <= event.xdata <= self.xm1+0.01*xmax):
                self.draggable12 = True
            if (self.ym2-0.01 <= event.ydata <= self.ym2+0.01) & (self.xm2-0.01*xmax <= event.xdata <= self.xm2+0.01*xmax):
                self.draggable22 = True
            if (self.ym3-0.01 <= event.ydata <= self.ym3+0.01) & (self.xm3-0.01*xmax <= event.xdata <= self.xm3+0.01*xmax):
                self.draggable32 = True
            if (self.ym4-0.01 <= event.ydata <= self.ym4+0.01) & (self.xm4-0.01*xmax <= event.xdata <= self.xm4+0.01*xmax):
                self.draggable42 = True
            if (self.ym5-0.01 <= event.ydata <= self.ym5+0.01) & (self.xm5-0.01*xmax <= event.xdata <= self.xm5+0.01*xmax):
                self.draggable52 = True
        elif event.button==3:
            self.draggable11=False
            self.draggable12=False
            self.draggable21=False
            self.draggable22=False
            self.draggable31=False
            self.draggable32=False
            self.draggable41=False
            self.draggable42=False
            self.draggable52=False

    def drag(self, event):
        if self.draggable11:
            self.update11(event)
        elif self.draggable12:
            self.update12(event)

        if self.draggable21:
            self.update21(event)
        elif self.draggable22:
            self.update22(event)

        if self.draggable31:
            self.update31(event)
        elif self.draggable32:
            self.update32(event)

        if self.draggable41:
            self.update41(event)
        elif self.draggable42:
            self.update42(event)

        if self.draggable52:
            self.update5(event)

        if self.draggable11 | self.draggable12 | self.draggable21 | self.draggable22 | self.draggable31 | self.draggable32 | self.draggable41 | self.draggable42 | self.draggable52:
            self.update6()
            #self.update7(vol)
        
        ax.figure.canvas.draw_idle()
        

    def release(self,event):
        if self.draggable11 | self.draggable12 | self.draggable21 | self.draggable22 | self.draggable31 | self.draggable32 | self.draggable41 | self.draggable42 | self.draggable52:
            self.update7(vol)
        self.ax1.figure.canvas.draw_idle()
            
        self.draggable11=False
        self.draggable12=False
        self.draggable21=False
        self.draggable22=False
        self.draggable31=False
        self.draggable32=False
        self.draggable41=False
        self.draggable42=False
        self.draggable51=False
        self.draggable52=False

    def update11(self, event):
        self.xm1 = event.xdata
        if self.xm1 < 0:
            self.xm1 = 0
        elif self.xm2 <= self.xm1:
            self.xm1 = self.xm2-0.01*xmax
        self.marker11[0].set_data([self.xm1],[-0.05])
        self.marker12[0].set_data([self.xm1],[self.ym1])

    def update12(self, event):
        self.ym1 = event.ydata
        if self.ym1 < 0:
            self.ym1 = 0
        elif self.ym1 > 0.3:
            self.ym1 = 0.3
        self.marker12[0].set_data([self.xm1],[self.ym1])

    def update21(self, event):
        self.xm2 = event.xdata
        if self.xm2 <= self.xm1:
            self.xm2 = self.xm1+0.01*xmax
        elif self.xm3 <= self.xm2:
            self.xm2 = self.xm3-0.01*xmax
        self.marker21[0].set_data([self.xm2],[-0.05])
        self.marker22[0].set_data([self.xm2],[self.ym2])

    def update22(self, event):
        self.ym2 = event.ydata
        if self.ym2 < 0:
            self.ym2 = 0
        elif self.ym2 > 0.3:
            self.ym2 = 0.3
        self.marker22[0].set_data([self.xm2],[self.ym2])

    def update31(self, event):
        self.xm3 = event.xdata
        if self.xm3 <= self.xm2:
            self.xm3 = self.xm2+0.01*xmax
        elif self.xm4 <= self.xm3:
            self.xm3 = self.xm4-0.01*xmax
        self.marker31[0].set_data([self.xm3],[-0.05])
        self.marker32[0].set_data([self.xm3],[self.ym3])

    def update32(self, event):
        self.ym3 = event.ydata
        if self.ym3 < 0:
            self.ym3 = 0
        elif self.ym3 > 0.3:
            self.ym3 = 0.3
        self.marker32[0].set_data([self.xm3],[self.ym3])

    def update41(self, event):
        self.xm4 = event.xdata
        if self.xm4 <= self.xm3:
            self.xm4 = self.xm3+0.01*xmax
        elif self.xm5 <= self.xm4:
            self.xm4 = self.xm5-0.01*xmax
        self.marker41[0].set_data([self.xm4],[-0.05])
        self.marker42[0].set_data([self.xm4],[self.ym4])

    def update42(self, event):
        self.ym4 = event.ydata
        if self.ym4 < 0:
            self.ym4 = 0
        elif self.ym4 > 0.3:
            self.ym4 = 0.3
        self.marker42[0].set_data([self.xm4],[self.ym4])

    def update5(self, event):
        self.ym5 = event.ydata
        if self.ym5 < 0:
            self.ym5 = 0
        elif self.ym5 > 0.3:
            self.ym5 = 0.3
        self.marker52[0].set_data([self.xm5],[self.ym5])

    def update6(self):
        self.line[0].set_data([0, self.xm1, self.xm2, self.xm3, self.xm4, self.xm5], [0, self.ym1, self.ym2, self.ym3, self.ym4, self.ym5])

    def update7(self, vol):
        self.img.set_data(DVR.DirectVolRendering1(vol, self.xm1, self.xm2, self.xm3, self.xm4, self.ym1, self.ym2, self.ym3, self.ym4, self.ym5))



dm = InteractiveDirectVolRendering()

# histogram of the image
fig2, ax2 = plt.subplots()
a = np.ravel(vol)
b = a[a>10]
plt.hist(b, 100)

plt.show()
