import tkinter
import PIL
import random
from PIL import Image, ImageTk
import csv



def center_window(top, w, h):
    # 获取屏幕 宽、高
    ws = top.winfo_screenwidth()
    hs = top.winfo_screenheight()
    # 计算 x, y 位置
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)
    top.geometry('%dx%d+%d+%d' % (w, h, x, y))

top3 = tkinter.Tk()

currentchoice = ""


center_window(top3,500,500)
top3.title('New Fantasy')
bg = Image.open('/Users/zbl/Desktop/nba-logo.png')
bg = bg.resize((500, 500), Image.ANTIALIAS)
background = ImageTk.PhotoImage(bg)
canvas1 = tkinter.Canvas(top3, width=500,
                 height=500)

canvas1.pack(fill="both", expand=True)

# Display image
canvas1.create_image(0, 0, image=background,anchor="nw")

# Add Text
canvas1.create_text(250, 100,font=('Pursia',30), text="Welcome" ,fill='Yellow')


# set for turn and
def decide_turn():
    small = 1
    big = 6
    if random.randint(small, big) <= 3:
        turn = 0
        order = 0  # 0 means player1
        print('player 1 choose first')
        return order, turn
    else:
        turn = 0
        order = 1  # means player 2
        print('player 2 choose first')
        return order, turn

csv_file = csv.reader(open('球员1.csv', 'r', encoding='utf8'))

# print(csv_file)
content = []
for i in csv_file:
    content.append(i)
content.remove(['\ufeffNo.', 'Team name', 'Player name', 'rating'])

def generate_list1():
    UI_list1 = []
    for i in content:
        if int(i[3]) >= 96:
            UI_list1.append(i)
    return UI_list1

def generate_list2():
    UI_list2 = []
    for i in content:
        if 92 <= int(i[3]) < 96:
            UI_list2.append(i)
    return UI_list2

def generate_list3():
    UI_list3 = []
    for i in content:
        if 88 <= int(i[3]) < 92:
            UI_list3.append(i)
    return UI_list3

def generate_list4():
    UI_list4 = []
    for i in content:
        if 84 <= int(i[3]) < 88:
            UI_list4.append(i)
    return UI_list4

def generate_list5():
    UI_list5 = []
    for i in content:
        if 80 <= int(i[3]) < 84:
            UI_list5.append(i)
    return UI_list5

def randPlaye1():
    ranlist = random.sample(range(0, 10), 4)
    x = generate_list1()
    UIplayer1 = []
    for i in ranlist:
        UIplayer1.append(x[i])
    return UIplayer1

def randPlaye2():
    ranlist = random.sample(range(0, 12), 4)
    x = generate_list2()
    UIplayer2 = []
    for i in ranlist:
        UIplayer2.append(x[i])
    return UIplayer2

def randPlaye3():
    ranlist = random.sample(range(0, 8), 4)
    x = generate_list3()
    UIplayer3 = []
    for i in ranlist:
        UIplayer3.append(x[i])
    return UIplayer3

def randPlaye4():
    ranlist = random.sample(range(0, 12), 4)
    x = generate_list4()
    UIplayer4 = []
    for i in ranlist:
        UIplayer4.append(x[i])
    return UIplayer4

def randPlaye5():
    ranlist = random.sample(range(0, 5), 4)
    x = generate_list5()
    UIplayer5 = []
    for i in ranlist:
        UIplayer5.append(x[i])
    return UIplayer5

T1 = randPlaye1()
Ima1 = Image.open('player photo/' + T1[0][2] + '.png')
Ima1 = Ima1.resize((120, 85), Image.ANTIALIAS)
Ima2 = Image.open('player photo/' + T1[1][2] + '.png')
Ima2 = Ima2.resize((120, 85), Image.ANTIALIAS)
Ima3 = Image.open('player photo/' + T1[2][2] + '.png')
Ima3 = Ima3.resize((120, 85), Image.ANTIALIAS)
Ima4 = Image.open('player photo/' + T1[3][2] + '.png')
Ima4 = Ima4.resize((120, 85), Image.ANTIALIAS)

T2 = randPlaye2()
Ima5 = Image.open('player photo/' + T2[0][2] + '.png')
Ima5 = Ima5.resize((120, 85), Image.ANTIALIAS)
Ima6 = Image.open('player photo/' + T2[1][2] + '.png')
Ima6 = Ima6.resize((120, 85), Image.ANTIALIAS)
Ima7 = Image.open('player photo/' + T2[2][2] + '.png')
Ima7 = Ima7.resize((120, 85), Image.ANTIALIAS)
Ima8 = Image.open('player photo/' + T2[3][2] + '.png')
Ima8 = Ima8.resize((120, 85), Image.ANTIALIAS)

T3 = randPlaye3()
Ima9 = Image.open('player photo/' + T3[0][2] + '.png')
Ima9 = Ima9.resize((120, 85), Image.ANTIALIAS)
Ima10 = Image.open('player photo/' + T3[1][2] + '.png')
Ima10 = Ima10.resize((120, 85), Image.ANTIALIAS)
Ima11 = Image.open('player photo/' + T3[2][2] + '.png')
Ima11 = Ima11.resize((120, 85), Image.ANTIALIAS)
Ima12 = Image.open('player photo/' + T3[3][2] + '.png')
Ima12 = Ima12.resize((120, 85), Image.ANTIALIAS)

T4 = randPlaye4()
Ima13 = Image.open('player photo/' + T4[0][2] + '.png')
Ima13 = Ima13.resize((120, 85), Image.ANTIALIAS)
Ima14 = Image.open('player photo/' + T4[1][2] + '.png')
Ima14 = Ima14.resize((120, 85), Image.ANTIALIAS)
Ima15 = Image.open('player photo/' + T4[2][2] + '.png')
Ima15 = Ima15.resize((120, 85), Image.ANTIALIAS)
Ima16 = Image.open('player photo/' + T4[3][2] + '.png')
Ima16 = Ima16.resize((120, 85), Image.ANTIALIAS)

T5 = randPlaye5()
Ima17 = Image.open('player photo/' + T5[0][2] + '.png')
Ima17 = Ima17.resize((120, 85), Image.ANTIALIAS)
Ima18 = Image.open('player photo/' + T5[1][2] + '.png')
Ima18 = Ima18.resize((120, 85), Image.ANTIALIAS)
Ima19 = Image.open('player photo/' + T5[2][2] + '.png')
Ima19 = Ima19.resize((120, 85), Image.ANTIALIAS)
Ima20 = Image.open('player photo/' + T5[3][2] + '.png')
Ima20 = Ima20.resize((120, 85), Image.ANTIALIAS)

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

# 14589 236710

turn = int(decide_turn()[1])
# print(turn)
order = int(decide_turn()[0])
print(order)
playerTeam = []
robTeam = []

def final_page():
    top2=tkinter.Toplevel()
    top2.title('Final Rating Page')
    center_window(top2, 500, 350)
    lab1=tkinter.Label(top2,text='rating for Team1')
    lab1.pack()
    lab2=tkinter.Label(top2,text='rating for Team2')
    lab2.pack()

def update_label(lab):
    if order == 0:
        if turn == 0:
            lab.place(x=40, y=250)
        if turn == 1:
            lab.place(x=900, y=250)
        if turn == 2:
            lab.place(x=900, y=300)
        if turn == 3:
            lab.place(x=40, y=300)
        if turn == 4:
            lab.place(x=40, y=350)
        if turn == 5:
            lab.place(x=900, y=350)
        if turn == 6:
            lab.place(x=900, y=400)
        if turn == 7:
            lab.place(x=40, y=400)
        if turn == 8:
            lab.place(x=40, y=450)
        if turn == 9:
            lab.place(x=900, y=450)

    if order == 1:
        if turn == 0:
            lab.place(x=900, y=250)
        if turn == 1:
            lab.place(x=40, y=250)
        if turn == 2:
            lab.place(x=40, y=300)
        if turn == 3:
            lab.place(x=900, y=300)
        if turn == 4:
            lab.place(x=900, y=350)
        if turn == 5:
            lab.place(x=40, y=350)
        if turn == 6:
            lab.place(x=40, y=400)
        if turn == 7:
            lab.place(x=900, y=400)
        if turn == 8:
            lab.place(x=900, y=450)
        if turn == 9:
            lab.place(x=40, y=450)



pool = []
for player in T1 + T2 + T3 + T4 + T5:
    pool.append(player[2])

p = []
for i in T1 + T2 + T3 + T4 + T5:
    p.append(i)

def cost(Str):
    money = 0
    for i in p:
        if Str == i[2]:
            if int(i[3]) >= 96:
                money = 5
            if 92 <= int(i[3]) < 96:
                money = 4
            if 88 <= int(i[3]) < 92:
                money = 3
            if 84 <= int(i[3]) < 88:
                money = 2
            if 80 <= int(i[3]) < 84:
                money = 1
    return int(money)

player_money = 19
robot_money = 19





def rob(pool, order, turn, money):
    for player in pool:
        for choice in T3:
            if choice[2] == player:
                return player
        for choice in T4:
            if choice[2] == player:
                return player
        for choice in T5:
            if choice[2] == player:
                return player

def check():
    print('robTeam',robTeam)
    print('playerTeam',playerTeam)



def start():
    top = tkinter.Toplevel()
    top.title('Fantasy League Team')
    center_window(top, 1000, 700)

    def okfunction():
        global turn
        selected = ""

        if order == 0:
            if turn == 0 or turn == 3 or turn == 4 or turn == 7 or turn == 8:
                selected = player_turn(pool, order, turn)
            if turn == 1 or turn == 2 or turn == 5 or turn == 6 or turn == 9:
                selected = robot_turn(pool, order, turn)
        if order == 1:
            if turn == 1 or turn == 2 or turn == 5 or turn == 6 or turn == 9:
                selected = player_turn(pool, order, turn)
            if turn == 0 or turn == 3 or turn == 4 or turn == 7 or turn == 8:
                selected = robot_turn(pool, order, turn)
        pool.remove(selected)
        turn = turn + 1

    buttonok = tkinter.Button(top,text='ok!', command=okfunction)  # choose to change turn
    buttonok.place(x=500, y=650)

    buttonok = tkinter.Button(top,text='check!', command=check)  # choose to change turn
    buttonok.place(x=600, y=650)

    def player_turn(pool, order, turn):
        global player_money
        if (pool.__contains__(currentchoice)):
            if (player_money >= player_money):
                playerTeam.append(currentchoice)
        player_money -= cost(currentchoice)
        print(player_money)
        return currentchoice

    def click1(x, y):
        global turn
        global order
        global currentchoice
        l = []

        currentchoice = y[x][2]
        lab = tkinter.Label(top, text=currentchoice + '(' + y[x][1] + ')')
        update_label(lab)

    def robot_turn(pool, order, turn):
        global robot_money
        a = rob(pool, order, turn, 0)
        if (pool.__contains__(a)):
            if (robot_money >= robot_money):
                robTeam.append(a)
        robot_money -= cost(currentchoice)
        update_label(tkinter.Label(top, text=a + '(' + a + ')'))
        return a



    button1 = tkinter.Button(top,image=p1, command=lambda: click1(0, T1))
    button1.place(x=250, y=50)
    button2 = tkinter.Button(top,image=p2, command=lambda: click1(1, T1))
    button2.place(x=370, y=50)
    button3 = tkinter.Button(top,image=p3, command=lambda: click1(2, T1))
    button3.place(x=490, y=50)
    button4 = tkinter.Button(top,image=p4, command=lambda: click1(3, T1))
    button4.place(x=610, y=50)
    
    button5 = tkinter.Button(top,image=p5, command=lambda: click1(0, T2))
    button5.place(x=250, y=165)
    button6 = tkinter.Button(top,image=p6, command=lambda: click1(1, T2))
    button6.place(x=370, y=165)
    button7 = tkinter.Button(top,image=p7, command=lambda: click1(2, T2))
    button7.place(x=490, y=165)
    button8 = tkinter.Button(top,image=p8, command=lambda: click1(3, T2))
    button8.place(x=610, y=165)
    
    button9 = tkinter.Button(top,image=p9, command=lambda: click1(0, T3))
    button9.place(x=250, y=280)
    button10 = tkinter.Button(top,image=p10, command=lambda: click1(1, T3))
    button10.place(x=370, y=280)
    button11 = tkinter.Button(top,image=p11, command=lambda: click1(2, T3))
    button11.place(x=490, y=280)
    button12 = tkinter.Button(top,image=p12, command=lambda: click1(3, T3))
    button12.place(x=610, y=280)
    
    button13 = tkinter.Button(top,image=p13, command=lambda: click1(0, T4))
    button13.place(x=250, y=395)
    button14 = tkinter.Button(top,image=p14, command=lambda: click1(1, T4))
    button14.place(x=370, y=395)
    button15 = tkinter.Button(top,image=p15, command=lambda: click1(2, T4))
    button15.place(x=490, y=395)
    button16 = tkinter.Button(top,image=p16, command=lambda: click1(3, T4))
    button16.place(x=610, y=395)
    
    button17 = tkinter.Button(top,image=p17, command=lambda: click1(0, T5))
    button17.place(x=250, y=510)
    button18 = tkinter.Button(top,image=p18, command=lambda: click1(1, T5))
    button18.place(x=370, y=510)
    button19 = tkinter.Button(top,image=p19, command=lambda: click1(2, T5))
    button19.place(x=490, y=510)
    button20 = tkinter.Button(top,image=p20, command=lambda: click1(3, T5))
    button20.place(x=610, y=510)
    
    Label1 = tkinter.Label(top, text=T1[0][2] + '(' + T1[0][1] + ')')
    Label1.place(x=250, y=145)
    Label2 = tkinter.Label(top,text=T1[1][2] + '(' + T1[1][1] + ')')
    Label2.place(x=370, y=145)
    Label3 = tkinter.Label(top,text=T1[2][2] + '(' + T1[2][1] + ')')
    Label3.place(x=490, y=145)
    Label4 = tkinter.Label(top,text=T1[3][2] + '(' + T1[3][1] + ')')
    Label4.place(x=610, y=145)
    
    Label5 = tkinter.Label(top,text=T2[0][2] + '(' + T2[0][1] + ')')
    Label5.place(x=250, y=260)
    Label6 = tkinter.Label(top,text=T2[1][2] + '(' + T2[1][1] + ')')
    Label6.place(x=370, y=260)
    Label7 = tkinter.Label(top,text=T2[2][2] + '(' + T2[2][1] + ')')
    Label7.place(x=490, y=260)
    Label8 = tkinter.Label(top,text=T2[3][2] + '(' + T2[3][1] + ')')
    Label8.place(x=610, y=260)
    
    Label9 = tkinter.Label(top,text=T3[0][2] + '(' + T3[0][1] + ')')
    Label9.place(x=250, y=375)
    Label10 = tkinter.Label(top,text=T3[1][2] + '(' + T3[1][1] + ')')
    Label10.place(x=370, y=375)
    Label11 = tkinter.Label(top,text=T3[2][2] + '(' + T3[2][1] + ')')
    Label11.place(x=490, y=375)
    Label12 = tkinter.Label(top,text=T3[3][2] + '(' + T3[3][1] + ')')
    Label12.place(x=610, y=375)
    
    Label13 = tkinter.Label(top,text=T4[0][2] + '(' + T4[0][1] + ')')
    Label13.place(x=250, y=490)
    Label14 = tkinter.Label(top,text=T4[1][2] + '(' + T4[1][1] + ')')
    Label14.place(x=370, y=490)
    Label15 = tkinter.Label(top,text=T4[2][2] + '(' + T4[2][1] + ')')
    Label15.place(x=490, y=490)
    Label16 = tkinter.Label(top,text=T4[3][2] + '(' + T4[3][1] + ')')
    Label16.place(x=610, y=490)
    
    Label17 = tkinter.Label(top,text=T5[0][2] + '(' + T5[0][1] + ')')
    Label17.place(x=250, y=605)
    Label18 = tkinter.Label(top,text=T5[1][2] + '(' + T5[1][1] + ')')
    Label18.place(x=370, y=605)
    Label19 = tkinter.Label(top,text=T5[2][2] + '(' + T5[2][1] + ')')
    Label19.place(x=490, y=605)
    Label20 = tkinter.Label(top,text=T5[3][2] + '(' + T5[3][1] + ')')
    Label20.place(x=610, y=605)
    
        # button1= tkinter.Button(top,text='Start',fg='red',font=('黑体', 10),)
        # button1.place(x=400,y=240)
    
    img1 = tkinter.Label(top,text='player1', font=('黑体', 15), fg='Goldenrod')
    img1.place(x=40, y=250)
    
    img2 = tkinter.Label(top,text='player2', font=('黑体', 15), fg='Goldenrod')
    img2.place(x=40, y=300)
    
    img3 = tkinter.Label(top,text='player3', font=('黑体', 15), fg='Goldenrod')
    img3.place(x=40, y=350)
    
    img4 = tkinter.Label(top,text='player4', font=('黑体', 15), fg='Goldenrod')
    img4.place(x=40, y=400)
    
    img5 = tkinter.Label(top,text='player5', font=('黑体', 15), fg='Goldenrod')
    img5.place(x=40, y=450)
    
    img6 = tkinter.Label(top,text='player6', font=('黑体', 15), fg='Goldenrod')
    img6.place(x=900, y=250)
    
    img7 = tkinter.Label(top,text='player7', font=('黑体', 15), fg='Goldenrod')
    img7.place(x=900, y=300)
    
    img8 = tkinter.Label(top,text='player8', font=('黑体', 15), fg='Goldenrod')
    img8.place(x=900, y=350)
    
    img9 = tkinter.Label(top,text='player9', font=('黑体', 15), fg='Goldenrod')
    img9.place(x=900, y=400)
    
    img10 = tkinter.Label(top,text='player10', font=('黑体', 15), fg='Goldenrod')
    img10.place(x=900, y=450)
    
    finish_button = tkinter.Button(top, text='exit', command=top.quit)
    finish_button.place(x=890, y=550)

    done_button = tkinter.Button(top, text='done', command=final_page)
    done_button.place(x=700, y=650)


def rule_page():
    top2 = tkinter.Toplevel()
    top2.title('Rule of Game')
    center_window(top2, 500, 350)
    canvas2 = tkinter.Canvas(top2, width=500,
                             height=350)

    canvas2.pack(fill="both", expand=True)
    rule='Hello,Welcome to the rule page of New Fantasy,You can choose\n the mode which you can play with you friends or play against the AI \n.'

    # Display image
    canvas2.create_image(0, 0, image=background, anchor="nw")
    canvas2.create_text(250, 25, text="The Rule of New Fantasy", font=('Pursia',30),fill='Yellow')
    canvas2.create_text(250, 90, text=rule, fill='Yellow')





start_button=tkinter.Button(top3,text='Start',command=start)
start_button.place(x=225,y=250)
rule_button=tkinter.Button(top3,text='rule',command=rule_page)
rule_button.place(x=225,y=300)







top3.mainloop()
