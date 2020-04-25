# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 20:07:43 2020

@author: Pratyusha
"""

matr = [[0]*8 for _ in range(8)]
matra = [[1]*8 for _ in range(8)]
matrv = [[0]*8 for _ in range(8)]
seq=[]
seq.append('P')
seq.append('H')
seq.append('P')
seq.append('P')
seq.append('H')
seq.append('P')
seq.append('H')
seq.append('H')
seq.append('P')
seq.append('H')
seq.append('P')
seq.append('P')
seq.append('P')
seq.append('H')
seq.append('H')
seq.append('P')
seq.append('P')
seq.append('H')
seq.append('H')
seq.append('P')
seq.append('H')

seq1=[]
seq1.append(180)
seq1.append(90)
seq1.append(90)
seq1.append(180)
seq1.append(270)
seq1.append(180)
seq1.append(180)
seq1.append(180)
seq1.append(90)
seq1.append(90)
seq1.append(90)
seq1.append(0)
seq1.append(0)
seq1.append(90)
seq1.append(180)
seq1.append(180)
seq1.append(180)
seq1.append(270)
seq1.append(270)
seq1.append(270)
seq1.append(270)

seq11=[]
seq11.append(1)
seq11.append(1)
seq11.append(1)
seq11.append(1)
seq11.append(1)
seq11.append(1)
seq11.append(1)
seq11.append(1)
seq11.append(1)
seq11.append(1)
seq11.append(1)
seq11.append(1)
seq11.append(1)
seq11.append(1)
seq11.append(1)
seq11.append(1)
seq11.append(1)
seq11.append(1)
seq11.append(1)
seq11.append(1)
seq11.append(1)


matr[6][1] = seq[0]
matr[5][1] = seq[1]
matr[4][1] = seq[2]
matr[4][2] = seq[3]
matr[5][2] = seq[4]
matr[5][3] = seq[5]
matr[5][4] = seq[6]
matr[5][5] = seq[7]
matr[4][5] = seq[8]
matr[3][5] = seq[9]
matr[2][5] = seq[10]
matr[2][4] = seq[11]
matr[2][3] = seq[12]
matr[1][3] = seq[13]
matr[1][4] = seq[14]
matr[1][5] = seq[15]
matr[1][6] = seq[16]
matr[2][6] = seq[17]
matr[3][6] = seq[18]
matr[4][6] = seq[19]
matr[5][6] = seq[20]

matra[6][1] = seq1[0]
matra[5][1] = seq1[1]
matra[4][1] = seq1[2]
matra[4][2] = seq1[3]
matra[5][2] = seq1[4]
matra[5][3] = seq1[5]
matra[5][4] = seq1[6]
matra[5][5] = seq1[7]
matra[4][5] = seq1[8]
matra[3][5] = seq1[9]
matra[2][5] = seq1[10]
matra[2][4] = seq1[11]
matra[2][3] = seq1[12]
matra[1][3] = seq1[13]
matra[1][4] = seq1[14]
matra[1][5] = seq1[15]
matra[1][6] = seq1[16]
matra[2][6] = seq1[17]
matra[3][6] = seq1[18]
matra[4][6] = seq1[19]
matra[5][6] = seq1[20]

matrv[6][1] = seq11[0]
matrv[5][1] = seq11[1]
matrv[4][1] = seq11[2]
matrv[4][2] = seq11[3]
matrv[5][2] = seq11[4]
matrv[5][3] = seq11[5]
matrv[5][4] = seq11[6]
matrv[5][5] = seq11[7]
matrv[4][5] = seq11[8]
matrv[3][5] = seq11[9]
matrv[2][5] = seq11[10]
matrv[2][4] = seq11[11]
matrv[2][3] = seq11[12]
matrv[1][3] = seq11[13]
matrv[1][4] = seq11[14]
matrv[1][5] = seq11[15]
matrv[1][6] = seq11[16]
matrv[2][6] = seq11[17]
matrv[3][6] = seq11[18]
matrv[4][6] = seq11[19]
matrv[5][6] = seq11[20]

sco = 0
for i in range(len(matr)):
    for j in range(len(matr[i])):
        if(matr[i][j] == 'H'):
            if(matra[i][j]==0):
                if(matr[i-1][j]=='H' and matra[i-1][j]!=90 and matrv[i-1][j]!=2):
                    sco = sco+1 
                if(matr[i+1][j]=='H' and matra[i+1][j]!=270 and matrv[i+1][j]!=2):
                    sco = sco+1
                if(matr[i][j-1]=='H' and matra[i][j-1]!=0 and matrv[i][j-1]!=2):
                    sco = sco+1
                matrv[i][j] = 2
            elif(matra[i][j]==90):
                if(matr[i-1][j]=='H' and matra[i-1][j]!=90 and matrv[i-1][j]!=2):
                    sco = sco+1 
                if(matr[i][j+1]=='H' and matra[i][j+1]!=180 and matrv[i][j+1]!=2):
                    sco = sco+1
                if(matr[i][j-1]=='H' and matra[i][j-1]!=0 and matrv[i][j-1]!=2):
                    sco = sco+1
                matrv[i][j] = 2
            elif(matra[i][j]==180):
                if(matr[i-1][j]=='H' and matra[i-1][j]!=90 and matrv[i-1][j]!=2):
                    sco = sco+1 
                if(matr[i+1][j]=='H' and matra[i+1][j]!=270 and matrv[i+1][j]!=2):
                    sco = sco+1
                if(matr[i][j+1]=='H' and matra[i][j+1]!=180 and matrv[i][j+1]!=2):
                    sco = sco+1
                matrv[i][j] = 2
            elif(matra[i][j]==270):
                if(matr[i][j+1]=='H' and matra[i][j+1]!=180 and matrv[i][j+1]!=2):
                    sco = sco+1 
                if(matr[i][j-1]=='H' and matra[i][j-1]!=0 and matrv[i][j-1]!=2):
                    sco = sco+1
                if(matr[i+1][j]=='H' and matra[i+1][j]!=270 and matrv[i+1][j]!=2):
                    sco = sco+1
                matrv[i][j] = 2
    print("score=",sco)