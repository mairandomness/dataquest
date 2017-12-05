## 2. Introduction to the Data ##


import csv
f = open("nfl_suspensions_data.csv")
g = csv.reader(f)
nfl_suspensions = list(g)
nfl_suspensions = nfl_suspensions[1:]
years = {}
for suspension in nfl_suspensions:
    row_year = suspension[5] 
    if row_year in years:
        years[row_year] += 1
    else:
        years[row_year] = 1
print(years)



## 3. Unique Values ##

import csv
f = open("nfl_suspensions_data.csv")
g = csv.reader(f)
nfl_suspensions = list(g)
nfl_suspensions = nfl_suspensions[1:]
years = {}
unique_teams = []
unique_games = []
for suspension in nfl_suspensions:
    unique_teams.append(suspension[1])
    unique_games.append(suspension[2])
unique_teams = set(unique_teams)
unique_games = set(unique_games)

## 4. Suspension Class ##

class Suspension:
   def  __init__(self, list_susp):
        self.name = list_susp[0]
        self.team = list_susp[1]
        self.games = list_susp[2]
        self.year = list_susp[5]
third_suspension = Suspension(nfl_suspensions[2])
        
    
    

## 5. Tweaking the Suspension Class ##

class Suspension():
    def __init__(self,row):
        self.name = row[0]
        self.team = row[1]
        self.games = row[2]
        try:
            self.year = int(row[5])
        except Exception:
            self.year = 0
    
    def get_year(self):
        return self.year
    
missing_year = Suspension(nfl_suspensions[22])
twenty_third_year = missing_year.get_year()