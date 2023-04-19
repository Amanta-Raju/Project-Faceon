from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2 #opencv open source computer vision library

class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1360x700+0+0")  #dimensions, x axis and y axis
        self.root.title("Face Recognition System")

        title_lbl=Label(self.root,text="DEVELOPERS",font=("times new roman",30,"bold"),bg="blue",fg="black")
        title_lbl.place(x=0,y=0,width=1360,height=35)

        img_top=Image.open(r"C:\Users\MYPC\Desktop\FR_Images\dev2.jpg")
        img_top=img_top.resize((1360,650),Image.ANTIALIAS) #Antialias convertss high level image to low level image
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=40,width=1360,height=650)

        #frame
        main_frame=Frame(f_lbl,bd=2,bg="lavender")
        main_frame.place(x=950,y=0,width=400,height=530)

        img_top1=Image.open(r"C:\Users\MYPC\Desktop\FR_Images\dev5.jpg")
        img_top1=img_top1.resize((390,390),Image.ANTIALIAS) #Antialias convertss high level image to low level image
        self.photoimg_top1=ImageTk.PhotoImage(img_top1)

        f_lbl=Label(main_frame,image=self.photoimg_top1)
        f_lbl.place(x=0,y=0,width=390,height=390)

        dev_label=Label(main_frame,text="This project was developed by Team FaceOn.",font=("times new roman",12,"bold"),bg="white")
        dev_label.place(x=40,y=390)

        dev_label=Label(main_frame,text="Members are:\n Amanta Raju-1901224028\n J. Bhagya Raju-1901224039\n Shashwati Panda-1901224059\n Dhananjay Kumar P-1901224035\n BTECH CSE 2019-23",font=("times new roman",12,"bold"),bg="white")
        dev_label.place(x=65,y=410)


        

















if __name__=="__main__":
    root=Tk() #Calling root from toolkit
    obj=Developer(root)
    root.mainloop()        