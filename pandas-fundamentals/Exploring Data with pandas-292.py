## 2. Using iloc to select by integer position ##

import pandas as pd
import numpy as np

f500 = pd.read_csv("f500.csv", index_col=0)
f500.index.name = None
f500.loc[f500["previous_rank"] == 0, "previous_rank"] = np.nan
fifth_row = f500.iloc[4]
first_three_rows = f500.iloc[0:3] 
first_seventh_row_slice = f500.iloc[[0,6],0:5]

## 3. Reading CSV files with pandas ##

f500 = pd.read_csv("f500.csv")
f500.loc[f500["previous_rank"]==0,"previous_rank"] = np.nan

## 4. Working with Integer Labels ##

sorted_emp = f500.sort_values("employees", ascending=False)
top5_emp = sorted_emp.iloc[0:5]

## 5. Using pandas methods to create boolean masks ##

previously_ranked = f500[f500["previous_rank"].notnull()]
rank_change = previously_ranked["rank"] - previously_ranked["previous_rank"]

## 6. Boolean Operators ##

# Example code:
# answer_0 = 1
answer_1 = 3
answer_2 = 2
answer_3 = 3

## 7. Using Boolean Operators ##

big_rev_neg_profit = f500[(f500["revenues"] > 100000) & (f500["profits"] < 0)]
tech_outside_usa = f500[(f500["country"] != "USA") & (f500["sector"] == "Technology")].head()

## 8. Pandas Index Alignment ##

previously_ranked = f500[f500["previous_rank"].notnull()]
rank_change = previously_ranked["previous_rank"] - previously_ranked["rank"]
f500["rank_change"] = rank_change

## 9. Using Loops with pandas ##

top_employer_by_country = {}
countries = f500["country"].unique()
for c in countries: 
    selected_rows = f500[f500["country"] == c]
    sorted_rows = selected_rows.sort_values("employees",ascending = False)
    sorted_rows = sorted_rows.iloc[0]
  
    top_employer_by_country[c] = sorted_rows["company"]

## 10. Challenge: Calculating Return on Assets by Country ##

top_roa_by_sector = {}
sector_names = f500["sector"].unique()
for s in sector_names:
    sorted_sector = f500[f500["sector"] == s]
    sorted_sector["roa"] = sorted_sector["profits"]/sorted_sector["assets"]
    new_sorted_sector = sorted_sector.sort_values("roa", ascending = False)
    name = new_sorted_sector.iloc[0]
    top_company = name["company"]
    top_roa_by_sector[s] = top_company
    
f500["roa"] = f500["profits"]/f500["assets"]