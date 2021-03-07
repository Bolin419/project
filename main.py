#!/usr/bin/python
# -*- coding: UTF-8 -*-
#The basic method for checking the player relaitonship between each other
List_ofPlayerandGroup=[['Karl Malone',1],['John Stockton',1],['Jeff Hornacek',1],['Wilt Chamberlain',2],['Jerry West',2],['Elgin Baylor',2],['Tim Duncan',3],['Tony Parker',3],['Manu Ginobili',3],
                       ['Steph Curry',4],['Klay Thompson',4],['Kevin Durant',4],['LeBron James',5],['Dwyane Wade',5],['Chris Bosh',5],['Machel Jordan',6],['Scottie Pippen',6],['Dennis Rodman',6],
                       ["Shaquille O'Neal",7],['Kobe Bryant',7],['PAUL PIERCE',8],['KEVIN GARNETT',8],['Ray Allen',8],['SHAWN KEMP',9],['GARY PAYTON',9],['LARRY BIRD',10],['KEVIN McHALE ',10],
                       ['Tracy McGrady',11],['Ming Yao',11],['Magic Johnson',12],['Kareem Abdul-Jabbar',12],['James Worthy',12],['Steve Nash',13],["Amar'e Stoudemire",13],['Shawn Marion',13],
                       ['Carmelon Anthony',14],['Allen Iverson',14],['Chris Andersen',14]]

Group_relation=[]

for i in range(len(List_ofPlayerandGroup)):
    temp = [];
    for j in range(len(List_ofPlayerandGroup)):
        temp.append(List_ofPlayerandGroup[i][1] != List_ofPlayerandGroup[j][1])
    Group_relation.append(temp)

#print(Group_relation)

List_of_Group=[['Group 1','Karl Malone','Karl Malone','Jeff Hornacek', "1990-2000"],['Group 2','Wilt Chamberlain','Jerry West','Elgin Baylor',"1965-1975"],['Group 3','Tim Duncan','Tony Parker','Manu Ginobili',"2000-2010"],
               ['Group 4','Steph Curry','Klay Thompson','Kevin Durant',"2010-2020"],['Group 5','LeBron James','Dwyane Wade','Chris Bosh',"2010-2020"],['Group 6','Machel Jordan','Scottie Pippen','Dennis Rodman',"1990-2000"],
               ['Group 7',"Shaquille O'Neal",'Kobe Bryant',"2000-2010"],['Group 8','PAUL PIERCE','KEVIN GARNETT','Ray Allen',"2000-2010"],['Group 9','SHAWN KEMP','GARY PAYTON',"1990-2000"],['Group 10','LARRY BIRD','KEVIN McHALE',"1980-1990"],
               ['Group 11','Tracy McGrady','Ming Yao',"2000-2010"],['Group 12','Magic Johnson','Kareem Abdul-Jabbar','James Worthy',"1980-1990"],['Group 13','Steve Nash',"Amar'e Stoudemire",'Shawn Marion',"2000-2010"],
               ['Group 14','Carmelon Anthony','Allen Iverson','Chris Andersen',"2000-2010"]]
GP_relation=[]
temp2 = []
for i in range(len(List_of_Group)):
    for j in range(len(List_of_Group)):
        if(List_of_Group[i][-1]==List_of_Group[j][-1]):
            re=1
            GP_relation.append([List_of_Group[i][0],List_of_Group[j][0],re])
        else:
            re=0
            GP_relation.append([List_of_Group[i][0],List_of_Group[j][0],re])
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

Final_Li=get_playername(List_ofPlayerandGroup)

print powerset(Final_Li)

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

x= get_details(key1,Player_ability)
for key in x:
    if key == 'Karl Malone':
        x[key]+=1
        print (x[key])
print((x))

