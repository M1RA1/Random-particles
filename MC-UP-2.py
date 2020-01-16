import TR1 #Es el script que calcula las trayectorias
import numpy as np
import matplotlib.pyplot as plt

class clk1:
    
    get_mouse=False
    get_key=False
    
    def __init__(self):
        pass
    
    def onclick(self,event):
        if event.dblclick:
            self.get_mouse=True
            
    def click(self):
        return self.get_mouse
    
    
def run_plot(frames,line):
    
    X=np.load('Position\X.npy')
    Y=np.load('Position\Y.npy')
    
    mcl=clk1() #Guarda la clase  
    fig.canvas.mpl_connect('button_press_event', mcl.onclick)
    #Permite el uso del double click en la pantalla (hace un "link")
    
    
    f=ax.text(-2,2.2,'',fontsize=12)
    
    for i in range(frames):
        f.set_text('Frame: '+str(i))
        line.set_data(X[i],Y[i])
        fig.canvas.draw()
        fig.canvas.flush_events()
        
        ##Doble click para parar##
        if mcl.click() == True:
            break

   
N=50 #Cantidad de particulas
L=2. #Tamano de la caja LxL
frames=1000
step=0.05*np.random.random_sample(size=(N,2)) #Random steps

TR1.states(L,N,frames,step) #Trayectoria de las particulas

plt.ion() #Activa el modo interactivo de la figura

fig = plt.figure() 
ax= fig.add_subplot(111,autoscale_on=False, 
                    xlim=(-L-0.1,L+0.1),ylim=(-L-0.1,L+0.1))
line, = ax.plot([],[],'bo', ms=4)


run_plot(frames,line)

