import pandas as pd
from texttable import Texttable

class MortalityContext:
    wentIcuY= 0,
    wentIcuN = 0,
    wentIcuSurvivalY = 0,
    wentIcuSurvivalN = 0

mortalityDic = {}

data = pd.read_csv(r"./metadata.csv")

df = pd.DataFrame(data)

totalFindings = df[df["finding"].str.contains("COVID-19", na = False)]["finding"].count()
totalDeath = df[df["survival"].str.contains("N", na = False)]["survival"].count()

locations = df["location"].dropna()

data = df[df["location"].notnull()]

# filtering distinct countries from the csv 
countries = []

for location in locations:
    locItems = location.split(',')
    countries.append(locItems[-1].strip())

countries = list(set(countries))
countries.sort()

for country in countries:
    
    countryData = data[data["location"].str.contains(country)]

    mortalityContext = MortalityContext()

    #went to icu
    #print(len(countryData))
    wentIcuY = countryData[(countryData["went_icu"].notnull()) &  (countryData["went_icu"] == "Y")]['went_icu'].count()
    wentIcuN = countryData[(countryData["went_icu"].notnull()) &  (countryData["went_icu"] == "N")]['went_icu'].count()

    wentIcuSurvivalY = countryData[(countryData["went_icu"].notnull()) &  (countryData["survival"] == "Y")]['survival'].count()
    wentIcuSurvivalN = countryData[(countryData["went_icu"].notnull()) &  (countryData["survival"] == "N")]['survival'].count()

    mortalityContext.wentIcuY = wentIcuY
    mortalityContext.wentIcuN = wentIcuN

    mortalityContext.wentIcuSurvivalY = wentIcuSurvivalY
    mortalityContext.wentIcuSurvivalN = wentIcuSurvivalN

    mortalityDic[country] = mortalityContext

t = Texttable()

for country in countries:
    
    countryItem = mortalityDic[country]
    t.add_rows([ ['Country', 'WentIcuY', 'WentIcuN', 'WentIcuSurvivalY', 'WentIcuSurvivalN'], [country, countryItem.wentIcuY, countryItem.wentIcuN, countryItem.wentIcuSurvivalY, countryItem.wentIcuSurvivalN] ])
    
    # print(country, ":")
    # print("\t", "WentIcuY:", countryItem.wentIcuY)
    # print("\t", "WentIcuN:", countryItem.wentIcuN)
    # print("\t", "WentIcuSurvivalY:", countryItem.wentIcuSurvivalY)
    # print("\t", "WentIcuSurvivalN:", countryItem.wentIcuSurvivalN)
    # print('\n')



print(t.draw())

