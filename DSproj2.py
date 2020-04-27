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

n1=int(n1)
n2=int(n2)
p=float(p)

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

list_letter = ['L','F','R']
text = []
scorearr = []
maxscore=[]
avgscore = []
text1=[]
ind = []

# Functions

# SEQUENCE GENERATOR
def sequencegenerator(cnt):
    for j in range(cnt):
        t=''
        for i in range(matsize-1):
            t += random.choice(list_letter)
        text.append(t)


# SCORE GENERATOR
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
    return sco


# ANGLES FOR DIRECTIONS
def getAngle(x):
    if x=='L':
        return -90
    elif x=='R':
        return 90
    elif x=='F':
        return 0
    

# ILLEGAL SEQUENCE REMOVER
def rmvIllegal(ind,text):
    ind.reverse()
    for i in ind:
        text.pop(i)
    for j in range(len(scorearr)):
        scorearr.pop(0)
    for i in range(len(ind)):
        ind.pop(0)


# TO CHECK FOR LEGAL SEQUENCES
def legalitycheck(text):
    count = 0
    for i in range(len(text)):
        curr_ang=180
        matr_visited = [[0]*cols for _ in range(rows)]
        matr_angle = [[1]*cols for _ in range(rows)]
        matr = [[0]*cols for _ in range(rows)]
        x=matsize
        y=matsize
        matr_visited[x][y]=1
        matr_angle[x][y]=curr_ang
        matr[x][y] = sequence[0]
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
                count = count + 1
                break

        # calculate score
        score = getScore(matr,matr_angle,matr_visited)
        scorearr.append(score)
    return count


# MUTATION 
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


# CROSSOVER AND SELECTION
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
    for i in range(len(text)):
        text.pop(0)
    for i in text1:
        text.append(i)

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
    rmvIllegal(ind,text)
    ind = []
    sequencegenerator(cnt)
    cnt = legalitycheck(text)


#SORTING THE INITIAL SET OF SEQUENCES
scorearr, text = (list(t) for t in zip(*sorted(zip(scorearr, text), reverse=True)))
print("Generation 0:")
print(scorearr)

maxscore.append(scorearr[0])
avgscore.append(sum(scorearr)/len(scorearr))

p1=p
p2=int(p1)
c=0
while(p2==0):
    p1=p1*10
    c=c+1
    p2=int(p1)
prob1={'F':p,'R':p}
prob2={'L':p,'R':p}
prob3={'L':p,'F':p}

#SORTING ALL MUTATED SEQUENCES
for l in range(n2):
    text2 = crossoverAndSelection()
    scorearr, text = (list(t) for t in zip(*sorted(zip(scorearr, text), reverse=True)))
    print("Generation ",l+1,":")
    print(scorearr)

print("\nMax Scores:")
print(maxscore)
print("Avg Scores:")
print(avgscore)
    

# GRAPHS

# MAX SCORES
index1 = []
for i in range(len(maxscore)):
    index1.append(i)

plt.plot(index1, maxscore)

plt.xlabel("Generations")
plt.ylabel("Maximum Score")
plt.title("Maximum scores for generations")
plt.show()

# AVG SCORES
index2 = []
for i in range(len(avgscore)):
    index2.append(i)

plt.plot(index2, avgscore)

plt.xlabel("Generations")
plt.ylabel("Average Score")
plt.title("Average scores for generations")
plt.show()

# MAX SCORES TREND
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

plt.xlabel("Sets of generations")
plt.ylabel("Average of max scores")
plt.title("Trend for Max Scores")
plt.show()

# AVG SCORES TREND
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

plt.xlabel("Sets of generations")
plt.ylabel("Average of average scores")
plt.title("Trend for average scores")
plt.show()
    
file.close()
