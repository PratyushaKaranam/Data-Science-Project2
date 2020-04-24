# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 14:54:17 2020

@author: Pratyusha
"""

import sys
import random
#import math
arg = sys.argv
#ip=sys.argv[1]


ip = input()

ip+='.txt'
file=open(ip,'r')
sequence1=[]
for index, line in enumerate(file.readlines()):
    if (index)%2 == 1:
       sequence1.append(line) 

tt = ''
sequence=[]
for i in range(len(sequence1[0])):
    if(sequence1[0][i]=='A' or sequence1[0][i]=='I' or sequence1[0][i]=='L' or sequence1[0][i]=='M' or sequence1[0][i]=='F' or sequence1[0][i]=='P' or sequence1[0][i]=='W' or sequence1[0][i]=='Y' or sequence1[0][i]=='V'):
        tt += 'H'
    else:
        tt += 'P'
sequence.append(tt)

matsize = len(sequence1[0])
rows,cols = (matsize*2,matsize*2)
matr = [[0]*cols for _ in range(rows)]
#matr_visited = [[0]*cols for _ in range(rows)]
#matr1 = [[0]*cols for _ in range(rows)]

list_letter = ['L','F','R']
text = []

def sequencegenerator(cnt):
    for j in range(cnt):
        t=''
        for i in range(matsize):
            t += random.choice(list_letter)
        text.append(t) 
sequencegenerator(100)
#x=matsize
#y=matsize
#print(x,y)
#matr_visited[x][y]=1
curr_ang = 180
def legalitycheck(text):
    ind = []
    count = 0
    for i in range(len(text)):
        curr_ang=180
        #print(matr_visited)
        matr_visited = [[0]*cols for _ in range(rows)]
        x=matsize
        y=matsize
        matr_visited[x][y]=1
        #print(x,y)
        #print("------------------------------")
        #print(matr_visited)
        #print("\n")
        for j in range(len(text[i])):
            # Assiginig angles to directions            
            if(text[i][j]=='L'):
                curr_ang -=90
            elif(text[i][j]=='R'):
                curr_ang +=90
            elif(text[i][j]=='F'):
                curr_ang +=0
        
            # getting angles between 0 to 360 
            if(curr_ang%360==0):
                y=y-1
            elif(curr_ang%360==90):
                x=x-1
            elif(curr_ang%360==180):
                y=y+1
            elif(curr_ang%360==270):
                x=x+1
        
            # checking if block is visited
            if(matr_visited[x][y]==0):
                matr_visited[x][y]=1
            elif(matr_visited[x][y]==1):
                ind.append(i)
                count = count + 1
                break
    ind.reverse()
    # removing illegal sequences
    for i in ind:
        #print(i)
        text.pop(i)
    return count

# adding more sequences to compensate for the removed sequences
cnt = legalitycheck(text)
while(cnt>0):
    sequencegenerator(cnt)
    cnt = legalitycheck(text)