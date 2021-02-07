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

print(Group_relation)

