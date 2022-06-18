import math
import os
import random
import re
import sys

# Complete the 'acmTeam' function below.
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY topic as parameter
N, m = map(int,input().split())
topic = []
for i in range(N):
    topic.append(int(input(), 2))
maxtopics = -1
nummax = 1
for i in range(N):
    for j in range(i+1,N):
        topics = len([k for k in bin(topic[i] | topic[j]) if k=='1'])
        if(topics > maxtopics):
            nummax = 1
            maxtopics = topics
        elif(topics == maxtopics):
            nummax += 1
print(maxtopics)
print(nummax)