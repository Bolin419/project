import itertools
import csv
import numpy as np


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

print(Get_teamElo('1997-98 Utah Jazz'))
def power(Str):
    ablitiy=0
    for i in per:
        if Str==i[1]:
            ablitiy=i[4]
    return float(ablitiy)


elos = []
for i in new_teamELo:
    elos.append(int(i[1]))

print(elos)
#print(per_new)
elo_name=[]
for i in new_teamELo:
    elo_name.append(i[0])
print(elo_name)
# normalised elo list
normal_elos = conversion(elos, per_new)
print(normal_elos)
#merge two list
normalised_elo=[list(x) for x in zip(elo_name,normal_elos)]
print(normalised_elo)

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

    t = (Get_normaliseElo(String)) * count - (team_sum)

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
#print(Team_infor('1997-98 Utah Jazz', 'Karl Malone\\malonka01', 'Jeff Hornacek\\hornaje01', 'John Stockton\\stockjo01'))

print(Team_infor('2016-17 Golden State Warriors','Klay Thompson\thompkl01','Stephen Curry\curryst01','null'))
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
    print(values)
    print(per_new)
    normal_values = conversion(values, per_new)
    print(normal_values)
    for i in range(0,len(true_memo)):
        true_memo[i] = (true_memo[i][0],normal_values[i])
    for (k,v) in true_memo:
        Memo2[k] = v
    for i in set:
        if len(i) == 1:
            Ds = whole_rating(i[0])
            Memo2[i] = Ds
    print(Memo2)
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
# print(Strength(('Karl Malone', 'John Stockton', 'Jeff Hornacek')))

# print(Strength(("Amar'e Stoudemire", 'Shawn Marion', 'Carmelon Anthony', 'Allen Iverson', 'Marcus Camby', )))
# print(Strength(("Amar'e Stoudemire", 'Shawn Marion')))
# print(Strength(('Carmelon Anthony', 'Allen Iverson', 'Marcus Camby')))


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



#print(Strength(('Tony Parker\\parketo01','Karl Malone\\malonka01','Chris Andersen\\anderch01')))
print(Strength(('Tony Parker\\parketo01','Bruce Bowen\\bowenbr01','Tim Duncan\\duncati01','Manu Ginóbili\\ginobma01','Karl Malone\\malonka01')))
#print((
#whole_rating('Tim Duncan'),
#whole_rating('Tony Parker'),
#whole_rating('Manu Ginobili'),
#whole_rating('Bruce Bowen'),
#whole_rating('Robert Horry'),
#whole_rating('Brent Barry'),
#whole_rating('Nazr Mohammed'),
#whole_rating('Beno Udrih')))


print(teamset('2007-08 Denver Nuggets'))
#print(Strength(('Shawn Marion','Carmelon Anthony','Allen Iverson','Marcus Camby')))
#print(Strength(('Carmelo Anthony', 'Allen Iverson', 'Marcus Camby','Tim Duncan','Tony Parker')))

print(Strength(teamset('2007-08 Denver Nuggets')))
print(Strength(teamset('2012-13 Miami Heat')))
def get_player_num(str):
    num = 0
    for i in per:
        if i[1] == str:
            num += 1
    return num


# print(get_player_num('Utah Jazz'))

def Strength_easy(Str):
    ave_rat = 0
    for i in per:
        if i[1] == Str:
            ave_rat += float(i[3])
    ave_rat = ave_rat / get_player_num(Str)
    return ave_rat




