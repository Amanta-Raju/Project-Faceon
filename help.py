from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2 #opencv open source computer vision library

class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1360x700+0+0")  #dimensions, x axis and y axis
        self.root.title("Face Recognition System")

        title_lbl=Label(self.root,text="HELP DESK",font=("times new roman",30,"bold"),bg="lavender",fg="dark red")
        title_lbl.place(x=0,y=0,width=1360,height=35)

        img_top=Image.open(r"C:\Users\MYPC\Desktop\FR_Images\helpbg.jpg")
        img_top=img_top.resize((1360,650),Image.ANTIALIAS) #Antialias convertss high level image to low level image
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=40,width=1360,height=650)

        main_frame=Frame(f_lbl,bd=2,bg="white")
        main_frame.place(x=850,y=170,width=400,height=230)

        dev_label=Label(main_frame,text="For any enquiries, you can contact the following:",font=("times new roman",12,"bold"),bg="white")
        dev_label.place(x=30,y=50)

        dev_label=Label(main_frame,text="Amanta Raju - amantaraju@gmail.com\nJ.Bhagya Raju - bhagyaraju0304@gmail.com\nDhananjay Kumar P - dhananjaykumarpallii@gmail.com\nShashwati Panda - shashwatipanda17@gmail.com",font=("times new roman",12,"bold"),bg="white")
        dev_label.place(x=10,y=80)




if __name__=="__main__":
    root=Tk() #Calling root from toolkit
    obj=Help(root)
    root.mainloop()        