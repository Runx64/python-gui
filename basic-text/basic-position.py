'''method pack'''
from tkinter import *  
root = Tk()
root.title('my first GUI')
root.geometry('200x200')
label1=Label(text='My Profile')
label1.pack()
label2=Label(text='I am your father.')
label2.pack()
label3=Label(text='How are you?')
label3.pack()
root.mainloop()

'''method place ยึดตำแหน่งตามค่า x,y (ลองแก้ให้แสดงผลเหมือนอันแรก)'''
from tkinter import *  
root = Tk()
root.title('my first GUI')
root.geometry('200x200')
label1=Label(text='My Profile')
label1.place(x=0,y=0)
label2=Label(text='I am your father.')
label2.place(x=0,y=100)
label3=Label(text='How are you?')
label3.place(x=100,y=100)
root.mainloop()

'''method grid ยึดตำแหน่งตามค่า row,column (ลองแก้ให้แสดงผลเรียงเป็นขั้นบันไดลงมา)'''
from tkinter import *  
root = Tk()
root.title('my first GUI')
root.geometry('200x200')
label1=Label(text='My Profile')
label1.grid(row=0,column=0)
label2=Label(text='I am your father.')
label2.grid(row=0,column=1)
label3=Label(text='How are you?')
label3.grid(row=1,column=1)
root.mainloop()