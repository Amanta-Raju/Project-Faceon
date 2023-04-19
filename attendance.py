from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2 #opencv open source computer vision library
import os
import csv
from tkinter import filedialog


mydata=[]
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1360x700+0+0")  #dimensions, x axis and y axis
        self.root.title("Face Recognition System")

        #==================Variables==================
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()


        #first image 
        img=Image.open(r"C:\Users\MYPC\Desktop\FR_Images\att2.jpg")
        img=img.resize((700,180),Image.ANTIALIAS) #Antialias convertss high level image to low level image
        self.photoimg=ImageTk.PhotoImage(img)

        #making a label
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=700,height=180)

#second image
        img1=Image.open(r"C:\Users\MYPC\Desktop\FR_Images\att4.png")
        img1=img1.resize((670,180),Image.ANTIALIAS) #Antialias convertss high level image to low level image
        self.photoimg1=ImageTk.PhotoImage(img1)

        #making a label
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=700,y=0,width=670,height=180)

#bg image
        img3=Image.open(r"C:\Users\MYPC\Desktop\FR_Images\stubg.jpg")
        img3=img3.resize((1360,700),Image.ANTIALIAS) #Antialias convertss high level image to low level image
        self.photoimg3=ImageTk.PhotoImage(img3)


        bg_image=Label(self.root,image=self.photoimg3)
        bg_image.place(x=0,y=180,width=1360,height=700)

        title_lbl=Label(bg_image,text="ATTENDANCE MANAGEMENT SYSTEM",font=("times new roman",30,"bold"),bg="orange",fg="dark blue")
        title_lbl.place(x=0,y=0,width=1360,height=35)

        main_frame=Frame(bg_image,bd=2,bg="white")
        main_frame.place(x=10,y=40,width=1330,height=470)

        #left label frame
        left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendance Details",font=("times new roman",12,"bold"))
        left_frame.place(x=10,y=10,width=630,height=440)

        img_left=Image.open(r"C:\Users\MYPC\Desktop\FR_Images\stulft.png")
        img_left=img_left.resize((630,100),Image.ANTIALIAS) #Antialias convertss high level image to low level image
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=620,height=100)

        left_inside_frame=Frame(left_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=0,y=105,width=620,height=310)

        #labels and entries

        #attendance id
        attendanceId_label=Label(left_inside_frame,text="Attendance ID:",font=("times new roman",12,"bold"),bg="white")
        attendanceId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        attendanceId_entry=ttk.Entry(left_inside_frame,width=18,textvariable=self.var_atten_id,font=("times new roman",12,"bold"))
        attendanceId_entry.grid(row=0,column=1,padx=4,pady=8,sticky=W)

        #Roll
        rollLabel=Label(left_inside_frame,text="Roll:",font=("times new roman",12,"bold"),bg="white")
        rollLabel.grid(row=0,column=2,padx=4,pady=8,sticky=W)

        atten_roll=ttk.Entry(left_inside_frame,width=18,textvariable=self.var_atten_roll,font=("times new roman",12,"bold"))
        atten_roll.grid(row=0,column=3,pady=8,sticky=W)

        #Name
        nameLabel=Label(left_inside_frame,text="Name:",font=("times new roman",12,"bold"),bg="white")
        nameLabel.grid(row=1,column=0)

        atten_name=ttk.Entry(left_inside_frame,width=18,textvariable=self.var_atten_name,font=("times new roman",12,"bold"))
        atten_name.grid(row=1,column=1,pady=8)

        #Department
        depLabel=Label(left_inside_frame,text="Department:",font=("times new roman",12,"bold"),bg="white")
        depLabel.grid(row=1,column=2,sticky=W)

        atten_dep=ttk.Entry(left_inside_frame,width=18,textvariable=self.var_atten_dep,font=("times new roman",12,"bold"))
        atten_dep.grid(row=1,column=3,pady=8,sticky=W)

        #Time
        timeLabel=Label(left_inside_frame,text="Time:",font=("times new roman",12,"bold"),bg="white")
        timeLabel.grid(row=2,column=0)

        atten_time=ttk.Entry(left_inside_frame,width=18,textvariable=self.var_atten_time,font=("times new roman",12,"bold"))
        atten_time.grid(row=2,column=1,pady=8)

        #Date
        dateLabel=Label(left_inside_frame,text="Date:",font=("times new roman",12,"bold"),bg="white")
        dateLabel.grid(row=2,column=2,padx=4,pady=8,sticky=W)

        atten_date=ttk.Entry(left_inside_frame,width=18,textvariable=self.var_atten_date,font=("times new roman",12,"bold"))
        atten_date.grid(row=2,column=3,pady=8,sticky=W)

        #attendance
        attendanceLabel = Label(left_inside_frame,text="Attendance Status:",font=("times new roman",12,"bold"),fg="black",bg="white")
        attendanceLabel.grid(row=3,column=0,padx=5,pady=5,sticky=W)

        self.atten_status=ttk.Combobox(left_inside_frame,width=13,textvariable=self.var_atten_attendance,font=("times new roman",12,"bold"),state="readonly")
        self.atten_status["values"]=("Status","Present","Absent")
        self.atten_status.current(0)
        self.atten_status.grid(row=3,column=1,padx=5,pady=8,sticky=W)

#buttons frame
        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=250,width=615,height=55)

        import_btn=Button(btn_frame,text="Import CSV",command=self.importCsv,width=20,font=("times new roman",10,"bold"),bg="blue",fg="white")
        import_btn.grid(row=0,column=0)

        export_btn=Button(btn_frame,text="Export CSV",command=self.exportCsv, width=20,font=("times new roman",10,"bold"),bg="blue",fg="white")
        export_btn.grid(row=0,column=1)

        update_btn=Button(btn_frame,text="Update",width=20,font=("times new roman",10,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",width=22,command=self.reset_data,font=("times new roman",10,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)



    
    #Right label frame
        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendance Details",font=("times new roman",12,"bold"))
        right_frame.place(x=670,y=10,width=630,height=440)

        table_frame=Frame(right_frame,bd=2,relief=RIDGE)
        table_frame.place(x=5,y=5,width=615,height=370)

        #========scroll bar table=============================
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(table_frame,column=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id",text="Attendance ID")
        self.AttendanceReportTable.heading("roll",text="Roll")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")

        self.AttendanceReportTable["show"]="headings"

        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)

        self.AttendanceReportTable.pack(fill=BOTH,expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)

        #===================fetch data=======================

    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)

    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All Files","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)

    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data Found to Export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All Files","*.*")),parent=self.root)       
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your data has been exported to "+os.path.basename(fln)+" successfully!")
        except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)                    

    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content['values']
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])

    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")







                    















if __name__=="__main__":
    root=Tk() #Calling root from toolkit
    obj=Attendance(root)
    root.mainloop()