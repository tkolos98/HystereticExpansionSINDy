import scipy as sp
import numpy as np

class preisachFun():    
    def __init__(self, alpha, alphaproxy, beta, betaproxy): 
        self.memory=0 #memory variable
        self.alpha=alpha
        self.beta=beta
        self.alphaproxy=alphaproxy
        self.betaproxy=betaproxy
        self.history=np.zeros([1,1])
    #The function, which implements the computation of output value           
    def fun(self, x):
        #In training mode, the passed array is not a single value
        if np.size(x) != 1: 
            A=0         
            maximas,_ = sp.signal.find_peaks(x) #find lokal maximas         
            minimas,_ = sp.signal.find_peaks(-x) #find lokal minimas (for proximity sensing)
            #iterate over passed array
            for count,i in enumerate(x): 
                # either limit reached, or the actual value is in its proximity and is an extrema
                if i >= self.beta or (np.isin(count,maximas) and  i >= self.beta-self.betaproxy):
                    self.memory = 1
                    An = 1
                #similarily to the lower limit
                elif self.alpha >= i or (np.isin(count,minimas) and  self.alpha+self.alphaproxy >= i) : 
                    self.memory = 0
                    An = 0
                #no switchover takes place, actual state returned
                else:
                    An = self.memory   
                A=np.hstack([A,An])
            
            A=A[1:] #clip the initial value      
            self.memory=0 #reset memory
            return A

        else: #simulation mode, similarly as previously described but no proximity detection
            if x >= self.beta: 
                self.memory = 1
                A = 1
            elif self.alpha >= x:
                self.memory = 0
                A = 0
            else:#no resetting of memory variable
                A = self.memory
                
        self.history=np.vstack([self.history,self.memory])
        return A
          
    def get_history(self):
        return self.history

    def reset_memory(self,initial_value=0):
        self.memory=initial_value
        self.history=np.full([1,1],initial_value)
