#!/usr/bin/python2.6
mlflist = []
wavlist = []
for line in open('oneWords.list'):
    mlflist.append(line.strip())
for line in open('wav.list'):
    wavlist.append(line.strip())
i=0
j=0
index = wavlist.index(value, )
while i<len(wavlist):
    if mlflist[j].find(wavlist[i].split('.')[0]):
        print(mlflist[j])
        i+=1
        j+=1
    else:
        j+=1
        