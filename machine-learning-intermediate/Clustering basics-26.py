## 2. The dataset ##

import pandas as pd
votes = pd.read_csv("114_congress.csv")
print(votes.head(5))
                   

## 3. Exploring the data ##

import numpy as np
print(votes["party"].value_counts())
print(np.mean(votes))

## 4. Distance between Senators ##

from sklearn.metrics.pairwise import euclidean_distances

print(euclidean_distances(votes.iloc[0,3:].values.reshape(1, -1), votes.iloc[1,3:].values.reshape(1, -1)))

distance = euclidean_distances(votes.iloc[0,3:],votes.iloc[2,3:])
print(distance)

## 6. Initial clustering ##

import pandas as pd
from sklearn.cluster import KMeans

kmeans_model = KMeans(n_clusters=2, random_state=1)
senator_distances = kmeans_model.fit_transform(votes.iloc[:,3:])
print(senator_distances)

## 7. Exploring the clusters ##

labels = kmeans_model.labels_
print(labels)
print(pd.crosstab(labels, votes["party"]))

## 8. Exploring Senators in the wrong cluster ##

democratic_outliers = votes[(votes["party"] == "D") & (labels== 1)]
print(democratic_outliers)

## 9. Plotting out the clusters ##

import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.scatter(x=senator_distances[:,0], y = senator_distances[:,1] , c = labels, linewidths=0)
plt.show()

## 10. Finding the most extreme ##

import numpy as np
extremism = senator_distances**3
extremism = extremism.sum(axis=1)
votes["extremism"] = extremism

votes.sort_values(by='extremism' ,inplace = True, ascending = False) 
print(votes.head(10))

