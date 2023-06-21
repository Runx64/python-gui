from tkinter import *  
root = Tk()
root.option_add("*font",'JasmineUPC 28 bold') 

root.title('My school')
root.geometry('600x800') 
root.resizable(False ,False)

photo1 = PhotoImage(file="kjn_logo.png")     
img1=Label(root,image=photo1).place(x=120,y=0)

title1=Label(text='โรงเรียนกาญจนาภิเษกวิทยาลัย',fg='gold',bg='SlateBlue4')
title1.place(x=100,y=500)

root.mainloop()