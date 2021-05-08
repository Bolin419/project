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

y33=[502.3292008371377,531.2867166837774]
xnew=['team chemistry','average']

b=[13.341740330165228, 12.396297665659592, 14.197889149878442, 27.539857408149167, 15.42671404319414, 25.124411558285384, 14.85620919921549, 12.828105839473984, 9.22988287038697, 18.006871004149627, 5.4719739074744504, 12.223431528900685, 11.468236982400741, 5.094856169943804, 7.19625346221563, 12.94976718062297, 8.92235257836244]
c=[13.735714285714284, 13.053846153846154, 13.576470588235294, 14.594117647058821, 12.838888888888889, 12.966666666666667, 13.973333333333331, 13.426666666666666, 14.076923076923077, 14.191666666666665, 12.866666666666667, 14.491666666666665, 12.5, 11.33529411764706, 13.012500000000001, 13.061111111111112, 14.031249999999998]

r = 0;
r2 = 0
r3 = 0

for i in range(len(teamElo)):
    r += (float(b[i]) - float(new_d[i]))**2
    r2 += (int(c[i]) - float(new_d[i]))** 2
print(r)
print(r2)




N=2
X=np.arange(N)
X=('team chemistry calculate','average rating')

x1 = np.array(new_e)
y= np.array(y)
x2 = np.array(b)
x3 = np.array(c)
x4=np.array(x4)
xnew = np.array(r2)

plt.plot(y,x1,color='red',label='conversion elo')
plt.plot(y,x2,color='green',label='calculate result')
plt.plot(y,x3,color='blue',label='average result')
plt.plot(y,x5,color='purple',label='2k rating result')
#plt.bar(X,y33,color='blue',label='data difference')
#plt.bar(xnew,y33,color='blue',label='data difference')
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
##plt.xlabel('Team')
#plt.ylabel('Team elo rating')
#plt.xlabel('data')
#plt.ylabel('value of difference')
#plt.title("Team Elo information Histogram")
plt.show()