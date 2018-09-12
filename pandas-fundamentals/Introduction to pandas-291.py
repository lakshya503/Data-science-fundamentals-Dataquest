## 1. Understanding pandas and NumPy ##

import pandas as pd
f500 = pd.read_csv("f500.csv", index_col=0)
f500.index.name = None

f500_type = type(f500)
f500_shape = f500.shape

## 2. Introducing DataFrames ##

f500_head = f500.head(6)
f500_tail = f500.tail(8)
f500.info()

## 3. Selecting Columns From a DataFrame by Label ##

industries = f500.loc[:,"industry"]
previous = f500.loc[:,["rank","previous_rank","years_on_global_500_list"]]
financial_data = f500.loc[:,"revenues":"profit_change"]

## 4. Column selection shortcuts ##

countries = f500.loc[:,"country"]
revenues_years = f500.loc[:,["revenues","years_on_global_500_list"]]
ceo_to_sector = f500.loc[:,"ceo":"sector"]

## 5. Selecting Items from a Series by Label ##

ceos = f500["ceo"]
walmart = ceos["Walmart"]
apple_to_samsung = ceos["Apple":"Samsung Electronics"]
oil_companies = ceos[["Exxon Mobil","BP", "Chevron"]]

                        

## 6. Selecting Rows From a DataFrame by Label ##

drink_companies = f500.loc[["Anheuser-Busch InBev", "Coca-Cola","Heineken Holding"]]
big_movers = f500.loc[["Aviva", "HP", "JD.com", "BHP Billiton"],["rank","previous_rank"]]
middle_companies = f500.loc["Tata Motors" : "Nationwide","rank" : "country"]

## 7. Series and Dataframe Describe Methods ##

profits_desc = f500["profits"].describe() 
revenue_and_employees_desc=f500[["revenues","employees"]].describe()
all_desc = f500.describe()

## 8. More Data Exploration Methods ##

top5_countries = f500["country"].value_counts().head()
top5_previous_rank = f500["previous_rank"].value_counts().head()
max_f500 = f500.max(numeric_only=True)

## 9. Assignment with pandas ##

f500["revenues_b"] = f500["revenues"]/1000
f500.loc["Dow Chemical","ceo"] = "Jim Fitterling"

## 10. Using Boolean Indexing with pandas Objects ##

kr_bool = f500["country"] == "South Korea"
f500 = f500[kr_bool]
top_5_kr = f500.head(5)

## 11. Using Boolean Arrays to Assign Values ##

import numpy as np
prev_rank_before = f500["previous_rank"].value_counts(dropna=False).head()
f500.loc[f500["previous_rank"] == 0,"previous_rank"] = np.nan
prev_rank_after = f500["previous_rank"].value_counts(dropna=False).head()

## 12. Challenge: Top Performers by Country ##

top_3_countries = f500["country"].value_counts().head(3)
cities_usa = f500.loc[f500["country"]=="USA","hq_location"].value_counts().head()
sector_china = f500.loc[f500["country"]=="China","sector"].value_counts().head()
mean_employees_japan = f500.loc[f500["country"]=="Japan","employees"].mean()
