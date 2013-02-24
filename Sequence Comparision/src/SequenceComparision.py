#FileName:    SequenceComparision.py
#Author:      Jagan Mohan Rao Vujjini
#UNCC ID:     800804731
#Email:       jvujjini@uncc.edu

'''This Program is decided to compare the similarity of two DNA Sequences
which can be done using two methods called Normalized Edit Distance and Longest
Common Subsequence(LCS)'''

from __future__ import print_function

#To get Filepaths as input

import sys

string1 = open(sys.argv[1], "r").readline()         # Input Path 1
string2 = open(sys.argv[2], "r").readline()         # Input Path 2

def NED2ROWS(s1,s2):
    
    '''NED2ROWS is designed to compute Normalized Edit Distance using a 
    memory of only 2 arrays. It takes s1 and s2 and the input strings and 
    returns a decimal value less than one which is a measure of similarity 
    between the two strings'''
    
    m = len(s1)+1
    n = len(s2)+1
    
    v = [[0 for row in range(n)] for col in range(2)] # Only two rows used
    
    for j in range(1,n):
        v[0][j] = j
    
    for i in range(1,m):
        for j in range(1,n):
            
            v[1][0] = i
            if s1[i-1] == s2[j-1]:
                v[1][j] = v[0][j-1]                     # If values equal gets the diagonal value
            else:
                v[1][j] = 1 + min(v[1][j-1],v[0][j])    # Else takes minimum of the adjacents and appends one
        
        for z in range(0,n):
            v[0][z] = v[1][z]
    
    x = v[1][n-1]
    
    y = len(s1)+len(s2)
    
    ned = (float)(y-x)/y
    
    return ned

def LCSTABLE(s1,s2):
    
    '''LCSTABLE is one of the method to compute the longest common subsequence
     of the strings s1 and s2 which are given as an input and returns s3 as an output. 
     This procedure uses an m*n matrix to compute the Dynamic Programming Table which 
     is a very efficient way to compute recursive problems'''
    
    m = len(s1)+1
    n = len(s2)+1
    s3 = ""
    
    v = [[0 for row in range(n)] for col in range(m)]       # Computing Full Table
    
    for i in range(1,m):
        v[i][0] = i
    
    for j in range(1,n):
        v[0][j] = j
    
    for i in range(1,m):
        for j in range(1,n):
            if s1[i-1] == s2[j-1]:
                v[i][j] = v[i-1][j-1]                       # If values are equal takes the diagonal value
            else:
                v[i][j] = 1 + min(v[i][j-1],v[i-1][j])      # Else takes minimum of the adjacents and appends one
    
    while(i < m and j < n and i != 0 and j != 0):           # Computing the Dynamic Programming Table
        if s1[i-1] == s2[j-1]:
            s3 = s1[i-1] + s3
            i -= 1
            j -= 1
        elif v[i][j-1] <= v[i-1][j]:
            j -= 1
        else:
            i -= 1
    
    return s3

def FMR(s1,s2):
    
    '''FMR function computes the forward middle row 
   which is given as an input to the LCSRecursive Function'''
   
    m = len(s1)
    n = len(s2)+1
    
    k = (m/2)+1
    
    v = [[0 for row in range(n)] for col in range(2)]   # Only two rows used
    
    for j in range(1,n):
        v[0][j] = j
    
    for i in range(1,k):
        for j in range(1,n):
            
            v[1][0] = i
            if s1[i-1] == s2[j-1]:
                v[1][j] = v[0][j-1]                     # If values are equal gets the diagonal value
            else: 
                v[1][j] = 1 + min(v[1][j-1],v[0][j])    # Else takes the minimum of the adjacents and appends one
        
        for z in range(0,n):
            v[0][z] = v[1][z]
    
    return v[1]

def RMR(s1,s2):
    
    '''RMR Function Computes Reverse Middle Row which 
    is given as an input to the LCSRecursive Function'''
    
    m = len(s1)+1
    n = len(s2)+1
    
    v = [[0 for row in range(n)] for col in range(2)]   # Only Two Rows are taken
    
    for j in range(1,n):
        v[1][j] = j
    v[1].reverse()
    
    k = (len(s1)/2)+1
    
    for i in reversed(range(k,m)):
        
        v[0][len(s2)] = v[1][len(s2)]+1
        
        for j in reversed(range(1,n)):
            
            if s1[i-1] == s2[j-1]:
                v[0][j-1] = v[1][j]                     # If Values are equal, gets the diagonal value
            else: 
                v[0][j-1] = 1 + min(v[0][j],v[1][j-1])  # Else takes the minimum of the other two adjoining and appends one
        
        for z in reversed(range(0,n)):
            v[1][z] = v[0][z]
    
    return v[0]

def YSplit(ftemp,rtemp):
    
    '''YSplit function is used to calculate the 
    vertical split of the DP Table. It takes the values 
    computed by FMR and RMR Functions from the LCSRecursive 
    Function and processes them and provides the input back 
    to it'''
    
    meds = []
    
    meds = map(sum,zip(ftemp,rtemp))                # Calculates sums of FMR and RMR
    
    for i in reversed(meds):
        if i == min(meds):
            yindex = meds.index(i)                  # Index for Vertical Split 
            break
        
    return yindex

def LCSRecursive(s1,s2,ans):
    
    '''LCSRecursive method is an alternative and 
    very effective method to calculate the Longest 
    Common Subsequence. It uses only Linear memory 
    even for very long sequences and takes only s1*s2 
    amount of space for computation.'''
    
    if len(s1) == 1 and s1.strip() != "":
        for i in s2:
            if s1 == i:                             #Prints out the value as it is a part of the LCS
                ans.append(s1)
    
    elif len(s2) == 1 and s2.strip() != "":
        for i in s1:
            if s2 == i:                             #Prints out the value as it is a part of the LCS
                ans.append(s2)
    
    else:
        ftemp = FMR(s1,s2)                          # Forward Middle Row
        rtemp = RMR(s1,s2)                          # Reverse Middle Row
        
        x = len(s1)/2
        y = YSplit(ftemp,rtemp)                     # Index for a Vertical Split
        
        X_front = s1[:x]
        Y_front = s2[:y]
        
        X_back = s1[x:]
        Y_back = s2[y:]
        
        LCSRecursive(X_front,Y_front,ans)           # Recursive Process
        LCSRecursive(X_back,Y_back,ans)


#Printing out the outputs to the output file.

ans = []
LCS = ""
LCSRecursive(string1,string2,ans)
for i in ans:
    LCS += i

log = open(sys.argv[3], "w")
print(NED2ROWS(string1,string2), file=log)
print(LCSTABLE(string1,string2), file=log)
print(LCS, file=log)
log.close()
