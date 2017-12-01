## 2. Introduction to the Data ##

import pandas as pd

all_ages = pd.read_csv("all-ages.csv")
recent_grads = pd.read_csv("recent-grads.csv")

print(all_ages.head())
print(recent_grads.head())

## 3. Summarizing Major Categories ##

# Unique values in Major_category column.
categories  = all_ages['Major_category'].unique()
aa_cat_counts = dict()
rg_cat_counts = dict()

for cat in categories:    
    is_cat1 = (all_ages["Major_category"] == cat)
    is_cat2 = (recent_grads["Major_category"] == cat)
    cat1 = all_ages[is_cat1]
    cat2 = recent_grads[is_cat2]
    
    
    aa_cat_counts[cat] = cat1["Total"].sum()
    rg_cat_counts[cat] = cat2["Total"].sum()
    
    


## 4. Low-Wage Job Rates ##



low_wage = recent_grads["Low_wage_jobs"].sum()
recent_grads_total = recent_grads["Total"].sum()

low_wage_proportion = low_wage / recent_grads_total



## 5. Comparing Data Sets ##

# All majors, common to both DataFrames
majors = recent_grads['Major'].unique()
rg_lower_count = 0

for major in majors:
    bool_aa = (all_ages['Major'] == major)
    bool_rg = (recent_grads['Major'] == major)
    
    maj_aa = all_ages[bool_aa]
    maj_rg = recent_grads[bool_rg]
    
    
    if (maj_rg.iloc[0]["Unemployment_rate"] < maj_aa.iloc[0]["Unemployment_rate"]):
        rg_lower_count +=1
    