## 1. Introduction ##

import csv 
f =  open("top100.csv","r")
music = list(csv.reader(f))
print(music)

artists=[]

for i in range(1,101,1):
    artists.append(music[i][1])

## 2. Extract the Artists using a List Comprehension ##

artists_lc = [i[1] for i in music[1:]] 
print(artists_lc)

## 3. Getting the Artist Count using a function ##

def count(alist):
    dic = dict()
    for i in alist:
        if i in dic.keys():
            dic[i]+=1
        else:
            dic[i] = 1
    return dic 
counts = count(artists)
        

## 4. Getting the artist count using Counter() ##

from collections import Counter
artist_counts = Counter(artists)

## 5. Looping through our counts using the items() method ##

artist_counts = []
for key, value in counts.items():
    artist_counts.append([key,value])

## 6. Using a List Comprehension ##

artist_counts = []
for key, value in counts.items():
    artist_counts.append([key,value])
artist_counts_two = [[key,value] for key,value in counts.items()]

## 7. Sorting our list of lists to extract the top value ##

artist_counts.sort()
top_artist = artist_counts[0]

## 8. Specifying a key when sorting our list ##

def by_count(alist):
    return alist[1]
artist_counts.sort(key = by_count, reverse = True)
    

## 9. Creating a function using lambda ##

f = open("top100.csv","r")
music = list(csv.reader(f))
artists = []
for row in music[1:]:
    artists.append(row[1])
from collections import Counter
artist_dict = Counter(artists)
artist_counts = [[key,value] for key,value in artist_dict.items()]
artist_counts.sort(key=lambda x: x[1], reverse=True)