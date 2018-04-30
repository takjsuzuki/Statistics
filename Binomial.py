import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.animation as animation

from matplotlib.animation import ArtistAnimation




class Histogram:

    def __init__(self,NumStage):
        count = np.zeros(NumStage+1)


def ShowHistogram(count,NumStage,ax):

    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    
    ax.set_xlim(-0.5,0.5)
    ax.set_ylim(0,1.0)

    ax.set_xlabel('x')
    ax.set_ylabel('freq')
    x = np.linspace(-NumStage/2,NumStage/2,NumStage+1)
    x = np.linspace(-0.5,0.5,NumStage+1)
    print(x)
    print(count)
    ax.plot(x,count*2)
            

class Object:
    
    def __init__(self,NumStage,count):
        self.x = 0.0
        self.y = NumStage
        # self.count = np.zeros(NumStage+1)
        
    def Forward_onestep(self):

        if (self.y > 0):
            self.x += np.random.randint(0,2) - 0.5
            self.y -= 1

    def Count(self):
        count[int(self.x+NumStage/2)] += 1

    def ReturnX(self):
        return self.x+NumStage/2
            
            
    def AddCircle(self,ax):
        c = patches.Circle(xy=(self.x, self.y*np.sqrt(3)*0.5), radius=0.1, fc='r', ec='r')
        ax.add_patch(c)

    def RemoveCircle(self,c):
        c.remove()

        

def Draw_Triangle(ax,NumStage):

    ax.set_xlim(-NumStage/2-0.5,NumStage/2+0.5)
    ax.set_ylim(-0.5,NumStage*0.5*np.sqrt(3)+0.5)
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    ax.set_axis_off()    

    
    for stage in range(NumStage):
        for num in range(stage+1):
            x = num - stage/2
            y1 = (NumStage-stage)*np.sqrt(3)*0.5
            y2 = (NumStage-stage-1)*np.sqrt(3)*0.5
            tri = plt.Polygon(((x,y1),(x-0.5,y2),(x+0.5,y2)),fc="#770000",fill=False)
            ax.add_patch(tri)            

    return 0



if __name__=="__main__":

    NumStage = 7
    count = np.zeros(NumStage+1)

    Nframes = 100
    NumObj = 1*Nframes
    #NumObj = Nframes

    fig = plt.figure()
    plt.subplots_adjust(left=-0.3, bottom=0.1, right=1.3, top=0.9, wspace=0, hspace=0)

    print(count)


    def plot(i,count,Nframes):

        plt.clf()
        plt.axis('off')

        ax = fig.add_subplot(2,1,1)
        ax2 = fig.add_subplot(2,1,2)

        Draw_Triangle(ax,NumStage)
    
        plt.axis('scaled')
        ax.set_aspect('equal')
        #ax2.set_aspect('equal')

        ini = int(NumObj/Nframes*i)
        fin = int(NumObj/Nframes*(i+1))
        print(ini,fin)

        obj = Object(NumStage,count)
        for i in range(NumStage):
            obj.Forward_onestep()
            obj.AddCircle(ax)
        obj.Count()

        for j in range(ini+1,fin):
            obj = Object(NumStage,count)
            for i in range(NumStage):
                obj.Forward_onestep()
                #obj.plot(ax)
            obj.Count()

        ShowHistogram(count/NumObj,NumStage,ax2)
    
    # for i in range(Nframes):
    #     im = plot(i,count,Nframes)
    #     plt.savefig("test{0}.png".format(i))

    ani = animation.FuncAnimation(fig, plot, fargs=(count,Nframes),frames=Nframes,interval=1)
    ani.save("output.gif", writer="imagemagick")



