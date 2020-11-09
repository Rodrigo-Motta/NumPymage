import numpy as np

#-------------------------------------------------------------------------- 

class NumPymage:
    
    def __init__(self,nlin=0,ncol=0,valor=0):
        if type(valor) == np.ndarray:
            array = np.copy(valor)
            self.array = array
            self.data = array
            self.shape = array.shape
        else:
            array = np.full((nlin,ncol), valor)
            self.array = array
            self.data = array
            self.shape = array.shape
        
        
    def __str__(self):
        nlin,ncol = self.array.shape
        array = self.array
        
        s = ""
        for i in range(0,nlin):
            for j in range(0,ncol):
                if j == (ncol-1) and array[i,j] >= 10:
                    s += "{} ".format(array[i,j])
                if j != (ncol-1) and array[i][j] >= 10:
                    s += "{}, ".format(array[i,j])

                if j == (ncol-1) and array[i,j] < 10:
                    s += "{} ".format(array[i,j])

                if j!= (ncol-1) and array[i,j] < 10:
                    s += "{}, ".format(array[i,j])
                    
            s += "\n"
        return s
    
    def shape(self):
        return self.shape
    
    def __getitem__(self,key):
        array = self.array
        return array[key]
    
    def __setitem__(self,key,valor):
        array = self.array
        array[key] = valor
        
    def crop(self,left=0,top=0,right=0,bottom=0):
        if left == 0 and top == 0 and right == 0 and bottom == 0:
            nova = np.copy(self.array)
        else:
            nova = np.copy(self.array[top:bottom, left:right])
        return NumPymage(0,0,nova)
    
    def __add__(self,other):
        lin,col = self.array.shape
        nova = NumPymage(lin,col,0)
        if type(other) == np.ndarray or type(other) == NumPymage:
            nova = self.array + other.array
            
        else:
            nova = self.array*other
            
        return NumPymage(0,0,nova)
    
    def __mul__(self,other):
        lin,col = self.array.shape
        nova = np.zeros((lin,col))
        if type(other) == np.ndarray or type(other) == NumPymage:
            nova = self.array * other.array
            
        else:
            nova = self.array * other
                    
        return NumPymage(0,0,nova)
    
            
    def paste(self, other, tlin, tcol):
        other_i, other_j = other.shape
        self_i, self_j = self.shape
        for i in range(0, other_i):
            for j in range(0, other_j):
                if self_i > i + tlin >= 0 and self_j > j + tcol >= 0:
                    self.array[i + tlin, j + tcol] = other.array[i, j]
                                       
                    
    def paste_rectangle(self,val,left, top, right, bottom):
        nova  = NumPymage(bottom - top ,right - left,val)
        self.paste(nova,top,left)
        
        
    def paste_disc(self,val,raio,clin,ccol):
        lin,col = self.shape
        origem = (clin,ccol)
        for i in range(lin):
            for j in range(col):
                if (( (i -(origem[0]))**2 + (j -(origem[1]))**2)
                    **(1/2)< raio):
                    self.array[i,j] = val
    
        
                
                        
