from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import tkinter
import os
from student import Student
from train import Train
from face_recognition import Face_recognition
from attendance import Attendance
from developer import Developer
from help import Help
from time import strftime
from datetime import datetime


class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1360x700+0+0")  #dimensions, x axis and y axis
        self.root.title("Face Recognition System")


#first image
        img=Image.open(r"C:\Users\MYPC\Desktop\FR_Images\0x0.jpg")
        img=img.resize((500,100),Image.ANTIALIAS) #Antialias convertss high level image to low level image
        self.photoimg=ImageTk.PhotoImage(img)

        #making a label
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=100)

#second image
        img1=Image.open(r"C:\Users\MYPC\Desktop\FR_Images\top2.jpg")
        img1=img1.resize((500,100),Image.ANTIALIAS) #Antialias convertss high level image to low level image
        self.photoimg1=ImageTk.PhotoImage(img1)

        #making a label
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=100)

#third image
        img2=Image.open(r"C:\Users\MYPC\Desktop\FR_Images\0x0.jpg")
        img2=img2.resize((500,100),Image.ANTIALIAS) #Antialias convertss high level image to low level image
        self.photoimg2=ImageTk.PhotoImage(img2)

        #making a label
        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=500,height=100)


#bg image
        img3=Image.open(r"C:\Users\MYPC\Desktop\FR_Images\bgimg.jpg")
        img3=img3.resize((1360,700),Image.ANTIALIAS) #Antialias convertss high level image to low level image
        self.photoimg3=ImageTk.PhotoImage(img3)

#making a label
        bg_image=Label(self.root,image=self.photoimg3)
        bg_image.place(x=0,y=100,width=1360,height=700)

        title_lbl=Label(bg_image,text="FACE RECOGNITION ATTENDANCE SYSTEM",font=("times new roman",30,"bold"),bg="black",fg="white")
        title_lbl.place(x=0,y=0,width=1360,height=35)


        #======================time===========================
        def time():
            string=strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000,time)

        lbl=Label(title_lbl, font=("times new roman",14,"bold"),background='white',foreground='blue')
        lbl.place(x=0,y=0,width=110,height=40)
        time()    


#student button
        img4=Image.open(r"C:\Users\MYPC\Desktop\FR_Images\student.jpg")
        img4=img4.resize((220,220),Image.ANTIALIAS) #Antialias converts high level image to low level image
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_image,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=100,y=80,width=200,height=200)

        b1_1=Button(bg_image,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="dark blue",fg="white")
        b1_1.place(x=100,y=280,width=200,height=30)

 #Detect Face button
        img5=Image.open(r"C:\Users\MYPC\Desktop\FR_Images\face.jpg")
        img5=img5.resize((220,220),Image.ANTIALIAS) #Antialias converts high level image to low level image
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_image,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x=400,y=80,width=200,height=200)

        b1_1=Button(bg_image,text="Face Detector",cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg="dark blue",fg="white")
        b1_1.place(x=400,y=280,width=200,height=30)

 #Attendance button
        img6=Image.open(r"C:\Users\MYPC\Desktop\FR_Images\att.jpg")
        img6=img6.resize((220,220),Image.ANTIALIAS) #Antialias converts high level image to low level image
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_image,image=self.photoimg6,cursor="hand2",command=self.attendance_data)
        b1.place(x=700,y=80,width=200,height=200)

        b1_1=Button(bg_image,text="Attendance",cursor="hand2",command=self.attendance_data,font=("times new roman",15,"bold"),bg="dark blue",fg="white")
        b1_1.place(x=700,y=280,width=200,height=30)

#Help-Desk button
        img7=Image.open(r"C:\Users\MYPC\Desktop\FR_Images\help.jpg")
        img7=img7.resize((220,220),Image.ANTIALIAS) #Antialias converts high level image to low level image
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_image,image=self.photoimg7,cursor="hand2",command=self.help_data)
        b1.place(x=1000,y=80,width=200,height=200)

        b1_1=Button(bg_image,text="Help Desk",cursor="hand2",command=self.help_data,font=("times new roman",15,"bold"),bg="dark blue",fg="white")
        b1_1.place(x=1000,y=280,width=200,height=30)

 #Train Face button
        img8=Image.open(r"C:\Users\MYPC\Desktop\FR_Images\train.jpg")
        img8=img8.resize((220,220),Image.ANTIALIAS) #Antialias converts high level image to low level image
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_image,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b1.place(x=100,y=350,width=200,height=200)

        b1_1=Button(bg_image,text="Train Data",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="dark blue",fg="white")
        b1_1.place(x=100,y=550,width=200,height=30)

#Photos Face button
        img9=Image.open(r"C:\Users\MYPC\Desktop\FR_Images\pho.jpg")
        img9=img9.resize((220,220),Image.ANTIALIAS) #Antialias converts high level image to low level image
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_image,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=400,y=350,width=200,height=200)

        b1_1=Button(bg_image,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="dark blue",fg="white")
        b1_1.place(x=400,y=550,width=200,height=30)

#Developer button
        img10=Image.open(r"C:\Users\MYPC\Desktop\FR_Images\dev.jpg")
        img10=img10.resize((220,220),Image.ANTIALIAS) #Antialias converts high level image to low level image
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(bg_image,image=self.photoimg10,cursor="hand2",command=self.developer_data)
        b1.place(x=700,y=350,width=200,height=200)

        b1_1=Button(bg_image,text="Developers",cursor="hand2",command=self.developer_data,font=("times new roman",15,"bold"),bg="dark blue",fg="white")
        b1_1.place(x=700,y=550,width=200,height=30)

#Exit button
        img11=Image.open(r"C:\Users\MYPC\Desktop\FR_Images\exit.jpg")
        img11=img11.resize((220,220),Image.ANTIALIAS) #Antialias converts high level image to low level image
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(bg_image,image=self.photoimg11,cursor="hand2",command=self.iExit)
        b1.place(x=1000,y=350,width=200,height=200)

        b1_1=Button(bg_image,text="Exit",cursor="hand2",command=self.iExit,font=("times new roman",15,"bold"),bg="dark blue",fg="white")
        b1_1.place(x=1000,y=550,width=200,height=30)
    
    
    def open_img(self):
        os.startfile("data") 

    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are you sure you want to exit?",parent=self.root)
        if self.iExit>0:
            self.root.destroy()
        else:
            return    



    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)    


    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_recognition(self.new_window)   

    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)  

    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window) 

    def help_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)            
   



        






#calling the main function
if __name__=="__main__":
    root=Tk() #Calling root from toolkit
    obj=Face_Recognition_System(root)
    root.mainloop()

        
