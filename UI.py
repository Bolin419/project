import tkinter
import PIL

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
center_window(top,1000,700)


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

Ima9 = Image.open('/Users/zbl/Desktop/player photo/Steve-Nash-2K.png')
Ima9=Ima9.resize((120, 85),Image.ANTIALIAS)
Ima10 = Image.open('/Users/zbl/Desktop/player photo/Scottie-Pippen-2K.png')
Ima10=Ima10.resize((120, 85),Image.ANTIALIAS)
Ima11 = Image.open('/Users/zbl/Desktop/player photo/Shaquille-ONeal-2K.png')
Ima11=Ima11.resize((120, 85),Image.ANTIALIAS)
Ima12 = Image.open('/Users/zbl/Desktop/player photo/Stephen-Curry-2K.png')
Ima12=Ima12.resize((120, 85),Image.ANTIALIAS)

Ima13 = Image.open('/Users/zbl/Desktop/player photo/Kobe-Bryant-Prime-2K.png')
Ima13=Ima13.resize((120, 85),Image.ANTIALIAS)
Ima14 = Image.open('/Users/zbl/Desktop/player photo/Magic-Johnson-2K.png')
Ima14=Ima14.resize((120, 85),Image.ANTIALIAS)
Ima15 = Image.open('/Users/zbl/Desktop/player photo/Michael-Jordan-2K.png')
Ima15=Ima15.resize((120, 85),Image.ANTIALIAS)
Ima16 = Image.open('/Users/zbl/Desktop/player photo/LeBron-James-Miami-Heat-2K.png')
Ima16=Ima16.resize((120, 85),Image.ANTIALIAS)

Ima17 = Image.open('/Users/zbl/Desktop/player photo/Carmelo-Anthony-Denver-Nuggers-2K.png')
Ima17=Ima17.resize((120, 85),Image.ANTIALIAS)
Ima18 = Image.open('/Users/zbl/Desktop/player photo/Larry-Bird-2K.png')
Ima18=Ima18.resize((120, 85),Image.ANTIALIAS)
Ima19 = Image.open('/Users/zbl/Desktop/player photo/Klay-Thompson-2K.png')
Ima19=Ima19.resize((120, 85),Image.ANTIALIAS)
Ima20 = Image.open('/Users/zbl/Desktop/player photo/Kareem-Abdul-Jabbar-LA-Lakers-2K.png')
Ima20=Ima20.resize((120, 85),Image.ANTIALIAS)

p1 = ImageTk.PhotoImage(Ima1)
p2 = ImageTk.PhotoImage(Ima2)
p3 = ImageTk.PhotoImage(Ima3)
p4 = ImageTk.PhotoImage(Ima4)

p5 = ImageTk.PhotoImage(Ima5)
p6 = ImageTk.PhotoImage(Ima6)
p7 = ImageTk.PhotoImage(Ima7)
p8 = ImageTk.PhotoImage(Ima8)

p9 = ImageTk.PhotoImage(Ima9)
p10 = ImageTk.PhotoImage(Ima10)
p11 = ImageTk.PhotoImage(Ima11)
p12 = ImageTk.PhotoImage(Ima12)

p13 = ImageTk.PhotoImage(Ima13)
p14 = ImageTk.PhotoImage(Ima14)
p15 = ImageTk.PhotoImage(Ima15)
p16 = ImageTk.PhotoImage(Ima16)

p17 = ImageTk.PhotoImage(Ima17)
p18 = ImageTk.PhotoImage(Ima18)
p19 = ImageTk.PhotoImage(Ima19)
p20 = ImageTk.PhotoImage(Ima20)


button1=tkinter.Button(image=p1)
button1.place(x=250,y=50)
button2=tkinter.Button(image=p2)
button2.place(x=370,y=50)
button3=tkinter.Button(image=p3)
button3.place(x=490,y=50)
button4=tkinter.Button(image=p4)
button4.place(x=610,y=50)


button5=tkinter.Button(image=p5)
button5.place(x=250,y=165)
button6=tkinter.Button(image=p6)
button6.place(x=370,y=165)
button7=tkinter.Button(image=p7)
button7.place(x=490,y=165)
button8=tkinter.Button(image=p8)
button8.place(x=610,y=165)

button9=tkinter.Button(image=p9)
button9.place(x=250,y=280)
button10=tkinter.Button(image=p10)
button10.place(x=370,y=280)
button11=tkinter.Button(image=p11)
button11.place(x=490,y=280)
button12=tkinter.Button(image=p12)
button12.place(x=610,y=280)

button13=tkinter.Button(image=p13)
button13.place(x=250,y=395)
button14=tkinter.Button(image=p14)
button14.place(x=370,y=395)
button15=tkinter.Button(image=p15)
button15.place(x=490,y=395)
button16=tkinter.Button(image=p16)
button16.place(x=610,y=395)

button17=tkinter.Button(image=p17)
button17.place(x=250,y=510)
button18=tkinter.Button(image=p18)
button18.place(x=370,y=510)
button19=tkinter.Button(image=p19)
button19.place(x=490,y=510)
button20=tkinter.Button(image=p20)
button20.place(x=610,y=510)



Label1=tkinter.Label(text="Yao ming"+'(Rocket)')
Label1.place(x=250,y=145)
Label2=tkinter.Label(text="Player name"+'(team)')
Label2.place(x=370,y=145)
Label3=tkinter.Label(text="Player name"+'(team)')
Label3.place(x=490,y=145)
Label4=tkinter.Label(text="Player name"+'(team)')
Label4.place(x=610,y=145)

Label5=tkinter.Label(text="Player name"+'(Rocket)')
Label5.place(x=250,y=260)
Label6=tkinter.Label(text="Player name"+'(team)')
Label6.place(x=370,y=260)
Label7=tkinter.Label(text="Player name"+'(team)')
Label7.place(x=490,y=260)
Label8=tkinter.Label(text="Player name"+'(team)')
Label8.place(x=610,y=260)

Label9=tkinter.Label(text="Player name"+'(Rocket)')
Label9.place(x=250,y=375)
Label10=tkinter.Label(text="Player name"+'(team)')
Label10.place(x=370,y=375)
Label11=tkinter.Label(text="Player name"+'(team)')
Label11.place(x=490,y=375)
Label12=tkinter.Label(text="Player name"+'(team)')
Label12.place(x=610,y=375)

Label13=tkinter.Label(text="Player name"+'(Rocket)')
Label13.place(x=250,y=490)
Label14=tkinter.Label(text="Player name"+'(team)')
Label14.place(x=370,y=490)
Label15=tkinter.Label(text="Player name"+'(team)')
Label15.place(x=490,y=490)
Label16=tkinter.Label(text="Player name"+'(team)')
Label16.place(x=610,y=490)

Label17=tkinter.Label(text="Player name"+'(team)')
Label17.place(x=250,y=605)
Label18=tkinter.Label(text="Player name"+'(team)')
Label18.place(x=370,y=605)
Label19=tkinter.Label(text="Player name"+'(team)')
Label19.place(x=490,y=605)
Label20=tkinter.Label(text="Player name"+'(team)')
Label20.place(x=610,y=605)





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



img6 = tkinter.Label(text='player6', font=('黑体', 15),fg='Goldenrod')
img6.place(x=900, y=250)

img7 = tkinter.Label(text='player7', font=('黑体', 15),fg='Goldenrod')
img7.place(x=900, y=300)

img8 = tkinter.Label(text='player8', font=('黑体', 15),fg='Goldenrod')
img8.place(x=900, y=350)

img9 = tkinter.Label(text='player9', font=('黑体', 15),fg='Goldenrod')
img9.place(x=900, y=400)

img10 = tkinter.Label(text='player10', font=('黑体', 15),fg='Goldenrod')
img10.place(x=900, y=450)


finish_button=tkinter.Button(top,text='exit',command=top.quit)
finish_button.place(x=890,y=550)

top.mainloop()