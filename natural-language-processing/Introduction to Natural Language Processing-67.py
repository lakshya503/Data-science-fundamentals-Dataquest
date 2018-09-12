## 3. Tokenizing the Headlines ##

tokenized_headlines = []

for i in submissions["headline"]:
    tokenized_headlines.append(i.split())

## 4. Preprocessing Tokens to Increase Accuracy ##

punctuation = [",", ":", ";", ".", "'", '"', "’", "?", "/", "-", "+", "&", "(", ")"]
clean_tokenized = []
for k in tokenized_headlines:
    new = []
    for i in k: 
        i = i.lower()
        for j in punctuation:
            i = i.replace(j,"")
        new.append(i)
    clean_tokenized.append(new)
    
#print(clean_tokenized)
        

## 5. Assembling a Matrix of Unique Words ##

import numpy as np
unique_tokens = []
single_tokens = []

for i in clean_tokenized:
    for token in i:
        if token not in single_tokens:
            single_tokens.append(token) 
        elif token in single_tokens and token not in unique_tokens:
            unique_tokens.append(token)
        elif token in single_tokens and token in unique_tokens:
            pass

counts = pd.DataFrame(0,index=np.arange(len(clean_tokenized)),columns = unique_tokens)



## 6. Counting Token Occurrences ##

# We've already loaded in clean_tokenized and counts
for index,value in enumerate(clean_tokenized):
    for i in value:
        if i in unique_tokens:
            counts.iloc[index][i]+=1
    

## 7. Removing Columns to Increase Accuracy ##

# We've already loaded in clean_tokenized and counts
word_counts = counts.sum(axis=0) 

word_counts=word_counts[word_counts>=5]
word_counts=word_counts[word_counts<=100]
print(word_counts)
for i in counts.columns:
    if i not in word_counts:
        counts = counts.drop(columns = i,axis=1)
        

## 9. Making Predictions With fit() ##

from sklearn.linear_model import LinearRegression

clf = LinearRegression()
clf.fit(X_train,y_train)
predictions = clf.predict(X_test)

## 10. Calculating Prediction Error ##

from sklearn.metrics import mean_squared_error
mse = mean_squared_error(y_test,predictions)