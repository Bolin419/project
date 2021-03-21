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
center_window(top,800,480)

#按钮
submit_button = tkinter.Button(top, text ="开始模拟", font=('黑体', 10),fg='red',width=10,height=2,)
submit_button.place(x=350, y=200)
submit_button2 = tkinter.Button(top, text ="球员数据", font=('黑体', 10),fg='red',width=10,height=2,)
submit_button2.place(x=350, y=250)
submit_button2 = tkinter.Button(top, text ="球队战绩", font=('黑体', 10),width=10,height=2,)
submit_button2.place(x=350, y=300)


#LOGO
load = Image.open("/Users/zbl/Desktop/nba-logo.png")
load = load.resize((420, 130),Image.ANTIALIAS)
render = ImageTk.PhotoImage(load)
img5 = tkinter.Label(image=render)
img5.place(x=200, y=0)

#label
img8 = tkinter.Label(text='金币：0', font=('黑体',10),fg='Goldenrod')
img8.place(x=10, y=5)
img9 = tkinter.Label(text='球队战力：0', font=('黑体',10),fg='red')
img9.place(x=10, y=30)
#top.mainloop()