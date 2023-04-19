from sys import path
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2                #opencv open source computer vision library
import os
import numpy as np 

#============Press Enter Button to Close=================

class Face_recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1360x700+0+0")  #dimensions, x axis and y axis
        self.root.title("Face Recognition System")


        title_lbl=Label(self.root,text="FACE RECOGNITION",font=("times new roman",30,"bold"),bg="lavender",fg="dark blue")
        title_lbl.place(x=0,y=0,width=1360,height=35)

#1st Image
        img_top=Image.open(r"C:\Users\MYPC\Desktop\FR_Images\tr2.jpg")
        img_top=img_top.resize((630,660),Image.ANTIALIAS) #Antialias convertss high level image to low level image
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=40,width=630,height=660)

#2nd Image
        img_bottom=Image.open(r"C:\Users\MYPC\Desktop\FR_Images\frbg1.jpg")
        img_bottom=img_bottom.resize((750,660),Image.ANTIALIAS) #Antialias convertss high level image to low level image
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        f_lbl=Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=630,y=40,width=750,height=660)

        #button
        b1_1=Button(f_lbl,text="Face Recognition",cursor="hand2",command=self.face_recognition,font=("times new roman",18,"bold"),bg="light blue",fg="black")
        b1_1.place(x=280,y=570,width=200,height=30)

#================Attendance======================
    def mark_attendance(self,i,r,n,d):
        with open("attendance.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
            if((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1}, Present")







#===============face recognition==================

    def face_recognition(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coord=[]

            for(x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))           #formula in report (LBPH)

                conn=mysql.connector.connect(host='localhost',username='root',password='Ama$am1013',database='face_recognizer')
                my_cursor=conn.cursor()   #fetching data from db

                my_cursor.execute("select Student_id from student where Student_id="+str(id))
                i=my_cursor.fetchone()
                i="+".join(i)

                my_cursor.execute("select Roll from student where Student_id="+str(id))
                r=my_cursor.fetchone()
                r="+".join(r)

                my_cursor.execute("select Name from student where Student_id="+str(id))
                n=my_cursor.fetchone()
                n="+".join(n)


                my_cursor.execute("select Dep from student where Student_id="+str(id))
                d=my_cursor.fetchone()
                d="+".join(d)


                if confidence>77: #training percentage
                    cv2.putText(img,f"ID:{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendance(i,r,n,d)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3) 

                coord=[x,y,w,h]   

            return coord

        def recognize(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,255,255),"Face",clf)
            return img
        
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("clf.xml")

        video_cap=cv2.VideoCapture(0)   #0 because we're using the Pc's camera. If any other camera then pass 1.

        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome to Face Recognition",img)

            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()


#Press Enter Button to Close





if __name__=="__main__":
    root=Tk() #Calling root from toolkit
    obj=Face_recognition(root)
    root.mainloop()

