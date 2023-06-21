from tkinter import *
from tkinter import ttk
root=Tk() #สร้างหน้าต่างชื่อ root

#กำหนด font และขนาดตัวอักษร ของหน้าต่าง root
root.option_add("*font",'JasmineUPC 28 bold') 

root.title('Ticket Calculator') #ข้อความ title ส่วนหัวโปรแกรม
root.geometry('430x300') #กำหนดขนาดหน้าจอ
root.resizable(False ,False)

#สร้าง Label ชื่อ title1 สำหรับแสดงข้อความ
title1=Label(text='โปรแกรมคำนวณค่าบัตรผ่านประตู',fg='gold',bg='SlateBlue4')
title1.place(x=5,y=0) #กำหนดตำแหน่งของข้อความ

#สร้าง Label ชื่อ lb1 และกำหนดตำแหน่ง
lb1=Label(root,text='ป้อนจำนวนคน: ',bg='OliveDrab1') 
lb1.place(x=10,y=60)

#กำหนด en1 เป็นชนิด Entry และกำหนดตำแหน่ง
#justify=RIGHT คือการกำหนดให้ตำแหน่งในการพิมพ์ในกล่องข้อความให้เริ่มจากขวา
en1=Entry(root,width=11,justify=RIGHT) 
en1.place(x=210,y=60)

#สร้าง Label ชื่อ lb2 และกำหนดตำแหน่ง
lb2=Label(root,text='เลือกเพศ: ',bg='OliveDrab1') 
lb2.place(x=10,y=110)

#สร้าง Combobox ชื่อ cb1 มีตัวเลือก ชาย,หญิง และกำหนดตำแหน่ง
cb1=ttk.Combobox(root,width=10,value=["ชาย","หญิง"]) 
cb1.place(x=210,y=110)

#กำหนด lb3 เป็นป้ายข้อความเปล่าไว้แสดงผลลัพธ์
lb3=Label(root,text='',fg='OrangeRed2') 
lb3.place(x=100,y=240)

def cal(): #สร้างฟังก์ชันชื่อ cal ใช้คำนวณราคา
    num=int(en1.get()) #กำหนดตัวแปร num รับค่าจาก en1 โดยแปลงเป็น int
    if cb1.get()=='ชาย': #เปรียบเทียบเงื่อนไขโดยรับค่าจาก cb1
        total=num*50
    else:
        total=num*30
    #กำหนดผลลัพธ์ที่จะแสดงใน lb3
    lb3.configure(text='ค่าบัตร = '+str(total)+' บาท')

#คำสั่งสร้างปุ่มชื่อ btn เมื่อกดปุ่มให้เรียกใช้ฟังก์ชัน cal
btn=Button(root,text='คำนวณ',command=cal,bg='SeaGreen1') 
btn.place(x=150,y=165)

en1.focus() #กำหนดให้เคอร์เซอร์เริ่มที่ตำแหน่งกล่องข้อความ en1
cb1.current(0) #กำหนดให้ combobox cb1 เลือก item แรกไว้
root.mainloop()