import csv
from matplotlib import pyplot as plt
import numpy as np

csv_file = csv.reader(open('per.csv', 'r', encoding='utf8'))

# print(csv_file)
content = []
for i in csv_file:
    content.append(i)
# average of 144 players
content.remove(['\ufeffRk', 'name', 'G', 'MP', 'PER', 'Team'])

player_per=[]
for i in content:
    player_per.append(float(i[4]))

content2=[]
csv_file2 = csv.reader(open('team Elo.csv', 'r', encoding='utf8'))
for i in csv_file2:
    content2.append(i)
content2.remove(['\ufeffTeam', 'Elo'])
#print(content2)
teamElo=[]
for i in content2:
    teamElo.append(int(i[1]))

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


new_e=conversion(teamElo, player_per)
#print((new_e))
d =[79,79,83,85,82,82,82,83,80,82,78,84,80,81,78,83,83]
new_d=conversion(d,player_per)
print(d)
y=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]


y2=[4,119,182]
x4=['team chemistry calculate','average rating','2krating web']

y33=[178,145]
xnew=['team chemistry','average']



x1 = np.array(new_e)
y= np.array(y)
#x2 = np.array(b)
#x3 = np.array(c)
#x4=np.array(x4)
x5 = np.array(d)

plt.plot(y,x1,color='red',label='conversion elo')
#plt.plot(y,x2,color='green',label='calculate result')
#plt.plot(y,x3,color='blue',label='average result')
plt.plot(y,x5,color='purple',label='2k rating result')
#plt.bar(x4,y2,color='blue',label='R square value')
#plt.bar(xnew,y33,color='blue',label='R square value')
plt.legend()
#x=player_per
#print(x)
#y=[0,5,7.5,10,12.5,15,17.5,20,22.5,25,27.5,30,32.5]
#hx=teamElo
#hy=[1650,1700,1750,1800,1850,1900]
#plt.hist(hx,hy)
#plt.xlabel('Player PER')
#plt.ylabel('number of Player')
#plt.title("Player Per information Histogram")
plt.xlabel('Team ELo rating')
plt.ylabel('number of team')
#plt.title("Team Elo information Histogram")
plt.show()