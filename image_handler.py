import cv2 as cv



class Image:
    def __init__(self):
        self.imagen#Matriz de la imagen
        self.mode:int#Modo de lectura
        self.byte#Bytes de la imagen
        self.width
        self.height
    def read_img(self,name:str,mode:int):#Leer imagen en modo estandar
        self.imagen=cv.imread(name,mode)
        self.height,self.width,channel=self.imagen.shape()
        if mode==0:
            self.mode=1
        elif mode==1:
            self.mode=3
        self.byte=self.imagen.tobytes()
    def read_img(self,name,mode,byte):#Leer imagen de archivo
        imagen.cv.imread(name,mode) 
        self.byte=self.imagen.tobytes()
    def assign_img(self,input):#Asignamos una nueva imagen
        self.imagen=input
        self.byte=imagen.tobytes()
        self.height,self.width,channel=self.imagen.shape()

    def show_image():
        cv.show_image("Imagen",self.imagen)
        cv.waitKey(0)
        cv.destroyAllWindows()


    def assign_vector(self,width,height,input,mode,img:bool):#Asignamos vector calculando la imagen
        self.mode=mode
        self.byte=input
        self.width=width
        self.height=height
        if img:
            self.imagen=np.frombuffer(self.byte, dtype=np.uint8)
            self.imagen=np.reshape(self.imagen, (height, width, mode))


    

    def canny(self):#Algoritmo de canny
        output=Image()
        borde=cv.canny(self.imagen,200,500)
        output.assign_img(borde)
        return output
        

        