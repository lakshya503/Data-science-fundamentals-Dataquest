## 1. Introduction ##

import csv
f= open("global_rankings.csv","r")
music = list(csv.reader(f))

## 2. Using the datetime module ##

from datetime import datetime
jan_27_1965= datetime(1965,1,27,12,43)
aug_3_1972 = datetime(1972,8,3,1,43)
oct_31_2000 = datetime(2000,10,31,15,12)
mar_2_2017 = datetime(2017,3,2,7,30)

## 3. Creating a datetime object using a string ##

jun_2_08 = datetime.strptime("6-02-2008","%m-%d-%Y")
jul_15_01 = datetime.strptime("7?15?2001","%m?%d?%Y")
dec_20_08 = datetime.strptime("12--30--2010","%m--%d--%Y")

## 4. Converting the string column into a datetime column ##

def string_to_date(music):
    new_listt=[]
    for i in music[1:]:
        i[-2] = datetime.strptime(i[-2],"%Y-%m-%d")
        new_listt.append(i)
    return new_listt
cleaned_music = string_to_date(music)

## 5. Extracting the month from the date object ##


def get_month(cleaned_music):
    for i in cleaned_music:
        i.append(i[-2].month)
    return cleaned_music     
add_month = get_month(cleaned_music)

## 6. Extracting the day from the date object ##

def get_day(cleaned_music):
    for i in cleaned_music:
        i.append(i[-3].day)
    return cleaned_music
add_day = get_day(cleaned_music)

## 7. Grouping and aggregating our data ##

def organize_by_month(cleaned_music):
    months = [1,2,3,4,5,6,7,8,9,10,11,12]
    
    organized = dict()
    for month in months:
        tracks_in_month = []
        for track in cleaned_music:
            if track[-2] == month:
                tracks_in_month.append(track)
        organized[month] = tracks_in_month
    return organized
organized = organize_by_month(add_day)
def aggregate(organized):
    months = [1,2,3,4,5,6,7,8,9,10,11,12]
    monthly_sum = dict()
    

    for month in months:
        tracks = organized[month]
        # Need the track name, artist and number of streams
        groups = dict()
        for t in tracks:
            track_name = t[2]
            if track_name not in groups.keys():
                groups[track_name] = int(t[3])
            else:
                groups[track_name] += int(t[3])
        monthly_sum[month] = groups
    return monthly_sum
aggregated = aggregate(organized)


## 8. Finding the top artist for each group ##

months = [1,2,3,4,5,6,7,8,9,10,11,12]
top_songs_by_month = []
for i in months:
    sorted_dict = sorted(aggregated[i].items(),key=lambda x: x[1],reverse = True)
    top_songs_by_month.append(sorted_dict[0])
