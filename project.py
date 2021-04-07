import itertools
import csv

List_ofPlayerandGroup = [['Karl Malone', 1], ['Jhon Stocketon', 1], ['Jeff Hornacek', 1], ['Wilt Chamberlain', 2],
                         ['Jerry West', 2], ['Gail Goodrich', 2], ['Tim Duncan', 3], ['Tony Parker', 3],
                         ['Manu Ginobili', 3],
                         ['Steph Curry', 4], ['Klay Thompson', 4], ['Kevin Durant', 4], ['LeBron James', 5],
                         ['Dwyane Wade', 5], ['Chris Bosh', 5], ['Machel Jordan', 6], ['Scottie Pippen', 6],
                         ['Dennis Rodman', 6],
                         ["Shaquille O'Neal", 7], ['Kobe Bryant', 7], ['PAUL PIERCE', 8], ['KEVIN GARNETT', 8],
                         ['Ray Allen', 8], ['SHAWN KEMP', 9], ['GARY PAYTON', 9], ['LARRY BIRD', 10],
                         ['KEVIN McHALE ', 10],
                         ['Tracy McGrady', 11], ['Ming Yao', 11], ['Magic Johnson', 12], ['Kareem Abdul-Jabbar', 12],
                         ['James Worthy', 12], ['Steve Nash', 13], ["Amar'e Stoudemire", 13], ['Shawn Marion', 13],
                         ['Carmelon Anthony', 14], ['Allen Iverson', 14], ['Marcus Camby', 14]]

Player_ability = [96, 93, 81, 95, 93, 84, 98, 90, 87, 96, 92, 97, 98, 92, 86, 99, 95, 86, 97, 97, 92, 93, 88, 89, 94,
                  97, 91, 91, 88, 98, 94, 86, 95, 89, 86, 92, 89, 87]

###
# Group_relation=[]
# for i in range(len(List_ofPlayerandGroup)):
#   temp = [];
##     temp.append(List_ofPlayerandGroup[i][1] == List_ofPlayerandGroup[j][1])
# Group_relation.append([temp,List_ofPlayerandGroup[i][0]])


# print(Group_relation)


List_of_Group = [['Group 1', 'Karl Malone', 'Tony Stocketon', 'Jeff Hornacek', "1990-2000"],
                 ['Group 2', 'Wilt Chamberlain', 'Jerry West', 'Elgin Baylor', "1965-1975"],
                 ['Group 3', 'Tim Duncan', 'Tony Parker', 'Manu Ginobili', "2000-2010"],
                 ['Group 4', 'Steph Curry', 'Klay Thompson', 'Kevin Durant', "2010-2020"],
                 ['Group 5', 'LeBron James', 'Dwyane Wade', 'Chris Bosh', "2010-2020"],
                 ['Group 6', 'Machel Jordan', 'Scottie Pippen', 'Dennis Rodman', "1990-2000"],
                 ['Group 7', "Shaquille O'Neal", 'Kobe Bryant', "2000-2010"],
                 ['Group 8', 'PAUL PIERCE', 'KEVIN GARNETT', 'Ray Allen', "2000-2010"],
                 ['Group 9', 'SHAWN KEMP', 'GARY PAYTON', "1990-2000"],
                 ['Group 10', 'LARRY BIRD', 'KEVIN McHALE', "1980-1990"],
                 ['Group 11', 'Tracy McGrady', 'Ming Yao', "2000-2010"],
                 ['Group 12', 'Magic Johnson', 'Kareem Abdul-Jabbar', 'James Worthy', "1980-1990"],
                 ['Group 13', 'Steve Nash', "Amar'e Stoudemire", 'Shawn Marion', "2000-2010"],
                 ['Group 14', 'Carmelon Anthony', 'Allen Iverson', 'Chris Andersen', "2000-2010"]]
GP_relation = []
temp2 = []


# for i in range(len(List_of_Group)):
#   for j in range(len(List_of_Group)):
#      if(List_of_Group[i][-1]==List_of_Group[j][-1]):
#         re=1
#        GP_relation.append([List_of_Group[i][0],List_of_Group[j][0],re])
##      re=0
#     GP_relation.append([List_of_Group[i][0],List_of_Group[j][0],re])
# print(GP_relation)

def get_playername(li):
    player_list = []
    for i in li:
        player_list.append(i[0])
    return player_list


def powerset(xs):
    q = []
    for i in range(1, 4):
        q.extend(itertools.combinations(xs, i))
    return q


# LL=["1","2",'3','4',"5",'6']

# L=['Karl Malone','Tony Stocketon','Jeff Hornacek','Wilt Chamberlain','Jerry West','Elgin Baylor','Tim Duncan']

Final_Li = get_playername(List_ofPlayerandGroup)

kk = powerset(Final_Li)

### Player dictionary
key1 = get_playername(List_ofPlayerandGroup)


def get_details(key, s):
    Player_details = {}
    for i in key:
        for y in s:
            Player_details[i] = y
            Player_ability.remove(y)
            break
    return Player_details


PL = get_details(key1, Player_ability)


# return Player raitng
def rating(str):
    for i in PL:
        if i == str:
            rate = PL[i]
            # print (ra)
    return rate


# return player GRoup
def Get_GPnum(Str):
    for i in List_ofPlayerandGroup:
        if Str == i[0]:
            N = i[1]
    return N


# Calculate MeMo by own predict
def Get_MeMo(set):
    ds = 0
    N1 = N2 = N3 = 0
    Memo = {}
    for i in set:
        if len(i) == 1:
            ds = rating(i[0])
            Memo[i] = ds
        if len(i) == 2:
            N1 = Get_GPnum(i[0])
            N2 = Get_GPnum(i[1])
            if N1 == N2:
                ds = (rating(i[0]) + rating(i[1]) + 3)
                Memo[i] = ds
        if len(i) == 3:
            N1 = Get_GPnum(i[0])
            N2 = Get_GPnum(i[1])
            N3 = Get_GPnum(i[2])
            if N1 == N2 == N3:
                ds = (rating(i[0]) + rating(i[1]) + rating(i[2]) + rating(i[2]) + rating(i[0]) + rating(i[1]) + 5) / 2
                Memo[i] = ds
    return Memo




x = ('Steve Nash', "Amar'e Stoudemire", 'Shawn Marion')
# print(Strength(x))

team_Elo = [['Utah Jazz', 1766], ['Lakers 1971', 1753], ['Spurs', 1764], ['Warriors', 1865], ['Heat', 1774],
            ['Bulls', 1853], ['Lakers 2001', 1779], ['Celtics', 1751], ['Sonics', 1731], ['85-86 Celtics', 1816],
            ['Rocket', 1697], ['Lakers 1987', 1758], ['Suns', 1743], ['Nuggest', 1691]]

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
    for i in team_Elo:
        if i[0] == Str:
            Elo = i[1]
    return Elo


csv_file = csv.reader(open('C:/Users/Zenovarse/Documents/GitHub/project/球员1.csv', 'r', encoding='utf8'))

# print(csv_file)
content = []
for i in csv_file:
    content.append(i)

# average of 144 players
content.remove(['\ufeffNo.', 'Team name', 'Player name', 'rating'])
all_p = 0
for i in content:
    all_p = all_p + int(i[3])
all_p = all_p / len(content)
# print(all_p)

# player rating
def power(Str):
    playerab = 0
    for i in content:
        if i[2] == Str:
            playerab = i[3]
    return playerab


# return the sum strength of the team and team number

team_elo_mean = 0

for i in team_Elo:
    team_elo_mean += i[1]
team_elo_mean/=len(team_Elo)

conversion_factor = team_elo_mean/79.188

def Team_infor(String, Str1, Str2, Str3):
    count = 0
    team_sum = 0
    s1 = s2 = s3 = 0
    k = 0
    t = 0
    f = 3
    for i in content:
        if i[1] == String:
            team_sum = team_sum + int(i[3])
            count += 1
            s1 = int(power(Str1))
            s2 = int(power(Str2))
            if Str3 == 'null':
                s3 = 0
                f = 2
            else:
                s3 = int(power(Str3))
    t = (int(Get_teamElo(String)) / conversion_factor) * count - (team_sum - s1 - s2 - s3)
    k = t - s1 - s2 - s3
    k /= f
    t = k + s1 + s2 + s3
    t = t / f
    return t


# each team k
cal_K_team = [[1, Team_infor('Utah Jazz', 'Karl Malone', 'John Stockton', 'Jeff Hornacek')],
              [2, Team_infor('Lakers 1971', 'Jerry West', 'Wilt Chamberlain', 'Gail Goodrich')],
              [3, Team_infor('Spurs', 'Tim Duncan', 'Tony Parker', 'Manu Ginobili')],
              [4, Team_infor('Warriors', 'Kevin Durant', 'Stephen Curry', 'Klay Thompson')],
              [5, Team_infor('Heat', 'LeBron James', 'Dwyane Wade', 'Chris Bosh')],
              [6, Team_infor('Bulls', 'Michael Jordan', 'Scottie Pippen', 'Dennis Rodman')],
              [7, Team_infor('Lakers 2001', 'Shaquille O’Neal', 'Kobe Bryant', 'null')],
              [8, Team_infor('Celtics', 'Kevin Garnett', 'Paul Pierce', 'Ray Allen')],
              [9, Team_infor('Sonics', 'Gary Payton', 'Shawn Kemp', 'null')],
              [10, Team_infor('85-86 Celtics', 'Larry Bird', 'Kevin McHale', 'null')],
              [11, Team_infor('Rocket', 'Tracy McGrady', 'Yao Ming', 'null')],
              [12, Team_infor('Lakers 1987', 'Magic Johnson', 'Kareem Abdul-Jabbar', 'James Worthy')],
              [13, Team_infor('Suns', 'Steve Nash', 'Amar’e Stoudemire', 'Shawn Marion')],
              [14, Team_infor('Nuggest', 'Carmelo Anthony', 'Allen Iverson', 'Marcus Camby')], ]

#print(cal_K_team)



# memo=Data_memo2(kk)
# print(memo)
# print(kk)


def whole_rating(str):  # from content get information
    rat = 0
    for i in content:
        if i[2] == str:
            rat = i[3]
    return int(rat)


# print(Get_WholeGP('Karl Malone'))


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
    return Memo2


def Get_WholeGP(Str):  # from content get information
    for i in content:
        if Str == i[2]:
            team = i[1]
    return team


#print(Get_WholeGP('Karl Malone'))




def teamset(str):
    se = []
    for i in content:
        if str == i[1]:
            se.append(i[2])
    set = tuple(se)
    return set


#print(teamset('Spurs'))
# print(Strength(('Karl Malone', 'John Stockton', 'Jeff Hornacek')))


# print(Strength(("Amar'e Stoudemire", 'Shawn Marion', 'Carmelon Anthony', 'Allen Iverson', 'Marcus Camby', )))
# print(Strength(("Amar'e Stoudemire", 'Shawn Marion')))
# print(Strength(('Carmelon Anthony', 'Allen Iverson', 'Marcus Camby')))


# print(content)
LLL = []
for i in content:
    LLL.append(i[2])
# print(LLL)

powe_set = powerset(LLL)

memo = Data_memo(powe_set)
#print(memo)

def Strength(set):
    strength = 0;
    if not (set in memo):
        for subset in itertools.combinations(set, len(set) - 1):
            strength += Strength(subset)
        strength /= len(set)
        memo[set] = strength
    return memo[set]



#print((
#whole_rating('Tim Duncan'),
#whole_rating('Tony Parker'),
#whole_rating('Manu Ginobili'),
#whole_rating('Bruce Bowen'),
#whole_rating('Robert Horry'),
#whole_rating('Brent Barry'),
#whole_rating('Nazr Mohammed'),
#whole_rating('Beno Udrih')))


#print(teamset('Nuggest'))
#print(Strength(('Shawn Marion','Carmelon Anthony','Allen Iverson','Marcus Camby')))
#print(Strength(('Carmelo Anthony', 'Allen Iverson', 'Marcus Camby','Tim Duncan','Tony Parker')))


def get_player_num(str):
    num = 0
    for i in content:
        if i[1] == str:
            num += 1
    return num


# print(get_player_num('Utah Jazz'))

def Strength_easy(Str):
    ave_rat = 0
    for i in content:
        if i[1] == Str:
            ave_rat += float(i[3])
    ave_rat = ave_rat / get_player_num(Str)
    return ave_rat





def evaluate_our_method():
    true_values = [];
    calculated_values = [];
    simp_values = []
    krating=[]

    for i in team_Elo:
        true_values.append(i[1] / conversion_factor)
        calculated_values.append(Strength(teamset(i[0])))
        simp_values.append(Strength_easy(i[0]))
        krating.append(Get_webrat(i[0]))

    print(true_values)
    print(calculated_values)
    print(simp_values)

    r = 0;
    r2 = 0
    r3 = 0

    for i in range(len(team_Elo)):
        r += (int(true_values[i]) - int(calculated_values[i])) ** 2
        r2 += (int(true_values[i]) - int(simp_values[i])) ** 2
        r3 += (int(true_values[i])-int(krating[i]))**2
    print(r)
    print(r2)
    print(r3)


evaluate_our_method()