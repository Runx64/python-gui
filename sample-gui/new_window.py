# โปรแกรมทดลองสร้างหน้าต่างใหม่
from tkinter import *
from tkinter.ttk import *
 
# creates a Tk() object
root = Tk()
root.geometry("400x400")
 
def window1():
    # Set Toplevel object which will
    window1 = Toplevel(root)
    window1.title("New Window")
    window1.geometry("400x400")
    # Set background for Toplevel
    window1['bg']='blue'
    # A Label widget to show in toplevel
    Label(window1,text ="This is Window1").pack(pady = 10)
    
def window2():
    # Set Toplevel object which will
    window2 = Toplevel(root)
    window2.title("New Window2")
    window2.geometry("400x400")
    # Set background for Toplevel
    window2['bg']='green'
    # A Label widget to show in toplevel
    Label(window2,text ="This is Window2").pack(pady = 10)
 
btn = Button(root,text ="Click to open Window1",command = window1)
btn.pack(pady = 10)
btn2 = Button(root,text ="Click to open Window2",command = window2)
btn2.pack(pady = 10) 
# mainloop, runs infinitely
mainloop()

# เขียนโปรแกรมคำนวณพื้นที่รูปเรขาคณิตอะไรก็ได้ 3 รูป แยกเป็น 3 หน้าต่าง(window) หน้าต่างละ 1 รูป
