import tkinter 
import tkinter as tk
root=tk.Tk()
root.geometry("500x500")
root.title("REGISTRATION FORM")


label1=tk.Label(root,text="User Registrion Form",fg="RED",width=20,font=("Arial",15))
label1.grid(row=6,column=1)
label1=tk.Label(root,text="NAME:",width=10,fg="blue")
label2=tk.Label(root,text="COUNTRY:",fg="blue",width=10)
label1.grid(row=0,column=0)
label2.grid(row=2,column=0)
text1=tk.Entry(root,text="",background="grey")
text2=tk.Entry(root,text="")
text1.grid(row=0,column=1)
text2.grid(row=2,column=1)
label4=tk.Label(root,text="GENDER:",width=10,fg="blue")
label4.grid(row=1,column=0)

var=tk.IntVar()
radio=tk.Radiobutton(root,text="MALE",variable=var,fg="green",value=1)
radio2=tk.Radiobutton(root,text="FEMALE",variable=var,fg="green",value=2)
radio.grid(row= 1, column=1)
radio2.grid(row= 1, column= 2)
label3=tk.Label(root,text="HOBBIES:",fg="blue",width=10)
label3.grid(row=3,column=0)

check1=tk.Checkbutton(root,text="volleyball",fg="orange")
check2=tk.Checkbutton(root,text="pc games",fg="orange")
check3=tk.Checkbutton(root,text="football",fg="orange")
check4=tk.Checkbutton(root,text="videography",fg="orange")
check1.grid(row=3,column=1)
check2.grid(row=3,column=2)
check3.grid(row=4,column=1)
check4.grid(row=4,column=2)

bottn=tk.Button(root,text="submit",background="grey",width=10)
bottn.grid(row=5,column=1)

menu=tk.StringVar()
menu.set("course")

option=tk.OptionMenu(root,menu,"jee","cusat","keam")
option.grid(row=6,column=3)


tk.mainloop()