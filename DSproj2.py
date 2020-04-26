# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 14:54:17 2020

@authors: Pratyusha, Prerit
"""

import matplotlib.pyplot as plt
import sys
import random
import math

arg = sys.argv
ip=sys.argv[1]
n1 = sys.argv[2]
n2 = sys.argv[3]
p = sys.argv[4]

#ip = input()

n1=int(n1)
n2=int(n2)
p=float(p)
print(n1,n2,p)

ip+='.txt'
file=open(ip,'r')
sequence1=[]
for index, line in enumerate(file.readlines()):
    if (index)%2 == 1:
       sequence1.append(line)

sequence=[]
for i in range(len(sequence1[0])):
    if(sequence1[0][i]=='A' or sequence1[0][i]=='I' or sequence1[0][i]=='L' or sequence1[0][i]=='M' or sequence1[0][i]=='F' or sequence1[0][i]=='P' or sequence1[0][i]=='W' or sequence1[0][i]=='Y' or sequence1[0][i]=='V'):
        sequence.append('H')
    else:
       sequence.append('P')


matsize = len(sequence1[0])
rows,cols = (matsize*2,matsize*2)
matr = [[0]*cols for _ in range(rows)]
#matr_visited = [[0]*cols for _ in range(rows)]
#matr1 = [[0]*cols for _ in range(rows)]

list_letter = ['L','F','R']
text = []
scorearr = []
maxscore=[]
avgscore = []
text1=[]
ind = []

def sequencegenerator(cnt):
    for j in range(cnt):
        t=''
        for i in range(matsize-1):
            t += random.choice(list_letter)
        text.append(t)


def getScore(matr,matr_angle,matr_visited):
    sco = 0
    for i in range(len(matr)):
        for j in range(len(matr[i])):
            if(matr[i][j] == 'H'):
                if(matr_angle[i][j]==0):
                    if(matr[i-1][j]=='H' and matr_angle[i-1][j]!=90 and matr_visited[i-1][j]!=2):
                        sco = sco+1
                    if(matr[i+1][j]=='H' and matr_angle[i+1][j]!=270 and matr_visited[i+1][j]!=2):
                        sco = sco+1
                    if(matr[i][j-1]=='H' and matr_angle[i][j-1]!=0 and matr_visited[i][j-1]!=2):
                        sco = sco+1
                    matr_visited[i][j] = 2
                elif(matr_angle[i][j]==90):
                    if(matr[i-1][j]=='H' and matr_angle[i-1][j]!=90 and matr_visited[i-1][j]!=2):
                        sco = sco+1
                    if(matr[i][j+1]=='H' and matr_angle[i][j+1]!=180 and matr_visited[i][j+1]!=2):
                        sco = sco+1
                    if(matr[i][j-1]=='H' and matr_angle[i][j-1]!=0 and matr_visited[i][j-1]!=2):
                        sco = sco+1
                    matr_visited[i][j] = 2
                elif(matr_angle[i][j]==180):
                    if(matr[i-1][j]=='H' and matr_angle[i-1][j]!=90 and matr_visited[i-1][j]!=2):
                        sco = sco+1
                    if(matr[i+1][j]=='H' and matr_angle[i+1][j]!=270 and matr_visited[i+1][j]!=2):
                        sco = sco+1
                    if(matr[i][j+1]=='H' and matr_angle[i][j+1]!=180 and matr_visited[i][j+1]!=2):
                        sco = sco+1
                    matr_visited[i][j] = 2
                elif(matr_angle[i][j]==270):
                    if(matr[i][j+1]=='H' and matr_angle[i][j+1]!=180 and matr_visited[i][j+1]!=2):
                        sco = sco+1
                    if(matr[i][j-1]=='H' and matr_angle[i][j-1]!=0 and matr_visited[i][j-1]!=2):
                        sco = sco+1
                    if(matr[i+1][j]=='H' and matr_angle[i+1][j]!=270 and matr_visited[i+1][j]!=2):
                        sco = sco+1
                    matr_visited[i][j] = 2
    #print("score=",sco)
    return sco


def getAngle(x):
    if x=='L':
        return -90
    elif x=='R':
        return 90
    elif x=='F':
        return 0

def rmvIllegal(ind,text):
    ind.reverse()
    for i in ind:
        text.pop(i)
    for j in range(len(scorearr)):
        scorearr.pop(0)
    for i in range(len(ind)):
        ind.pop(0)


def legalitycheck(text):
    count = 0
    for i in range(len(text)):
        curr_ang=180
        #print(matr_visited)
        matr_visited = [[0]*cols for _ in range(rows)]
        matr_angle = [[1]*cols for _ in range(rows)]
        matr = [[0]*cols for _ in range(rows)]
        x=matsize
        y=matsize
        matr_visited[x][y]=1
        matr_angle[x][y]=curr_ang
        matr[x][y] = sequence[0]
        #print(x,y)
        #print("------------------------------")
        #print(matr_visited)
        #print("\n")
        for j in range(len(text[i])):
            # Assiginig angles to directions
            curr_ang += getAngle(text[i][j])

            # getting angles between 0 to 360
            if(curr_ang%360==0):
                y=y-1
            elif(curr_ang%360==90):
                x=x-1
            elif(curr_ang%360==180):
                y=y+1
            elif(curr_ang%360==270):
                x=x+1
            curr_ang = curr_ang%360
            # checking if block is visited
            if(matr_visited[x][y]==0):
                matr_visited[x][y]=1
                matr_angle[x][y]=curr_ang
                matr[x][y]=sequence[j+1]
            elif(matr_visited[x][y]==1):
                ind.append(i)
                #print("collision at",i)
                count = count + 1
                break
        #print(matr_angle)
        #print(matr)

        # calculate score
        score = getScore(matr,matr_angle,matr_visited)
        scorearr.append(score)
    return count

# Mutation

def mutation(seq):
    s=[]
    for i in seq:
        if i=='L':
            pick1=[]
            for key, x in prob1.items():
                pick1.extend([key]*int(x*pow(10,c)))
            sub="".join(random.choice(pick1))
        if i=='F':
            pick2=[]
            for key, x in prob2.items():
                pick2.extend([key]*int(x*pow(10,c)))
            sub="".join(random.choice(pick2))
        if i=='R':
            pick3=[]
            for key, x in prob3.items():
                pick3.extend([key]*int(x*pow(10,c)))
            sub="".join(random.choice(pick3))
        s.append(sub)
    str=""
    for i in s:
        str += i
    return str

# crossover and selection
def crossoverAndSelection():
    #print(text)
    text1=[]
    newtext = []
    for i in range(len(text)-1):
        newt = ''
        for j in range(math.floor(len(text[i])/2)):
            newt += text[i][j]
        for k in range(math.floor(len(text[i])/2),len(text[i+1])):
            newt += text[i+1][k]
        newtext.append(newt)
    cnt = legalitycheck(newtext)
    if len(ind)!=0:
        #print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        rmvIllegal(ind,newtext)
    else:
        for i in range(len(scorearr)):
            scorearr.pop(0)

    if len(newtext)>=0.05*n1:
        x=math.ceil(0.05*n1)
        for i in range(x):
            text1.append(newtext[i])
    else:
        x=len(newtext)
        for i in range(x):
            text1.append(newtext[i])
    for i in range(len(text)-x):
        text1.append(text[i])
    #cnt = legalitycheck(text1)
    #scorearr, text1 = (list(t) for t in zip(*sorted(zip(scorearr, text1), reverse=True)))
    #maxscore.append(scorearr[0])
    for i in range(len(text)):
        text.pop(0)

    for i in text1:
        text.append(i)
    #print(text)
    #print("\n")
    for q in range(len(text)):
        l = mutation(text[q])
        text.pop(q)
        text.insert(q,l)
    cnt = legalitycheck(text)
    while(cnt>0):
        ind.reverse()
        for r in ind:
            l1 = mutation(text[r])
            text.pop(r)
            text.insert(r,l1)
        for r in range(len(ind)):
            ind.pop(0)
        for r in range(len(scorearr)):
            scorearr.pop(0)
        cnt=legalitycheck(text)

    maxscore.append(max(scorearr))
    avgscore.append(sum(scorearr)/len(scorearr))
    return text


# initial set of sequences
sequencegenerator(n1)
# adding more sequences to compensate for the removed sequences
cnt = legalitycheck(text)
while(cnt>0):
    #print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    rmvIllegal(ind,text)
    ind = []
    sequencegenerator(cnt)
    cnt = legalitycheck(text)


#Sorting the scorearr in descending order and the text list is sorted parrallely in accordance
scorearr, text = (list(t) for t in zip(*sorted(zip(scorearr, text), reverse=True)))
maxscore.append(scorearr[0])
avgscore.append(sum(scorearr)/len(scorearr))
#print(text)
print("generation 0")
print(scorearr)
#print("\n")
#p = 0.001
p1=p
p2=int(p1)
c=0
while(p2==0):
    p1=p1*10;
    c=c+1
    p2=int(p1)
prob1={'F':p,'R':p}
prob2={'L':p,'R':p}
prob3={'L':p,'F':p}
for l in range(n2):
    text2 = crossoverAndSelection()
    scorearr, text = (list(t) for t in zip(*sorted(zip(scorearr, text), reverse=True)))
    print("generation ",l+1)
    #print(text)
    print(scorearr)
    #print("\n")


print("Max scores are:", maxscore)
print("Avg scores are:", avgscore)


# graphs

#max scores
index1 = []
for i in range(len(maxscore)):
    index1.append(i)

plt.plot(index1, maxscore)

plt.xlabel("Index")
plt.ylabel("Maximum Score")
plt.title("Maximum scores of indices")
plt.show()

#avg scores
index2 = []
for i in range(len(avgscore)):
    index2.append(i)

plt.plot(index2, avgscore)

plt.xlabel("Index")
plt.ylabel("Average Score")
plt.title("Average scores of indices")
plt.show()

#trend for max scores
index3=[]
arr3 = []
for i in range(len(maxscore)-math.floor(len(maxscore)/2)):
    g=0
    for j in range(i,i+math.floor(len(maxscore)/2)):
        g += maxscore[j]
    g=g/math.floor(len(maxscore)/2)
    arr3.append(g)
    index3.append(i)

plt.plot(index3, arr3)

plt.xlabel("Index")
plt.ylabel("Average over half the max scores")
plt.title("Trend")
plt.show()

#trend for avg scores
index4=[]
arr4 = []
for i in range(len(avgscore)-math.floor(len(avgscore)/2)):
    g=0
    for j in range(i,i+math.floor(len(avgscore)/2)):
        g += avgscore[j]
    g=g/math.floor(len(avgscore)/2)
    arr4.append(g)
    index4.append(i)

plt.plot(index4, arr4)

plt.xlabel("Index")
plt.ylabel("Average over half the avg scores")
plt.title("Trend")
plt.show()
    
file.close()
