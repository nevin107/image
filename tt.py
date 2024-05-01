import tkinter
t=tkinter.Tk()
t.geometry('500x500')


label1=tkinter.Label(t,text="User Name",background="green",width=20)
label2=tkinter.Label(t,text="password",background="blue",width=20)
label3=tkinter.Label(t,text="Captcha",background="pink",width=20)
text1=tkinter.Entry(t,text="Text1",background="Orange",width=20)
text2=tkinter.Entry(t,text="Text2",background="Orange",width=20)
button1=tkinter.Button(t,text="Click me",background="blue")

var=tkinter.StringVar()
r1 = tkinter.Radiobutton(t, text="Female", variable=var, value="Female")
r2 = tkinter.Radiobutton(t, text="Male", variable=var, value="Male")
a=str(var.get())
label4=tkinter.Label(t,text="hai"+a)

checkvar1 = tkinter.IntVar()  
checkvar2 = tkinter.IntVar()  
checkvar3 =tkinter.IntVar()  
chkbtn1 = tkinter.Checkbutton(t, text = "C", variable = checkvar1, onvalue = 1, height = 2, width = 10)  
chkbtn2 = tkinter.Checkbutton(t, text = "C++", variable = checkvar2, onvalue = 1, offvalue = 0, height = 2, width = 10)  
chkbtn3 = tkinter.Checkbutton(t, text = "Java", variable = checkvar3, onvalue = 1, offvalue = 0, height = 2, width = 10)  

menu=tkinter.StringVar()
menu.set("Select Color")


drop1=tkinter.OptionMenu(t,menu,"Red","Green","blue","pink")


label1.grid(row=0,column=0)
label2.grid(row=1,column=0)
label3.grid(row=2,column=0)
text1.grid(row=0,column=1)
text2.grid(row=1,column=1)
button1.grid(row=3,columnspan=3)
r1.grid(row=4,column=1)
r2.grid(row=5,column=1)
label4.grid(row=6,column=1)

chkbtn1.grid(row=7,column=1)  
chkbtn2.grid(row=7,column=2)
chkbtn3.grid(row=7,column=3)

drop1.grid(row=8,column=3)
tkinter.mainloop()