
import itertools
import csv
List_ofPlayerandGroup=[['Karl Malone',1],['Tony Stocketon',1],['Jeff Hornacek',1],['Wilt Chamberlain',2],['Jerry West',2],['Elgin Baylor',2],['Tim Duncan',3],['Tony Parker',3],['Manu Ginobili',3],
                       ['Steph Curry',4],['Klay Thompson',4],['Kevin Durant',4],['LeBron James',5],['Dwyane Wade',5],['Chris Bosh',5],['Machel Jordan',6],['Scottie Pippen',6],['Dennis Rodman',6],
                       ["Shaquille O'Neal",7],['Kobe Bryant',7],['PAUL PIERCE',8],['KEVIN GARNETT',8],['Ray Allen',8],['SHAWN KEMP',9],['GARY PAYTON',9],['LARRY BIRD',10],['KEVIN McHALE ',10],
                       ['Tracy McGrady',11],['Ming Yao',11],['Magic Johnson',12],['Kareem Abdul-Jabbar',12],['James Worthy',12],['Steve Nash',13],["Amar'e Stoudemire",13],['Shawn Marion',13],
                       ['Carmelon Anthony',14],['Allen Iverson',14],['Chris Andersen',14]]

Player_ability=[96,93,87,95,93,92,97,90,87,96,92,98,94,86,98,95,87,97,97,97,92,93,88,90,94,97,91,92,90,98,95,87,95,89,88,95,93,85]


###
#Group_relation=[]
#for i in range(len(List_ofPlayerandGroup)):
 #   temp = [];
  ##     temp.append(List_ofPlayerandGroup[i][1] == List_ofPlayerandGroup[j][1])
   # Group_relation.append([temp,List_ofPlayerandGroup[i][0]])


#print(Group_relation)


List_of_Group=[['Group 1','Karl Malone','Tony Stocketon','Jeff Hornacek', "1990-2000"],['Group 2','Wilt Chamberlain','Jerry West','Elgin Baylor',"1965-1975"],['Group 3','Tim Duncan','Tony Parker','Manu Ginobili',"2000-2010"],
               ['Group 4','Steph Curry','Klay Thompson','Kevin Durant',"2010-2020"],['Group 5','LeBron James','Dwyane Wade','Chris Bosh',"2010-2020"],['Group 6','Machel Jordan','Scottie Pippen','Dennis Rodman',"1990-2000"],
               ['Group 7',"Shaquille O'Neal",'Kobe Bryant',"2000-2010"],['Group 8','PAUL PIERCE','KEVIN GARNETT','Ray Allen',"2000-2010"],['Group 9','SHAWN KEMP','GARY PAYTON',"1990-2000"],['Group 10','LARRY BIRD','KEVIN McHALE',"1980-1990"],
               ['Group 11','Tracy McGrady','Ming Yao',"2000-2010"],['Group 12','Magic Johnson','Kareem Abdul-Jabbar','James Worthy',"1980-1990"],['Group 13','Steve Nash',"Amar'e Stoudemire",'Shawn Marion',"2000-2010"],
               ['Group 14','Carmelon Anthony','Allen Iverson','Chris Andersen',"2000-2010"]]
GP_relation=[]
temp2 = []
#for i in range(len(List_of_Group)):
 #   for j in range(len(List_of_Group)):
  #      if(List_of_Group[i][-1]==List_of_Group[j][-1]):
   #         re=1
    #        GP_relation.append([List_of_Group[i][0],List_of_Group[j][0],re])
     ##      re=0
       #     GP_relation.append([List_of_Group[i][0],List_of_Group[j][0],re])
#print(GP_relation)

def get_playername(li):
    player_list=[]
    for i in li:
        player_list.append(i[0])
    return player_list

def powerset(xs):
    q=[]
    for i in range(1,6):
        q.extend(itertools.combinations(xs,i))
    return q

LL=["1","2",'3','4',"5",'6']

L=['Karl Malone','Tony Stocketon','Jeff Hornacek','Wilt Chamberlain','Jerry West','Elgin Baylor','Tim Duncan']
Final_Li=get_playername(List_ofPlayerandGroup)
kk=powerset(Final_Li)


### Player dictionary
key1=get_playername(List_ofPlayerandGroup)
def get_details(key,s):
    Player_details={}
    for i in key:
        for y in s:
            Player_details[i] = y
            Player_ability.remove(y)
            break
    return Player_details

PL= get_details(key1,Player_ability)

def rating(str):
    for i in PL:
        if i == str:
            ra=PL[i]
            #print (ra)
    return ra

#return player GRoup
def Get_GPnum(Str):
    for i in List_ofPlayerandGroup:
        if Str == i[0]:
            N=i[1]
    return N

#Calculate
def Get_MeMo(set):
    Memo={}
    for i in set:
        if len(i)== 1:
            ds=rating(i[0])
            Memo[i]=ds
        if len(i)== 2:
            N1=Get_GPnum(i[0])
            N2=Get_GPnum(i[1])
            if N1 == N2:
                ds=rating(i[0])+rating(i[1])+3
                Memo[i]=ds
        if len(i)== 3:
            N1 = Get_GPnum(i[0])
            N2 = Get_GPnum(i[1])
            N3 = Get_GPnum(i[2])
            if N1 == N2 == N3:
                ds=rating(i[0])+rating(i[1])+rating(i[2])+5
                Memo[i]=ds
        else:
            Memo[i]=0;
    return Memo

def Strength(set,memo):
    if not (set in memo):
        strength = 0;
        for subset in itertools.combinations(set, len(set)-1):
            strength += Strength(subset,memo)
        strength / (len(set)-1)
        memo[set] = strength
    return memo[set]

memo=Get_MeMo(kk)
print(Strength(('Steve Nash', "Amar'e Stoudemire", 'Shawn Marion','Steph Curry', 'Klay Thompson'), memo))


#[队伍，elo评分]
team_Elo=[['Utah Jazz',1766],['Lakers 1971',1753],['Spurs', 1764],['Warriors',1865],['Heat',1774],['Bulls',1853],['Lakers 2001',1779],['Celtics', 1751],['Sonics',1731],['85-86 Celtics',1816],['Rocket',1697],['Lakers 1987',1758],['Suns',1743],['Nuggest',1691]]
def Get_teamElo(Str):
    Elo=0
    for i in team_Elo:
        if i[0]== Str:
            Elo=i[1]
    return Elo

csv_file=csv.reader(open('/Users/zbl/Desktop/球员1.csv','r'))
print(csv_file)
content=[]
for i in csv_file:
    content.append(i)
print(content)

#average of 144 players
content.remove(['\ufeffNo.', 'Team name', 'Player name', 'rating'])
all_p=0
for i in content:
    all_p=all_p+int(i[3])
all_p=all_p/len(content)
#print(all_p)

#ratio value for elo
print(1767.6/79.2)

#player rating
def power(Str):
    playerab=0
    for i in content:
        if i[2]==Str:
            playerab=i[3]
    return playerab


#return the sum strength of the team and team number
def Team_infor(String,Str1,Str2,Str3):
    count=0
    team_sum=0
    s1=s2=s3=0
    k=0
    t=0
    f=3
    for i in content:
        if i[1] == String:
            team_sum = team_sum + int(i[3])
            count+=1
            s1=int(power(Str1))
            s2=int(power(Str2))
            if Str3 == 'null':
                s3=0
                f=2
            else:
                s3=int(power(Str3))
    t=(int(Get_teamElo(String)) / 22.3) * count - (team_sum - s1 - s2 - s3)
    t=t/f
    k=t-(s1+s2+s3)/f
    return k


relation_value=(Team_infor('Warriors','Kevin Durant','Stephen Curry','Klay Thompson'))
print(relation_value)

#each team k
cal_K_team=[[1,Team_infor('Utah Jazz','Karl Malone','John Stockton','Jeff Hornacek')],[2,Team_infor('Lakers 1971','Jerry West','Wilt Chamberlain','Gail Goodrich')],[3,Team_infor('Spurs','Tim Duncan','Tony Parker','Manu Ginobili')],[4,Team_infor('Warriors','Kevin Durant','Stephen Curry','Klay Thompson')],[5,Team_infor('Heat','LeBron James','Dwyane Wade','Chris Bosh')],[6,Team_infor('Bulls','Michael Jordan','Scottie Pippen','Dennis Rodman')],[7,Team_infor('Lakers 2001','Shaquille O’Neal','Kobe Bryant','null')],
            [8,Team_infor('Celtics','Kevin Garnett','Paul Pierce','Ray Allen')],[9,Team_infor('Sonics','Gary Payton','Shawn Kemp','null')],[10,Team_infor('85-86 Celtics','Larry Bird','Kevin McHale','null')],[11,Team_infor('Rocket','Tracy McGrady','Yao Ming','null')],[12,Team_infor('Lakers 1987','Magic Johnson','Kareem Abdul-Jabbar','James Worthy')],[13,Team_infor('Suns','Steve Nash','Amar’e Stoudemire','Shawn Marion')],[14,Team_infor('Nuggest','Carmelo Anthony','Allen Iverson','Marcus Camby')],]
#print(cal_K_team)



#calculate the memo by acutal data
def Data_memo(set):
    Memo2 = {}
    for i in set:
        if len(i) == 1:
            Ds = rating(i[0])
            Memo2[i] = Ds
        if len(i) == 2:
            D1 = Get_GPnum(i[0])
            D2 = Get_GPnum(i[1])
            if D1 == D2:
                K=cal_K_team[int(D1)-1][1]
                Ds = (rating(i[0]) + rating(i[1]) + K)
                Memo2[i] = Ds
        if len(i) == 3:
            D1 = Get_GPnum(i[0])
            D2 = Get_GPnum(i[1])
            D3 = Get_GPnum(i[2])
            if D1 == D2 == D3:
                K = cal_K_team[int(D1) - 1][1]
                Ds = (rating(i[0]) + rating(i[1]) + rating(i[2]) + rating(i[2]) + rating(i[0]) + rating(i[1]) + K) / 2
                Memo2[i] = Ds
    return Memo2


print(Data_memo(kk))

