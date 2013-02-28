Sequence Comparision
========================================================================================

About Me:
========

Author:      Jagan Mohan Rao Vujjini
UNCC ID:     800804731
Email:       jvujjini@uncc.edu
========================================================================================

Description:
===========

DNA Comparision is a very important subject in the field of Computational Biology. 
It is used to study the similarility between two things or creatures. This Program is designed 
to compare the similarity of two DNA Sequences which can be done using two methods called 
Normalized Edit Distance and Longest Common Subsequence(LCS).
========================================================================================

Technical Details:
==================

Language: Python
Version : 2.7.3
Compiler : python
========================================================================================

Compilation Procedure:
=====================

1. Goto the home directory of Python in terminal(GNU/Linux) or command prompt(Windows)
(Eg: "C:\Python").

2. Place the file in that folder(else set the classpath).

3.Type the Compiler name followed by name of the file followed by the input file name and 
output file name arguments and press enter.
(Eg: "C:\Python\python SequenceComparision.py example1a.txt example1b.txt output.txt")

4.Now Open the output.txt file to get the output.
========================================================================================

Breakdown of Functions Created:
===============================

1.NED2ROWS():

	NED2ROWS is designed to compute Normalized Edit Distance using a 
    memory of only 2 arrays. It takes s1 and s2 and the input strings and 
    returns a decimal value less than one which is a measure of similarity 
    between the two strings.

2.LCSTABLE():
	
	LCSTABLE is one of the method to compute the longest common subsequence
     of the strings s1 and s2 which are given as an input and returns s3 as an output. 
     This procedure uses an m*n matrix to compute the Dynamic Programming Table which 
     is a very efficient way to compute recursive problems.

3.FMR():
	
	FMR function computes the forward middle row 
   which is given as an input to the LCSRecursive Function.

4.RMR():
	
	RMR Function Computes Reverse Middle Row which 
    is given as an input to the LCSRecursive Function.

5.YSplit():

	YSplit function is used to calculate the 
    vertical split of the DP Table. It takes the values 
    computed by FMR and RMR Functions from the LCSRecursive 
    Function and processes them and provides the input back 
    to it.

6.LCSRecursive():
	
	LCSRecursive method is an alternative and 
    very effective method to calculate the Longest 
    Common Subsequence. It uses only Linear memory 
    even for very long sequences and takes only s1*s2 
    amount of space for computation.
==========================================================================================

Successes/Fails:
================

The Code works efficiently and computes everything as described in the project description and 
also gives exact output as requested. The Challenge I faced was taking "sequence one" on the left 
hand side rather than on top which was the traditional way of doing and to which many people are 
habituated. There were many bugs as a result of this and a lot of effort went into debugging. 
Going back to the description solved most of the problems as it is illustrates every point and 
in the right manner. To be honest, i just followed the instructions in it.Also, Calculating the 
Reverse Middle Row and designing the LCSRecursive Functions were the most enjoyable parts for me 
on this assignment.

However, the LCSRecursive function provides the correct output and in the right way according 
to the project description, capturing it in the right format was not possible. Hence i used a 
list to capture it and then converted it to a string.

===========================================================================================

Data Structure Design:
======================

List is a very powerful Data Structure in Python. It can be used as a stack or a queue,etc,.
Most of the tasks which can be complex in other languages are made easy by lists in python.
Some of them are Splitting the List(a[i:j:k] = a[:j] + a[j:]). Reversing the elements in the 
list(a.reverse()),etc,. Lists and Strings in python share most of the properties and some of 
the methods can be used on both of them.

I used Lists for storing the elements in a 2 Rows array and also to store the elements of the 
Dynamic Programming Table and strings were used to display the output and also to split the 
input strings in each recursion.