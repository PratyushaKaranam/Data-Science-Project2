# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 14:54:17 2020

@author: Pratyusha
"""

import sys
import random
import math
arg = sys.argv
#ip=sys.argv[1]


ip = input()

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
    
    if len(newtext)>=5:
        x=5
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
    return text


# initial set of sequences        
sequencegenerator(10)
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
#print(text)  
print("generation 0")
print(scorearr)
#print("\n")
p = 0.001   
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
for l in range(30):
    text2 = crossoverAndSelection()
    scorearr, text = (list(t) for t in zip(*sorted(zip(scorearr, text), reverse=True)))
    print("generation ",l+1)
    #print(text)
    print(scorearr)
    #print("\n")
    

print("max scores:", maxscore)
file.close()
