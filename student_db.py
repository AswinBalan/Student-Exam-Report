from tkinter import *
import tkinter as tk
from tkinter import ttk,messagebox,font
from PIL import Image, ImageTk
import io
from reportlab.pdfgen import canvas
from PyPDF2 import PdfFileWriter, PdfFileReader
from reportlab.lib.pagesizes import letter
    
root =Tk()
i=0 
root.title("Student Details Software")
frame =tk.Frame(root, bg="lightyellow")
frame.grid(column=0,row=0,sticky=(N,E,W,S))
frame.columnconfigure(0,weight =1)
frame.rowconfigure(0,weight =1)

var = StringVar(root)
var1 =StringVar(root)
var2 =StringVar(root)
var3 =StringVar(root)

#getting entry inputs........

StudentName =StringVar()
year =StringVar()
semester =StringVar()
section =StringVar()
mark1 =StringVar()
mark2 =StringVar()
mark3 =StringVar()
mark4 =StringVar()
mark5 =StringVar()
mark6 =StringVar()
p1 =StringVar()
p2 =StringVar()
p3 =StringVar()
total =StringVar()
average =StringVar()
Grade =StringVar()



e1 =ttk.Entry(frame, width=30, textvariable=StudentName)
e1.grid(column =2, row=1, sticky =(W,E))
e2 =ttk.Entry(frame, width=30, textvariable=mark1)
e2.grid(column =2, row=2, sticky = (W,E))
e3 =ttk.Entry(frame, width=30, textvariable=mark2)
e3.grid(column =2, row=3, sticky = (W,E))
e4 =ttk.Entry(frame, width=30, textvariable=mark3)
e4.grid(column =2, row=4, sticky = (W,E))
e5 =ttk.Entry(frame, width=30, textvariable=mark4)
e5.grid(column =2, row=5, sticky = (W,E))
e6 =ttk.Entry(frame, width=30, textvariable=mark5)
e6.grid(column =2, row=6, sticky = (W,E))
e7 =ttk.Entry(frame, width=30, textvariable=mark6)
e7.grid(column =2, row=7, sticky = (W,E))
e8=ttk.Entry(frame, width=30, textvariable=p1)
e8.grid(column =2, row=8, sticky = (W,E))
e9=ttk.Entry(frame, width=30, textvariable=p2)
e9.grid(column =2, row=9, sticky = (W,E))
e10=ttk.Entry(frame, width=30, textvariable=p3)
e10.grid(column =2, row=10, sticky = (W,E))
e11 =ttk.Entry(frame, width=30, textvariable=total)
e11.grid(column =2, row=11, sticky = (W,E))
e12 =ttk.Entry(frame, width=30, textvariable=average)
e12.grid(column =2, row=12, sticky = (W,E))
e13 =ttk.Entry(frame, width=30, textvariable=Grade)
e13.grid(column =2, row=13, sticky = (W,E))

#h = font.Font(family='Helvetica', size=20, weight='bold')
#total marks goes here.......

def calculate(*args):
    try:
          if StudentName.get().isalpha():   
             val=int(mark1.get())+int(mark2.get())+int(mark3.get())+int(mark4.get())+int(mark5.get())+int(mark6.get())
             total.set(val)     
          else:
              messagebox.showwarning("WARNING","Invalid Name")
#calculating average...

          val1=int(mark1.get())+int(mark2.get())+int(mark3.get())+int(mark4.get())+int(mark5.get())+int(mark6.get())
          avg1 =val1/6
          avg1 =round(avg1,2)
          average.set(avg1)                                                                            
          if avg1 >= 90:
            Grade.set("S")
          elif avg1 >=80 and avg1 <90:
            Grade.set("A")
          elif avg1 >=70 and avg1 <80:
            Grade.set("B")
          elif avg1 >=60 and avg1 <70:
            Grade.set("C")
          elif avg1 >=55 and avg1 <60:
            Grade.set("D")
          elif avg1>=50 and avg1<55:
            Grade.set("E")
          elif avg1 < 50:
            Grade.set("F")
    
    except ValueError:
          messagebox.showwarning("WARNING","you must fill all the entries with valid inputs")

#clearing entries.............
           
def clear(*args):
     e1.delete(0,END)
     e2.delete(0,END)
     e3.delete(0,END)
     e4.delete(0,END)
     e5.delete(0,END)
     e6.delete(0,END)
     e7.delete(0,END)
     e8.delete(0,END)
     e9.delete(0,END)
     e10.delete(0,END)
     e11.delete(0,END)
     e12.delete(0,END)
     e13.delete(0,END)

#pdf part goes here............

v =canvas.Canvas("student.pdf")
v.drawString(0,800,"StudentName")
v.drawString(100,800,"M-IV")
v.drawString(140,800,"ALC")
v.drawString(180,800,"DAA")
v.drawString(220,800,"MPMC")
v.drawString(280,800,"OOP")
v.drawString(320,800,"GIP")
v.drawString(360,800,"P1")
v.drawString(390,800,"P2")
v.drawString(420,800,"P3")
v.drawString(450,800,"total")
v.drawString(490,800,"average")
v.drawString(550,800,"grade")

v.save()

def save():
    global i
    print(var1.get())
    try:
       if StudentName.get().isalpha():   
          val=int(mark1.get())+int(mark2.get())+int(mark3.get())+int(mark4.get())+int(mark5.get())+int(mark6.get())
          #print(str(var.get()))
          value=str(var.get())+str(var1.get())+str(var2.get())+str(var3.get())
       else:
          messagebox.showwarning("WARNING","you must fill all the entries with valid inputs")
    except:
          messagebox.showwarning("WARNING","you must fill all the entries with valid inputs")
    
    f=open("text",'r')
    #f.seek(0)
    #f.truncate()
    if f.read() is "" :
        f=open("text",'w')
        f.write('0')
        f.close()
    f=open("text",'r')    
    g=f.read()
    print(g)
    i =int(g)+40
    #f.write(str(i))
    #h=f.readlines()
    #print(h[len(h)])
    f.close()
    f=open("text",'w')
    f.write(str(i))
    f.close()
    if 800-i <= 0:
        messagebox.showwarning("page full")
        
    packet =io.BytesIO()
    c = canvas.Canvas(packet, pagesize=letter)
    c.drawString(60,820,var.get())
    c.drawString(100,820,var1.get())
    c.drawString(140,820,var2.get())
    c.drawString(80,820,var3.get())
    c.drawString(0,800-i,StudentName.get())
    c.drawString(100,800-i,mark1.get())
    c.drawString(140,800-i,mark2.get())
    c.drawString(180,800-i,mark3.get())
    c.drawString(220,800-i,mark4.get())
    c.drawString(280,800-i,mark5.get())
    c.drawString(320,800-i,mark6.get())
    c.drawString(360,800-i,p1.get())
    c.drawString(390,800-i,p2.get())
    c.drawString(420,800-i,p3.get())
    c.drawString(450,800-i,total.get())
    c.drawString(490,800-i,average.get())
    c.drawString(550,800-i,Grade.get())
    c.save()
    packet.seek(0)
    new_pdf = PdfFileReader(packet)
 
    existing_pdf = PdfFileReader(open("student1.pdf", "rb"))
    output = PdfFileWriter()

    page = existing_pdf.getPage(0)
    page.mergePage(new_pdf.getPage(0))
    output.addPage(page)

    outputStream = open("student1.pdf", "wb")
    output.write(outputStream)
    outputStream.close()


def Exit():
    exit()
#inserting image.......    

img1 =Image.open(r'C:\Users\Venkat\AppData\Local\Programs\Python\Python36-32\smvec1.png')
img2 =img1.resize((75, 75), Image.ANTIALIAS)
img3 = ImageTk.PhotoImage(img2)
b = ttk.Label(root, image = img3)
b.place(x=380, y=180) 

#dropdown list ...

op =OptionMenu(root,var, "2","3","4")
op.place(x=500, y=5)
op1 =OptionMenu(root,var1, "2","3","4","5","6","7","8")
op1.place(x=500, y=40)
op2 =OptionMenu(root,var2, "A","B","C")
op2.place(x=500, y=80)
op3 =OptionMenu(root, var3,"1","2","3","model","model-2")
op3.place(x=500, y=120)
#creating buttons.....
  
#but=ttk.Button(frame, text="ok", command =ok).grid(column=4, row=10,sticky=S)
#ttk.Button(frame, text="next", command =aver).grid(column=3, row=15,sticky=S)
Button(frame, text="calculate", command =calculate,bg="green",fg="white").grid(column=3, row=15,sticky=E)
ttk.Button(frame, text="Clear All", command =clear).grid(column=1, row=15,sticky=S)
ttk.Button(frame, text="Save", command =save).grid(column=2,row=15, sticky=S)
ttk.Button(frame, text="Exit", command =Exit).grid(column=4,row=15, sticky=S)

#creating labels....

Label(frame, text="Student Name\n", width =20, fg="red").grid(column=1, row=1, sticky =W)
ttk.Label(frame, text="Year\t", width =20).grid(column=3, row=1, sticky =E)
ttk.Label(frame, text="Semester\t", width =20).grid(column=3, row=2, sticky =E)
ttk.Label(frame, text="Section\t", width =20).grid(column=3, row=3, sticky =E)
ttk.Label(frame, text="M-IV\n", width=20).grid(column=1, row=2, sticky =W)
ttk.Label(frame, text="DAA\n", width =20).grid(column=1, row=3, sticky =W)
ttk.Label(frame, text="MPMC\n", width =20).grid(column=1, row=4, sticky =W)
ttk.Label(frame, text="GIP\n", width =20).grid(column=1, row=5, sticky =W)
ttk.Label(frame, text="ALC\n", width =20).grid(column=1, row=6, sticky =W)
ttk.Label(frame, text="OOP\n", width =20).grid(column=1, row=7, sticky =W)
ttk.Label(frame, text="P-I\n", width =20).grid(column=1, row=8, sticky =W)
ttk.Label(frame, text="P-II\n", width =20).grid(column=1, row=9, sticky =W)
ttk.Label(frame, text="P-III\n", width =20).grid(column=1, row=10, sticky =W)
ttk.Label(frame, text="Total \n", width =20).grid(column=1, row=11, sticky =W)
ttk.Label(frame, text="Average \n", width =20).grid(column=1, row=12, sticky =W)
Label(frame, text="Grade \n", width =20,fg="blue").grid(column=1, row=13, sticky =W)
ttk.Label(frame, text="Internal", width =20).grid(column=3, row=4, sticky =E)
#polishing the frame...

for child in frame.winfo_children(): child.grid_configure(padx=2 , pady=2)
e1.focus()

root.bind('<Return>',calculate)
root.resizable(width =False, height=False)

#making the GUI infinte...

root.mainloop()
