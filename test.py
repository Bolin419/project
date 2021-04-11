import csv
from matplotlib import pyplot as plt
import numpy as np

csv_file = csv.reader(open('球员1.csv', 'r', encoding='utf8'))

# print(csv_file)
content = []
for i in csv_file:
    content.append(i)

# average of 144 players
content.remove(['\ufeffNo.', 'Team name', 'Player name', 'rating'])


x=[]
for i in content:
    x.append(int(i[3]))


team_Elo = [['Utah Jazz', 1766], ['Lakers 1971', 1753], ['Spurs', 1764], ['Warriors', 1865], ['Heat', 1774],
            ['Bulls', 1853], ['Lakers 2001', 1779], ['Celtics', 1751], ['Sonics', 1731], ['85-86 Celtics', 1816],
            ['Rocket', 1697], ['Lakers 1987', 1758], ['Suns', 1743], ['Nuggest', 1691]]
a=[]
for n in team_Elo:
    a.append(int(n[1]))

re1=[79.13358845640839, 78.55106487207469, 79.04396944343398, 83.56972959864193, 79.49206450830606, 83.03201552079544, 79.71611204074209, 78.46144585910028, 77.56525572935612, 81.37406378076876, 76.04173250879107, 78.77511240451074, 78.10296980720263, 75.77287546986783]
b=[79.9794855705105, 78.64261321962194, 79.49741728305243, 83.66636622071326, 79.49206450830606, 84.98713180550506, 80.58139260585823, 78.15371239476877, 77.50234932813035, 81.37406378076876, 75.52786556727698, 78.46251112066463, 78.25819538418011, 76.86217746183797]
c=[75.75, 79.375, 83.125, 82.7, 80.88888888888889, 77.16666666666667, 77.76923076923077, 79.15384615384616, 77.36363636363636, 80.22222222222223, 77.58333333333333, 80.18181818181819, 79.5, 81.375]
y=[1,2,3,4,5,6,7,8,9,10,11,12,13,14]
d =[79, 82, 83, 85, 82, 82, 82, 83, 80, 82, 80, 84, 80, 81]

y2=[4,119,182]
x4=['team chemistry calculate','average rating','2krating web']

y33=[178,145]
xnew=['team chemistry','average']

mu=np.mean(d)
la=np.mean(re1)
d /= (mu/la)

print(a)
x1 = np.array(re1)
y= np.array(y)
x2 = np.array(b)
x3 = np.array(c)
x4=np.array(x4)
x5 = np.array(d)

##plt.plot(y,x1,color='red',label='true value')
#plt.plot(y,x2,color='green',label='calculate result')
#plt.plot(y,x3,color='blue',label='average result')
#plt.plot(y,x5,color='purple',label='2k rating result')
#plt.bar(x4,y2,color='blue',label='R square value')
plt.bar(xnew,y33,color='blue',label='R square value')
plt.legend()

#plt.hist(a,bins=[1650,1700,1750,1800,1850,1900])
#plt.title("Team Elo information Histogram")
plt.show()