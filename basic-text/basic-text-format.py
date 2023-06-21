from tkinter import *  
root = Tk() #สร้างหน้าต่างชื่อ root

#กำหนด font และขนาดตัวอักษร ของหน้าต่าง root
root.option_add("*font",'JasmineUPC 28 bold') 

root.title('My school')
root.geometry('400x200') 
root.resizable(False ,False)

title1=Label(text='โรงเรียนกาญจนาภิเษกวิทยาลัย',fg='gold',bg='SlateBlue4')
title1.place(x=10,y=0)

title2=Label(text='นครปฐม',fg='DarkRed',bg='HotPink')
title2.place(x=140,y=50)

title3=Label(text='(พระตำหนักสวนกุหลาบมัธยม)',fg='DarkMagenta',bg='Gold')
title3.place(x=15,y=100)
root.mainloop()

#ดูสีเพิ่มเติม search: css color