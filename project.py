import itertools
import csv
import numpy as np
import tkinter
import PIL
import random
from PIL import Image, ImageTk
import csv


# player per
csv_file = csv.reader(open('per.csv', 'r', encoding='utf8'))

per = []
for i in csv_file:
    per.append(i)

per = per[1:len(per)]

per_new = []
for i in per:
    per_new.append(float(i[4]))
#print(per_new)


csv_file1 = csv.reader(open('team Elo.csv'))
new_teamELo = []
for i in csv_file1:
    new_teamELo.append(i)
new_teamELo.remove(new_teamELo[0])
#print(new_teamELo)

def conversion(data_from, data_to):
    mean1 = np.mean(data_from)
    mean2 = np.mean(data_to)

    std1 = np.std(data_from)
    std2 = np.std(data_to)

    samples = 10000
    a=np.sort(np.random.normal(mean1, std1, samples))
    b=np.sort(np.random.normal(mean2, std2, samples))

    for counter in range(0,len(data_from)):
        dist = float('inf')
        closest_index = 0
        for i in range (0,len(a)):
            if dist > abs(a[i] - data_from[counter]):
                dist = abs(a[i] - data_from[counter])
                closest_index = i
        data_from[counter] = b[closest_index]
    return data_from



def powerset(xs):
    q = []
    for i in range(1, 3):
        q.extend(itertools.combinations(xs, i))
    return q


#the data from 2krating
Overall = [['Utah Jazz', 79], ['Lakers 1971', 82], ['Spurs', 83], ['Warriors', 85], ['Heat', 82],
            ['Bulls', 82], ['Lakers 2001', 82], ['Celtics', 83], ['Sonics', 80], ['85-86 Celtics', 82],
            ['Rocket', 80], ['Lakers 1987', 84], ['Suns', 80], ['Nuggest', 81]]

def Get_webrat(Str): ###rating from 2krating
    Elo = 0
    for i in Overall:
        if i[0] == Str:
            Elo = i[1]
    return Elo

#print(Get_webrat('Utah Jazz'))


def Get_teamElo(Str):
    Elo = 0
    for i in new_teamELo:
        if i[0] == Str:
            Elo = i[1]
    return Elo

#print(Get_teamElo('1997-98 Utah Jazz'))
def power(Str):
    ablitiy=0
    for i in per:
        if Str==i[1]:
            ablitiy=i[4]
    return float(ablitiy)


elos = []
for i in new_teamELo:
    elos.append(int(i[1]))

#print(elos)
#print(per_new)
elo_name=[]
for i in new_teamELo:
    elo_name.append(i[0])
#print(elo_name)
# normalised elo list
normal_elos = conversion(elos, per_new)
#print(normal_elos)
#merge two list
normalised_elo=[list(x) for x in zip(elo_name,normal_elos)]
#print(normalised_elo)

# Get the elo which have already normalised
def Get_normaliseElo(Str):
    ELO=0
    for i in normalised_elo:
        if Str==i[0]:
            ELO=float(i[1])
    return ELO

#print(Get_normaliseElo('1997-98 Utah Jazz'))

def Team_infor(String, Str1, Str2, Str3):
    count = 0
    team_sum = 0
    s1 = s2 = s3 = 0
    k = 0
    t = 0
    f = 3
    for i in per:
        if i[5] == String:
            team_sum = team_sum + float(i[4])
            count += 1
            s1 = (power(Str1))
            s2 = (power(Str2))
            if Str3 == 'null':
                s3 = 0
                f = 2
            else:
                s3 = (power(Str3))

    t = (Get_normaliseElo(String)) * count - (team_sum) + (s1+s2+s3)

    t = t / f
    return t

# each team k
#cal_K_team = [[1, Team_infor('Utah Jazz', 'Karl Malone', 'John Stockton', 'Jeff Hornacek')],
            #  [2, Team_infor('Lakers 1971', 'Jerry West', 'Wilt Chamberlain', 'Gail Goodrich')],
            #  [3, Team_infor('Spurs', 'Tim Duncan', 'Tony Parker', 'Manu Ginobili')],
             # [4, Team_infor('Warriors', 'Kevin Durant', 'Stephen Curry', 'Klay Thompson')],
            #  [5, Team_infor('Heat', 'LeBron James', 'Dwyane Wade', 'Chris Bosh')],
            #  [6, Team_infor('Bulls', 'Michael Jordan', 'Scottie Pippen', 'Dennis Rodman')],
            #  [7, Team_infor('Lakers 2001', 'Shaquille O’Neal', 'Kobe Bryant', 'null')],
            #  [8, Team_infor('Celtics', 'Kevin Garnett', 'Paul Pierce', 'Ray Allen')],
            #  [9, Team_infor('Sonics', 'Gary Payton', 'Shawn Kemp', 'null')],
            #  [10, Team_infor('85-86 Celtics', 'Larry Bird', 'Kevin McHale', 'null')],
            #  [11, Team_infor('Rocket', 'Tracy McGrady', 'Yao Ming', 'null')],
            #  [12, Team_infor('Lakers 1987', 'Magic Johnson', 'Kareem Abdul-Jabbar', 'James Worthy')],
            #  [13, Team_infor('Suns', 'Steve Nash', 'Amar’e Stoudemire', 'Shawn Marion')],
            #  [14, Team_infor('Nuggest', 'Carmelo Anthony', 'Allen Iverson', 'Marcus Camby')], ]

#print(cal_K_team)

#print(Team_infor('2016-17 Golden State Warriors','Klay Thompson\thompkl01','Stephen Curry\curryst01','null'))
def whole_rating(str):  # from content get information
    rat = 0
    for i in per:
        if i[1] == str:
            rat = i[4]
    return (rat)




def Get_WholeGP(Str):  # from content get information
    for i in per:
        if Str == i[1]:
            team = i[5]
    return team



def Data_memo(set):
    Memo2 = {}
    for i in set:
        if len(i) == 1:
            Ds = whole_rating(i[0])
            Memo2[i] = Ds
        if len(i) == 2:
            G1=Get_WholeGP(i[0])
            G2=Get_WholeGP(i[1])
            if G1==G2:
                rate=Team_infor(G1,i[0],i[1],'null')
                Memo2[i]=rate
        if len(i) == 3:
            G1 = Get_WholeGP(i[0])
            G2 = Get_WholeGP(i[1])
            G3 = Get_WholeGP(i[2])
            if G1 == G2 == G3:
                Ds = Team_infor(G1,i[0],i[1],i[2])
                Memo2[i] = Ds
    true_memo = [(k,v) for k,v in Memo2.items()]
    values = []
    for (k,v) in true_memo:
        values.append(float(v))
    #print(values)
    #print(per_new)
    normal_values = conversion(values, per_new)
    #print(normal_values)
    for i in range(0,len(true_memo)):
        true_memo[i] = (true_memo[i][0],normal_values[i])
    for (k,v) in true_memo:
        Memo2[k] = v
    for i in set:
        if len(i) == 1:
            Ds = whole_rating(i[0])
            Memo2[i] = Ds
    #print(Memo2)
    return Memo2


def teamset(str):
    se = []
    for i in per:
        if str == i[5]:
            se.append(i[1])
    set = tuple(se)
    return set

#print(Get_WholeGP('Tony Parker\\parketo01'))
#print(teamset('2004-05 San Antonio Spurs'))
#print(Strength(('Karl Malone', 'John Stockton', 'Jeff Hornacek')))

# print(content)
LLL = []
for i in per:
    LLL.append(i[1])
#print(LLL)


powe_set = powerset(LLL)

memo = Data_memo(powe_set)
#print(memo[('Karl Malone\\malonka01','Jeff Hornacek\hornaje01')])
#print(Team_infor('1997-98 Utah Jazz','Karl Malone\\malonka01','Jeff Hornacek\hornaje01','null'))

def Strength(set):
    strength = 0;
    if not (set in memo):
        for subset in itertools.combinations(set, len(set) - 1):
            strength += float(Strength(subset))
        strength /= len(set)
        memo[set] = strength
    return memo[set]



#print(Strength(('Karl Malone\\malonka01', 'John Stockton\\stockjo01')))

#print(Strength(['Carmelo Anthony', 'Allen Iverson', 'Marcus Camby','Tim Duncan','Tony Parker']))
#(Strength(('Tony Parker\\parketo01','Karl Malone\\malonka01')))

#print(teamset('2007-08 Denver Nuggets'))
#print(Strength(('Shawn Marion','Carmelon Anthony','Allen Iverson','Marcus Camby')))
#print(Strength(('Carmelo Anthony', 'Allen Iverson', 'Marcus Camby','Tim Duncan','Tony Parker')))
#print(Strength(teamset('1997-98 Utah Jazz')))
#print(Strength(teamset('2007-08 Denver Nuggets')))
#print(Strength(teamset('2012-13 Miami Heat')))
#print(Strength(teamset('2010-11 Dallas Mavericks')))

def get_player_num(str):
    num = 0
    for i in per:
        if i[5] == str:
            num += 1
    return num


#print(get_player_num('2007-08 Denver Nuggets'))

def Strength_easy(Str):
    ave_rat = 0
    for i in per:
        if i[5] == Str:
            ave_rat += float(i[4])
    ave_rat = ave_rat / get_player_num(Str)
    return ave_rat

#a=[]
#b=[]
#for i in new_teamELo:
#    a.append(Strength(teamset(i[0])))
#    b.append(Strength_easy(i[0]))
#print(a)
#print(b)


#UI code

import tkinter
import PIL
import random
from PIL import Image, ImageTk
import csv
from tkinter import messagebox

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

center_window(top3, 500, 500)
top3.title('New Fantasy')
bg = Image.open('/Users/zbl/Desktop/nba-logo.png')
bg = bg.resize((500, 500), Image.ANTIALIAS)
background = ImageTk.PhotoImage(bg)
canvas1 = tkinter.Canvas(top3, width=500,
                         height=500)

canvas1.pack(fill="both", expand=True)

# Display image
canvas1.create_image(0, 0, image=background, anchor="nw")

# Add Text
canvas1.create_text(250, 100, font=('Pursia', 30), text="Welcome", fill='Yellow')


# choose mode page
def mode_page():
    top4 = tkinter.Toplevel()
    top4.title('Choosing Mode Page')
    center_window(top4, 500, 350)
    canvas2 = tkinter.Canvas(top4, width=500, height=350)
    canvas2.pack(fill="both", expand=True)
    canvas2.create_image(0, 0, image=background, anchor="nw")
    canvas2.create_text(250, 25, text="The Mode of New Fantasy", font=('Pursia', 30), fill='Yellow')
    lab1 = tkinter.Button(top4, text='Player Against Player', command=Player_Against_Player)
    lab1.place(x=180, y=100)
    lab2 = tkinter.Button(top4, text='Player Against Simple AI', command=Player_against_AI)
    lab2.place(x=180, y=170)


# set for turn and
def decide_turn():
    small = 1
    big = 6
    if random.randint(small, big) <= 3:
        turn = 0
        order = 0  # 0 means player1
        text = 'player 1 choose first'
        print(text)
        return order, turn, text
    else:
        turn = 0
        order = 1  # means player 2
        text = 'player 2 choose first'
        print(text)
        return order, turn, text


csv_file5 = csv.reader(open('球员1.csv', 'r', encoding='utf8'))

# print(csv_file)
content5 = []
for i in csv_file5:
    content5.append(i)
content5.remove(['\ufeffNo.', 'Team name', 'Player name', 'rating'])


def generate_list1():
    UI_list1 = []
    for i in content5:
        if int(i[3]) >= 96:
            UI_list1.append(i)
    return UI_list1


def generate_list2():
    UI_list2 = []
    for i in content5:
        if 92 <= int(i[3]) < 96:
            UI_list2.append(i)
    return UI_list2


def generate_list3():
    UI_list3 = []
    for i in content5:
        if 88 <= int(i[3]) < 92:
            UI_list3.append(i)
    return UI_list3


def generate_list4():
    UI_list4 = []
    for i in content5:
        if 84 <= int(i[3]) < 88:
            UI_list4.append(i)
    return UI_list4


def generate_list5():
    UI_list5 = []
    for i in content5:
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

# 14589 236710 the turn check
roll = decide_turn()
turn = int(roll[1])
# print(turn)
order = int(roll[0])
# print(order)
text = roll[2]
playerTeam = []
player2Team = []
robTeam = []


def final_page():
    top2 = tkinter.Toplevel()
    top2.title('Final Rating Page')
    center_window(top2, 500, 350)
    canvas2 = tkinter.Canvas(top2, width=500, height=350)
    canvas2.pack(fill="both", expand=True)
    canvas2.create_image(0, 0, image=background, anchor="nw")
    canvas2.create_text(250, 25, text="The Final Rating Page", font=('Pursia', 30), fill='Yellow')
    canvas2.create_text(120, 125, text=" Player Team ", font=('Pursia', 20), fill='Yellow')
    canvas2.create_text(400, 125, text=" Robot Team", font=('Pursia', 20), fill='Yellow')
    S1 = Strength(((tuple(robTeam))))
    S2 = Strength(((tuple(playerTeam))))
    canvas2.create_text(120, 160, text="Rating:" + str(S2), font=('Pursia', 20), fill='Yellow')
    canvas2.create_text(400, 160, text="Rating:"+ str(S1), font=('Pursia', 20), fill='Yellow')
    if S1 > S2:
        Lab = tkinter.Label(canvas2, text="Robot Team Win", font=('Pursia', 30), foreground='yellow')
        Lab.place(x=175, y=50)
    else:
        Lab = tkinter.Label(canvas2, text="Player Team Win", font=('Pursia', 30), foreground='yellow')
        Lab.place(x=175, y=50)


def final_page2():
    top7 = tkinter.Toplevel()
    top7.title('Final Rating Page')
    center_window(top7, 500, 350)
    canvas2 = tkinter.Canvas(top7, width=500, height=350)
    canvas2.pack(fill="both", expand=True)
    canvas2.create_image(0, 0, image=background, anchor="nw")
    canvas2.create_text(250, 25, text="The Final Rating Page", font=('Pursia', 30), fill='Yellow')
    canvas2.create_text(120, 125, text=" Team 1  ", font=('Pursia', 20), fill='Yellow')
    canvas2.create_text(400, 125, text=" Team 2  ", font=('Pursia', 20), fill='Yellow')
    S1 = Strength(((tuple(playerTeam))))
    S2 = Strength(((tuple(player2Team))))
    canvas2.create_text(120, 160, text="Rating:"+ str(S1), font=('Pursia', 20), fill='Yellow')
    canvas2.create_text(400, 160, text="Rating:"+str(S2), font=('Pursia', 20), fill='Yellow')
    if S1>S2:
        Lab=tkinter.Label(canvas2,text="Team 1 Win",font=('Pursia', 30), foreground='yellow')
        Lab.place(x=175,y=50)
    else:
        Lab = tkinter.Label(canvas2, text="Team 2 Win", font=('Pursia', 30), foreground='yellow')
        Lab.place(x=175, y=50)



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
player2_money = 19


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
    print('robTeam', robTeam)
    print('playerTeam', playerTeam)


def check2():
    print('player2Team', player2Team)
    print('playerTeam', playerTeam)


def Player_against_AI():
    top = tkinter.Toplevel()
    top.title('Fantasy League Team')
    center_window(top, 1000, 700)

    global turn, text, order
    print(order)
    print(text)
    label2 = tkinter.Label(top, text=text)
    label2.place(x=50, y=30)
    turn_label = tkinter.Label(top, text='turn:' + str(turn))
    turn_label.place(x=50, y=50)

    def player_turn(pool, order, turn):
        global player_money
        has_choosen = True
        if (pool.__contains__(currentchoice)):
            if (player_money >= cost(currentchoice)):
                has_choosen = True
                playerTeam.append(currentchoice)
                player_money -= cost(currentchoice)
                money_label = tkinter.Label(top, text='Player_money:' + str(player_money))
                money_label.place(x=50, y=150)
                print(player_money)
            else:
                has_choosen = False
                messagebox.showerror('error', 'You don not have enough money!')
        else:
            messagebox.showerror('error', 'The player have already be chosen! \n or You have not choose the player!')
        return currentchoice, has_choosen

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

    def okfunction():
        global turn
        chose = True
        selected = ""
        if order == 0:
            if turn == 0 or turn == 3 or turn == 4 or turn == 7 or turn == 8:
                selected1 = player_turn(pool, order, turn)
                selected = selected1[0]
                chose = selected1[1]
            if turn == 1 or turn == 2 or turn == 5 or turn == 6 or turn == 9:
                selected = robot_turn(pool, order, turn)
        if order == 1:
            if turn == 1 or turn == 2 or turn == 5 or turn == 6 or turn == 9:
                selected1 = player_turn(pool, order, turn)
                selected = selected1[0]
                chose = selected1[1]
            if turn == 0 or turn == 3 or turn == 4 or turn == 7 or turn == 8:
                selected = robot_turn(pool, order, turn)

        if chose == True:
            pool.remove(selected)
            turn = turn + 1
        else:
            turn = turn

        turn_label = tkinter.Label(top, text='turn:' + str(turn))
        turn_label.place(x=50, y=50)

    buttonok = tkinter.Button(top, text='ok!', command=okfunction)  # choose to change turn
    buttonok.place(x=475, y=670)

    buttonok = tkinter.Button(top, text='check!', command=check)  # choose to change turn
    buttonok.place(x=75, y=575)

    money_label = tkinter.Label(top, text='money:' + str(player_money))
    money_label.place(x=50, y=150)

    # T1 Player
    button1 = tkinter.Button(top, image=p1, command=lambda: click1(0, T1))
    button1.place(x=250, y=25)
    button2 = tkinter.Button(top, image=p2, command=lambda: click1(1, T1))
    button2.place(x=370, y=25)
    button3 = tkinter.Button(top, image=p3, command=lambda: click1(2, T1))
    button3.place(x=490, y=25)
    button4 = tkinter.Button(top, image=p4, command=lambda: click1(3, T1))
    button4.place(x=610, y=25)

    # T2 Player
    button5 = tkinter.Button(top, image=p5, command=lambda: click1(0, T2))
    button5.place(x=250, y=155)
    button6 = tkinter.Button(top, image=p6, command=lambda: click1(1, T2))
    button6.place(x=370, y=155)
    button7 = tkinter.Button(top, image=p7, command=lambda: click1(2, T2))
    button7.place(x=490, y=155)
    button8 = tkinter.Button(top, image=p8, command=lambda: click1(3, T2))
    button8.place(x=610, y=155)

    # T3 Player
    button9 = tkinter.Button(top, image=p9, command=lambda: click1(0, T3))
    button9.place(x=250, y=285)
    button10 = tkinter.Button(top, image=p10, command=lambda: click1(1, T3))
    button10.place(x=370, y=285)
    button11 = tkinter.Button(top, image=p11, command=lambda: click1(2, T3))
    button11.place(x=490, y=285)
    button12 = tkinter.Button(top, image=p12, command=lambda: click1(3, T3))
    button12.place(x=610, y=285)

    # T4 Player
    button13 = tkinter.Button(top, image=p13, command=lambda: click1(0, T4))
    button13.place(x=250, y=415)
    button14 = tkinter.Button(top, image=p14, command=lambda: click1(1, T4))
    button14.place(x=370, y=415)
    button15 = tkinter.Button(top, image=p15, command=lambda: click1(2, T4))
    button15.place(x=490, y=415)
    button16 = tkinter.Button(top, image=p16, command=lambda: click1(3, T4))
    button16.place(x=610, y=415)

    # T5 Player
    button17 = tkinter.Button(top, image=p17, command=lambda: click1(0, T5))
    button17.place(x=250, y=545)
    button18 = tkinter.Button(top, image=p18, command=lambda: click1(1, T5))
    button18.place(x=370, y=545)
    button19 = tkinter.Button(top, image=p19, command=lambda: click1(2, T5))
    button19.place(x=490, y=545)
    button20 = tkinter.Button(top, image=p20, command=lambda: click1(3, T5))
    button20.place(x=610, y=545)



    Label1 = tkinter.Label(top, text=T1[0][2] + '\n(' + T1[0][1] + ')')
    Label1.place(x=270, y=118)
    Label2 = tkinter.Label(top, text=T1[1][2] + '\n(' + T1[1][1] + ')')
    Label2.place(x=390, y=118)
    Label3 = tkinter.Label(top, text=T1[2][2] + '\n(' + T1[2][1] + ')')
    Label3.place(x=510, y=118)
    Label4 = tkinter.Label(top, text=T1[3][2] + '\n(' + T1[3][1] + ')')
    Label4.place(x=630, y=118)
    LabelT1 = tkinter.Label(top, text="T1 Player(Cost Money:5)!", font=('Pursia', 13))
    LabelT1.place(x=750, y=68)

    Label5 = tkinter.Label(top, text=T2[0][2] + '\n(' + T2[0][1] + ')')
    Label5.place(x=270, y=248)
    Label6 = tkinter.Label(top, text=T2[1][2] + '\n(' + T2[1][1] + ')')
    Label6.place(x=390, y=248)
    Label7 = tkinter.Label(top, text=T2[2][2] + '\n(' + T2[2][1] + ')')
    Label7.place(x=510, y=248)
    Label8 = tkinter.Label(top, text=T2[3][2] + '\n(' + T2[3][1] + ')')
    Label8.place(x=630, y=248)
    LabelT2 = tkinter.Label(top, text="T2 Player(Cost Money:4)!", font=('Pursia', 13))
    LabelT2.place(x=750, y=198)

    Label9 = tkinter.Label(top, text=T3[0][2] + '\n(' + T3[0][1] + ')')
    Label9.place(x=270, y=378)
    Label10 = tkinter.Label(top, text=T3[1][2] + '\n(' + T3[1][1] + ')')
    Label10.place(x=390, y=378)
    Label11 = tkinter.Label(top, text=T3[2][2] + '\n(' + T3[2][1] + ')')
    Label11.place(x=510, y=378)
    Label12 = tkinter.Label(top, text=T3[3][2] + '\n(' + T3[3][1] + ')')
    Label12.place(x=630, y=378)
    LabelT3 = tkinter.Label(top, text="T3 Player(Cost Money:3)!", font=('Pursia', 13))
    LabelT3.place(x=750, y=328)

    Label13 = tkinter.Label(top, text=T4[0][2] + '\n(' + T4[0][1] + ')')
    Label13.place(x=270, y=508)
    Label14 = tkinter.Label(top, text=T4[1][2] + '\n(' + T4[1][1] + ')')
    Label14.place(x=390, y=508)
    Label15 = tkinter.Label(top, text=T4[2][2] + '\n(' + T4[2][1] + ')')
    Label15.place(x=510, y=508)
    Label16 = tkinter.Label(top, text=T4[3][2] + '\n(' + T4[3][1] + ')')
    Label16.place(x=630, y=508)
    LabelT4 = tkinter.Label(top, text="T4 Player(Cost Money:2)!", font=('Pursia', 13))
    LabelT4.place(x=750, y=446)

    Label17 = tkinter.Label(top, text=T5[0][2] + '\n(' + T5[0][1] + ')')
    Label17.place(x=270, y=638)
    Label18 = tkinter.Label(top, text=T5[1][2] + '\n(' + T5[1][1] + ')')
    Label18.place(x=390, y=638)
    Label19 = tkinter.Label(top, text=T5[2][2] + '\n(' + T5[2][1] + ')')
    Label19.place(x=510, y=638)
    Label20 = tkinter.Label(top, text=T5[3][2] + '\n(' + T5[3][1] + ')')
    Label20.place(x=630, y=638)
    LabelT5 = tkinter.Label(top, text="T5 Player(Cost Money:1)!", font=('Pursia', 13))
    LabelT5.place(x=750, y=588)

    LabelTeam = tkinter.Label(top, text="Player 1 Team", font=('黑体', 20))
    LabelTeam.place(x=40, y=215)
    LabelTeam2 = tkinter.Label(top, text="Player2 ROB Team", font=('黑体', 20))
    LabelTeam2.place(x=860, y=215)

    img1 = tkinter.Label(top, text='player1', font=('黑体', 15), fg='Goldenrod')
    img1.place(x=40, y=250)

    img2 = tkinter.Label(top, text='player2', font=('黑体', 15), fg='Goldenrod')
    img2.place(x=40, y=300)

    img3 = tkinter.Label(top, text='player3', font=('黑体', 15), fg='Goldenrod')
    img3.place(x=40, y=350)

    img4 = tkinter.Label(top, text='player4', font=('黑体', 15), fg='Goldenrod')
    img4.place(x=40, y=400)

    img5 = tkinter.Label(top, text='player5', font=('黑体', 15), fg='Goldenrod')
    img5.place(x=40, y=450)

    img6 = tkinter.Label(top, text='player6', font=('黑体', 15), fg='Goldenrod')
    img6.place(x=900, y=250)

    img7 = tkinter.Label(top, text='player7', font=('黑体', 15), fg='Goldenrod')
    img7.place(x=900, y=300)

    img8 = tkinter.Label(top, text='player8', font=('黑体', 15), fg='Goldenrod')
    img8.place(x=900, y=350)

    img9 = tkinter.Label(top, text='player9', font=('黑体', 15), fg='Goldenrod')
    img9.place(x=900, y=400)

    img10 = tkinter.Label(top, text='player10', font=('黑体', 15), fg='Goldenrod')
    img10.place(x=900, y=450)

    finish_button = tkinter.Button(top, text='exit', command=top.quit)
    finish_button.place(x=75, y=600)

    done_button = tkinter.Button(top, text='done', command=final_page)
    done_button.place(x=75, y=550)


# Player Against Player
def Player_Against_Player():
    top = tkinter.Toplevel()
    top.title('Fantasy League Team')
    center_window(top, 1000, 700)

    global turn, text, order
    print(order)
    print(text)
    label2 = tkinter.Label(top, text=text)
    label2.place(x=50, y=30)
    turn_label = tkinter.Label(top, text='turn:' + str(turn))
    turn_label.place(x=50, y=50)

    def player_turn(pool, order, turn):
        global player_money
        has_choosen = True
        if (pool.__contains__(currentchoice)):
            if (player_money >= cost(currentchoice)):
                has_choosen = True
                playerTeam.append(currentchoice)
                player_money -= cost(currentchoice)
                money_label = tkinter.Label(top, text='Player_1 money:' + str(player_money))
                money_label.place(x=50, y=150)
                print(player_money)
            else:
                has_choosen = False
                messagebox.showerror('error', 'You don not have enough money!')
        else:
            messagebox.showerror('error', 'The player have already be chosen!')
        return currentchoice, has_choosen

    def playertwo_turn(pool, order, turn):
        global player2_money
        has_choosen = True
        if (pool.__contains__(currentchoice)):
            if (player2_money >= cost(currentchoice)):
                has_choosen = True
                player2Team.append(currentchoice)
                player2_money -= cost(currentchoice)
                money_label = tkinter.Label(top, text='Player_2 money:' + str(player2_money))
                money_label.place(x=850, y=150)
                print(player2_money)
            else:
                has_choosen = False
                messagebox.showerror('error', 'You don not have enough money!')
        else:
            messagebox.showerror('error', 'The player have already be chosen!')
        return currentchoice, has_choosen



    def click1(x, y):
        global turn
        global order
        global currentchoice
        currentchoice = y[x][2]
        lab = tkinter.Label(top, text=currentchoice + '(' + y[x][1] + ')')
        update_label(lab)


    def okfunction():
        global turn
        chose = True
        selected = ""
        if order == 0:
            if turn == 0 or turn == 3 or turn == 4 or turn == 7 or turn == 8:
                selected1 = player_turn(pool, order, turn)
                selected = selected1[0]
                chose = selected1[1]
            if turn == 1 or turn == 2 or turn == 5 or turn == 6 or turn == 9:
                selected1 = playertwo_turn(pool, order, turn)
                selected = selected1[0]
                chose = selected1[1]
        if order == 1:
            if turn == 1 or turn == 2 or turn == 5 or turn == 6 or turn == 9:
                selected1 = player_turn(pool, order, turn)
                selected = selected1[0]
                chose = selected1[1]
            if turn == 0 or turn == 3 or turn == 4 or turn == 7 or turn == 8:
                selected1 = playertwo_turn(pool, order, turn)
                selected = selected1[0]
                chose = selected1[1]

        if chose == True:
            pool.remove(selected)
            turn = turn + 1
        else:
            turn = turn

        turn_label = tkinter.Label(top, text='turn:' + str(turn))
        turn_label.place(x=50, y=50)



    money_label = tkinter.Label(top, text='Player_1 money:' + str(player_money))
    money_label.place(x=50, y=150)
    money_label = tkinter.Label(top, text='Player_2 money:' + str(player2_money))
    money_label.place(x=850, y=150)

    #T1 Player
    button1 = tkinter.Button(top, image=p1, command=lambda: click1(0, T1))
    button1.place(x=250, y=25)
    button2 = tkinter.Button(top, image=p2, command=lambda: click1(1, T1))
    button2.place(x=370, y=25)
    button3 = tkinter.Button(top, image=p3, command=lambda: click1(2, T1))
    button3.place(x=490, y=25)
    button4 = tkinter.Button(top, image=p4, command=lambda: click1(3, T1))
    button4.place(x=610, y=25)

    #T2 Player
    button5 = tkinter.Button(top, image=p5, command=lambda: click1(0, T2))
    button5.place(x=250, y=155)
    button6 = tkinter.Button(top, image=p6, command=lambda: click1(1, T2))
    button6.place(x=370, y=155)
    button7 = tkinter.Button(top, image=p7, command=lambda: click1(2, T2))
    button7.place(x=490, y=155)
    button8 = tkinter.Button(top, image=p8, command=lambda: click1(3, T2))
    button8.place(x=610, y=155)

    #T3 Player
    button9 = tkinter.Button(top, image=p9, command=lambda: click1(0, T3))
    button9.place(x=250, y=285)
    button10 = tkinter.Button(top, image=p10, command=lambda: click1(1, T3))
    button10.place(x=370, y=285)
    button11 = tkinter.Button(top, image=p11, command=lambda: click1(2, T3))
    button11.place(x=490, y=285)
    button12 = tkinter.Button(top, image=p12, command=lambda: click1(3, T3))
    button12.place(x=610, y=285)

    #T4 Player
    button13 = tkinter.Button(top, image=p13, command=lambda: click1(0, T4))
    button13.place(x=250, y=415)
    button14 = tkinter.Button(top, image=p14, command=lambda: click1(1, T4))
    button14.place(x=370, y=415)
    button15 = tkinter.Button(top, image=p15, command=lambda: click1(2, T4))
    button15.place(x=490, y=415)
    button16 = tkinter.Button(top, image=p16, command=lambda: click1(3, T4))
    button16.place(x=610, y=415)

    #T5 Player
    button17 = tkinter.Button(top, image=p17, command=lambda: click1(0, T5))
    button17.place(x=250, y=545)
    button18 = tkinter.Button(top, image=p18, command=lambda: click1(1, T5))
    button18.place(x=370, y=545)
    button19 = tkinter.Button(top, image=p19, command=lambda: click1(2, T5))
    button19.place(x=490, y=545)
    button20 = tkinter.Button(top, image=p20, command=lambda: click1(3, T5))
    button20.place(x=610, y=545)

    Label1 = tkinter.Label(top, text=T1[0][2] +  '\n(' + T1[0][1] + ')')
    Label1.place(x=270, y=118)
    Label2 = tkinter.Label(top, text=T1[1][2] + '\n(' + T1[1][1] + ')')
    Label2.place(x=390, y=118)
    Label3 = tkinter.Label(top, text=T1[2][2] + '\n(' + T1[2][1] + ')')
    Label3.place(x=510, y=118)
    Label4 = tkinter.Label(top, text=T1[3][2] + '\n(' + T1[3][1] + ')')
    Label4.place(x=630, y=118)
    LabelT1 = tkinter.Label(top,text="T1 Player(Cost Money:5)!",font=('Pursia', 13))
    LabelT1.place(x=750,y=68)

    Label5 = tkinter.Label(top, text=T2[0][2] + '\n(' + T2[0][1] + ')')
    Label5.place(x=270, y=248)
    Label6 = tkinter.Label(top, text=T2[1][2] + '\n(' + T2[1][1] + ')')
    Label6.place(x=390, y=248)
    Label7 = tkinter.Label(top, text=T2[2][2] + '\n(' + T2[2][1] + ')')
    Label7.place(x=510, y=248)
    Label8 = tkinter.Label(top, text=T2[3][2] + '\n(' + T2[3][1] + ')')
    Label8.place(x=630, y=248)
    LabelT2 = tkinter.Label(top, text="T2 Player(Cost Money:4)!", font=('Pursia', 13))
    LabelT2.place(x=750, y=198)


    Label9 = tkinter.Label(top, text=T3[0][2] + '\n(' + T3[0][1] + ')')
    Label9.place(x=270, y=378)
    Label10 = tkinter.Label(top, text=T3[1][2] + '\n(' + T3[1][1] + ')')
    Label10.place(x=390, y=378)
    Label11 = tkinter.Label(top, text=T3[2][2] + '\n(' + T3[2][1] + ')')
    Label11.place(x=510, y=378)
    Label12 = tkinter.Label(top, text=T3[3][2] + '\n(' + T3[3][1] + ')')
    Label12.place(x=630, y=378)
    LabelT3 = tkinter.Label(top, text="T3 Player(Cost Money:3)!", font=('Pursia', 13))
    LabelT3.place(x=750, y=328)

    Label13 = tkinter.Label(top, text=T4[0][2] + '\n(' + T4[0][1] + ')')
    Label13.place(x=270, y=508)
    Label14 = tkinter.Label(top, text=T4[1][2] + '\n(' + T4[1][1] + ')')
    Label14.place(x=390, y=508)
    Label15 = tkinter.Label(top, text=T4[2][2] + '\n(' + T4[2][1] + ')')
    Label15.place(x=510, y=508)
    Label16 = tkinter.Label(top, text=T4[3][2] + '\n(' + T4[3][1] + ')')
    Label16.place(x=630, y=508)
    LabelT4 = tkinter.Label(top, text="T4 Player(Cost Money:2)!", font=('Pursia', 13))
    LabelT4.place(x=750, y=446)

    Label17 = tkinter.Label(top, text=T5[0][2] + '\n(' + T5[0][1] + ')')
    Label17.place(x=270, y=638)
    Label18 = tkinter.Label(top, text=T5[1][2] + '\n(' + T5[1][1] + ')')
    Label18.place(x=390, y=638)
    Label19 = tkinter.Label(top, text=T5[2][2] + '\n(' + T5[2][1] + ')')
    Label19.place(x=510, y=638)
    Label20 = tkinter.Label(top, text=T5[3][2] + '\n(' + T5[3][1] + ')')
    Label20.place(x=630, y=638)
    LabelT5 = tkinter.Label(top, text="T5 Player(Cost Money:1)!", font=('Pursia', 13))
    LabelT5.place(x=750, y=588)

    # button1= tkinter.Button(top,text='Start',fg='red',font=('黑体', 10),)
    # button1.place(x=400,y=240)
    LabelTeam = tkinter.Label(top, text="Player 1 Team",font=('黑体', 20))
    LabelTeam.place(x=40, y=215)
    LabelTeam2 = tkinter.Label(top, text="Player 2 Team", font=('黑体', 20))
    LabelTeam2.place(x=860, y=215)


    img1 = tkinter.Label(top, text='player1', font=('黑体', 15), fg='Goldenrod')
    img1.place(x=40, y=250)

    img2 = tkinter.Label(top, text='player2', font=('黑体', 15), fg='Goldenrod')
    img2.place(x=40, y=300)

    img3 = tkinter.Label(top, text='player3', font=('黑体', 15), fg='Goldenrod')
    img3.place(x=40, y=350)

    img4 = tkinter.Label(top, text='player4', font=('黑体', 15), fg='Goldenrod')
    img4.place(x=40, y=400)

    img5 = tkinter.Label(top, text='player5', font=('黑体', 15), fg='Goldenrod')
    img5.place(x=40, y=450)

    img6 = tkinter.Label(top, text='player6', font=('黑体', 15), fg='Goldenrod')
    img6.place(x=900, y=250)

    img7 = tkinter.Label(top, text='player7', font=('黑体', 15), fg='Goldenrod')
    img7.place(x=900, y=300)

    img8 = tkinter.Label(top, text='player8', font=('黑体', 15), fg='Goldenrod')
    img8.place(x=900, y=350)

    img9 = tkinter.Label(top, text='player9', font=('黑体', 15), fg='Goldenrod')
    img9.place(x=900, y=400)

    img10 = tkinter.Label(top, text='player10', font=('黑体', 15), fg='Goldenrod')
    img10.place(x=900, y=450)

    finish_button = tkinter.Button(top, text='exit', command=top.quit)
    finish_button.place(x=75, y=600)

    done_button = tkinter.Button(top, text='done', command=final_page2)
    done_button.place(x=75, y=550)

    buttonok = tkinter.Button(top, text='ok!', command=okfunction)  # choose to change turn
    buttonok.place(x=475, y=670)

    buttonok = tkinter.Button(top, text='check!', command=check2)  # choose to change turn
    buttonok.place(x=75, y=575)


def rule_page():
    top2 = tkinter.Toplevel()
    top2.title('Rule of Game')
    center_window(top2, 500, 350)
    canvas2 = tkinter.Canvas(top2, width=500,
                             height=350)

    canvas2.pack(fill="both", expand=True)
    rule = 'Hello,Welcome to the rule page of New Fantasy,You can choose\n the mode which you can ' \
           'play with you friends or play against the AI \n.'

    # Display image
    canvas2.create_image(0, 0, image=background, anchor="nw")
    canvas2.create_text(250, 25, text="The Rule of New Fantasy", font=('Pursia', 30), fill='Yellow')
    canvas2.create_text(250, 90, text=rule, fill='Yellow')


start_button = tkinter.Button(top3, text='Start', command=mode_page)
start_button.place(x=225, y=250)
rule_button = tkinter.Button(top3, text='rule', command=rule_page)
rule_button.place(x=225, y=300)

top3.mainloop()
