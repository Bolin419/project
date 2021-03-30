import tkinter
from PIL import Image, ImageTk
import csv

def center_window(top,w, h):
    # 获取屏幕 宽、高
    ws = top.winfo_screenwidth()
    hs = top.winfo_screenheight()
    # 计算 x, y 位置
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    top.geometry('%dx%d+%d+%d' % (w, h, x, y))




top = tkinter.Tk()


top.title('Fantasy League Team')
center_window(top,1000,600)


Ima1 = Image.open('/Users/zbl/Desktop/1.png')
Ima1=Ima1.resize((120, 85),Image.ANTIALIAS)
Ima2 = Image.open('/Users/zbl/Desktop/player photo/Manu-Ginobili-2K.png')
Ima2=Ima2.resize((120, 85),Image.ANTIALIAS)
Ima3 = Image.open('/Users/zbl/Desktop/player photo/Karl-Malone-2K.png')
Ima3=Ima3.resize((120, 85),Image.ANTIALIAS)
Ima4 = Image.open('/Users/zbl/Desktop/player photo/Tony-Parker-2K.png')
Ima4=Ima4.resize((120, 85),Image.ANTIALIAS)

Ima5 = Image.open('/Users/zbl/Desktop/player photo/Shawn-Kemp-2K.png')
Ima5=Ima5.resize((120, 85),Image.ANTIALIAS)
Ima6 = Image.open('/Users/zbl/Desktop/player photo/Allen-Iverson-2K.png')
Ima6=Ima6.resize((120, 85),Image.ANTIALIAS)
Ima7 = Image.open('/Users/zbl/Desktop/player photo/Amare-Stoudemire-2K.png')
Ima7=Ima7.resize((120, 85),Image.ANTIALIAS)
Ima8 = Image.open('/Users/zbl/Desktop/player photo/Paul-Pierce-2K-1.png')
Ima8=Ima8.resize((120, 85),Image.ANTIALIAS)



p1 = ImageTk.PhotoImage(Ima1)
p2 = ImageTk.PhotoImage(Ima2)
p3 = ImageTk.PhotoImage(Ima3)
p4 = ImageTk.PhotoImage(Ima4)

p5 = ImageTk.PhotoImage(Ima1)
p6 = ImageTk.PhotoImage(Ima2)
p7 = ImageTk.PhotoImage(Ima3)
p8 = ImageTk.PhotoImage(Ima4)



button1=tkinter.Button(image=pt)
button1.place(x=250,y=50)
button2=tkinter.Button(image=pt2)
button2.place(x=370,y=50)
button3=tkinter.Button(image=pt3)
button3.place(x=490,y=50)
button4=tkinter.Button(image=pt4)
button4.place(x=610,y=50)

Label1=tkinter.Label(text="YAO MIng"+'(Rocket)')
Label1.place(x=250,y=145)
Label2=tkinter.Label(text="Manu Ginobili"+'(Spurs)')
Label2.place(x=370,y=145)
Label3=tkinter.Label(text="Manu Ginobili"+'(Spurs)')
Label3.place(x=490,y=145)
Label4=tkinter.Label(text="Manu Ginobili"+'(Spurs)')
Label4.place(x=610,y=145)






#button1= tkinter.Button(top,text='Start',fg='red',font=('黑体', 10),)
#button1.place(x=400,y=240)



img1 = tkinter.Label(text='player1', font=('黑体', 15),fg='Goldenrod')
img1.place(x=40, y=250)

img2 = tkinter.Label(text='player2', font=('黑体', 15),fg='Goldenrod')
img2.place(x=40, y=300)

img3 = tkinter.Label(text='player3', font=('黑体', 15),fg='Goldenrod')
img3.place(x=40, y=350)

img4 = tkinter.Label(text='player4', font=('黑体', 15),fg='Goldenrod')
img4.place(x=40, y=400)

img5 = tkinter.Label(text='player5', font=('黑体', 15),fg='Goldenrod')
img5.place(x=40, y=450)


finish_button=tkinter.Button(top,text='exit',command=top.quit)
finish_button.place(x=890,y=550)

top.mainloop()