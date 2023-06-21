from tkinter import *
root = Tk()
root.option_add("*font",'JasmineUPC 28 bold') 
root.title('My school')
root.geometry('800x800') 
root.resizable(False ,False)

lb1=Label(text='เลือกโปเกมอนของคุณ',fg='white',bg='red')
lb1.place(x=280,y=20)
lb2=Label(text='',fg='DarkBlue')
lb2.place(x=280,y=700)

photo1 = PhotoImage(file="001.png")
photo2 = PhotoImage(file="004.png")
photo3 = PhotoImage(file="007.png")

def option1():
    img1=Label(root,image=photo1).place(x=200,y=200)
    lb2.configure(text='Bulbasaur #0001')
def option2():
    img1=Label(root,image=photo2).place(x=200,y=200)
    lb2.configure(text='Charmander #0004')
def option3():
    img1=Label(root,image=photo3).place(x=200,y=200)
    lb2.configure(text='Squirtle #0007')
    
btn1=Button(root,text='GREEN',command=option1,bg='ForestGreen').place(x=100,y=120)
btn2=Button(root,text='RED',command=option2,bg='Crimson').place(x=350,y=120)
btn3=Button(root,text='BLUE',command=option3,bg='DeepSkyBlue').place(x=600,y=120)
root.mainloop()
#ทำเพิ่มเป็น 5 ปุ่ม รูปการ์ตูนอะไรก็ได้
