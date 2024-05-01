import tkinter as tk

t = tk.Tk()
t.geometry('500x500')
label23=tk.Label(t,text="ggfhjf",fg="black",font=("arial",15))
label23.grid(rows=5,column=2)
label1 = tk.Label(t, text="User Name", background="green", width=20)
label2 = tk.Label(t, text="password", background="blue", width=20)
label3 = tk.Label(t, text="Captcha", background="pink", width=20)
text1 = tk.Entry(t, text="Text1", background="Orange", width=20)
text2 = tk.Entry(t, text="Text2", background="Orange", width=20)
button1 = tk.Button(t, text="Click me", background="blue")

var = tk.StringVar()
r1 = tk.Radiobutton(t, text="Female", variable=var, value="Female")
r2 = tk.Radiobutton(t, text="Male", variable=var, value="Male")
label4 = tk.Label(t, text="hai")

checkvar1 = tk.IntVar()  
checkvar2 = tk.IntVar()  
checkvar3 = tk.IntVar()  
chkbtn1 = tk.Checkbutton(t, text="C", variable=checkvar1, onvalue=1, height=2, width=10)  
chkbtn2 = tk.Checkbutton(t, text="C++", variable=checkvar2, onvalue=1, offvalue=0, height=2, width=10)  
chkbtn3 = tk.Checkbutton(t, text="Java", variable=checkvar3, onvalue=1, offvalue=0, height=2, width=10)  

menu = tk.StringVar()
menu.set("Select Color")
drop1 = tk.OptionMenu(t, menu, "Red", "Green", "blue", "pink")

label1.grid(row=0, column=0)
label2.grid(row=1, column=0)
label3.grid(row=2, column=0)
text1.grid(row=0, column=1)
text2.grid(row=1, column=1)
button1.grid(row=3, columnspan=3)
r1.grid(row=4, column=1)
r2.grid(row=5, column=1)
label4.grid(row=6, column=1)

chkbtn1.grid(row=7, column=1)  
chkbtn2.grid(row=7, column=2)
chkbtn3.grid(row=7, column=3)

drop1.grid(row=8, column=3)

tk.mainloop()
