from sys import path
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2 #opencv open source computer vision library
import os
import numpy as np 



class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1360x700+0+0")  #dimensions, x axis and y axis
        self.root.title("Face Recognition System")


        title_lbl=Label(self.root,text="TRAIN DATA SET",font=("times new roman",30,"bold"),bg="light gray",fg="black")
        title_lbl.place(x=0,y=0,width=1360,height=35)

        img_top=Image.open(r"C:\Users\MYPC\Desktop\FR_Images\trainface.jpg")
        img_top=img_top.resize((1360,300),Image.ANTIALIAS) #Antialias convertss high level image to low level image
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=40,width=1360,height=300)

#button
        b1_1=Button(self.root,text="TRAIN DATA",command=self.train_classifier,cursor="hand2",font=("times new roman",20,"bold"),bg="navy blue",fg="white")
        b1_1.place(x=0,y=320,width=1360,height=50)


        img_bottom=Image.open(r"C:\Users\MYPC\Desktop\FR_Images\trbg.jpg")
        img_bottom=img_bottom.resize((1360,300),Image.ANTIALIAS) #Antialias convertss high level image to low level image
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        f_lbl=Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=0,y=370,width=1360,height=300)

    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)] #list comprehesion

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L')  #Gray scale image
            imageNp=np.array(img,'uint8')       #use Numpy to convert it to grid scale
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13   #To close
        ids=np.array(ids) # Numpy betters the performance by 80% when converting to an array

        #================= Train the classifier and save==============

        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("clf.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training of datasets is completed!",parent=self.root)



            




if __name__=="__main__":
    root=Tk() #Calling root from toolkit
    obj=Train(root)
    root.mainloop()
