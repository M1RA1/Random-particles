import numpy as np

def states(L,N,frames,step):
    
    B=np.zeros((N,2))
    B[:,0]+=np.linspace(-L,L,N,endpoint=True)
    S=np.zeros((N,2)) #Contiene los estados actuales y anteriores de las particulas
    R=step*np.random.randint(-1,2,size=(N,2)) #Elije la direccion a las
                                              #que se mueven las particulas
    DATX=[]
    DATY=[]
    
    for i in range(frames):
        #B->x #S->y
        
        DATX.append(np.copy(B[:,0]))
        DATY.append(np.copy(S[:,0]))
        
        B[:,1]=B[:,0]
        B[:,0]+=R[:,0]
        
        S[:,1]=S[:,0] #Guarda el estado anterior
        S[:,0]+=R[:,1] #Actualiza la posicion
    
        ##Corrige la posicion## 
        for j in range(len(S)):
            if S[j,0] > L :
                if S[j,1] > 0.:
                    if B[j,0] != B[j,1] : #x1 != x2
                        m=(S[j,0]-S[j,1])/(B[j,0]-B[j,1]) #Pendiente
                        x_p=B[j,1]+(-L-S[j,1])/m #Realiza una interpolacion
                        if np.abs(x_p) > L: #Verifica si esta en los limites
                            if m>0:
                                S[j,0]=m*(-L-B[j,1])+S[j,1]
                                B[j,0]=-L
                            elif m<0:
                                S[j,0]=m*(L-B[j,1])+S[j,1]
                                B[j,0]=L
                        else:
                            B[j,0]=x_p 
                            S[j,0] = -L #y=-L
                    else:
                        S[j,0] = -L
                        
                    
            elif S[j,0] < -L :
                if S[j,1] < 0.:
                    if B[j,0] != B[j,1] : #x1 != x2
                        m=(S[j,0]-S[j,1])/(B[j,0]-B[j,1]) #Pendiente
                        x_p=B[j,1]+(L-S[j,1])/m #Realiza una interpolacion
                        if abs(x_p) > L: #Verifica si esta en los limites
                            if m>0:
                                S[j,0]=m*(L-B[j,1])+S[j,1]
                                B[j,0]=L
                            elif m<0:
                                S[j,0]=m*(-L-B[j,1])+S[j,1]
                                B[j,0]=-L
                        else:
                            B[j,0]=x_p 
                            S[j,0] = L #y=L
                    else:
                        S[j,0] = L #y=L
                    
            elif B[j,0] > L :
                if B[j,1] > 0.:
                    if B[j,0] != B[j,1] : #x1 != x2
                         m=(S[j,0]-S[j,1])/(B[j,0]-B[j,1]) #Pendiente
                         y_p=m*(-L-B[j,1])+S[j,1] #Interpolacion
                         if abs(y_p) > L:
                             if m>0:
                                 B[j,0]=B[j,1]+(-L-S[j,1])/m
                                 S[j,0]=-L
                             elif m<0:
                                    B[j,0]=B[j,1]+(L-S[j,1])/m
                                    S[j,0]=L
                         else:
                             S[j,0]=y_p                           
                             B[j,0] = -L #x=-2
                    else:
                        B[j,0] = -L #x=-2
                          
            elif B[j,0] < -L :
                if B[j,1] < 0.:
                    if B[j,0] != B[j,1] : #x1 != x2
                         m=(S[j,0]-S[j,1])/(B[j,0]-B[j,1]) #Pendiente
                         y_p=m*(L-B[j,1])+S[j,1] #Interpolacion
                         if abs(y_p) > L:
                             if m>0:
                                 B[j,0]=B[j,1]+(L-S[j,1])/m
                                 S[j,0]=L
                             elif m<0:
                                    B[j,0]=B[j,1]+(-L-S[j,1])/m
                                    S[j,0]=-L
                         else:
                             S[j,0]=y_p                           
                             B[j,0] = L #x=2 
                    else:
                        B[j,0] = L #x=2 

    np.save('Position\X.npy', np.asarray(DATX,dtype=np.float))
    np.save('Position\Y.npy', np.asarray(DATY,dtype=np.float))

