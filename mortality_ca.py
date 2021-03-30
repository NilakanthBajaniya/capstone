from numpy import positive
import pandas as pd

data = pd.read_csv(r"./COVID19-eng.csv")

print()
df = pd.DataFrame(data)

totalPositive = len(data)
totalDeath = df[df["Death"] == 1]["Death"].count()
print("Overall Mortality Rate: ", round((totalDeath / totalPositive) * 100, 2), "\n")

totalInIcu = df[df["Hospital status"] == 1]["Hospital status"].count()
totalInIcuDeath = df[(df["Hospital status"] == 1) & (df["Death"] == 1)]["Hospital status"].count()
print("Went in ICU Mortality: ", (totalInIcuDeath / totalInIcu) * 100, "\n" )

malePositive = df[df["Gender"] == 1]["Gender"].count()
maleDeath = df[(df["Gender"] == 1) & (df["Death"] == 1)]["Gender"].count()
print("Male Mortality: ", (maleDeath / malePositive) * 100)

femalePositive = df[df["Gender"] == 2]["Gender"].count()
femaleDeath = df[(df["Gender"] == 2) & (df["Death"] == 1)]["Gender"].count()
print("Female Mortality", (femaleDeath / femalePositive) * 100)
print()

ageGroups = {}

ageGroups[1] = "0 to 19 Years"
ageGroups[2] = "20 to 29 Years"
ageGroups[3] = "30 to 39 Years"
ageGroups[4] = "40 to 49 Years"

ageGroups[5] = "50 to 59 Years"
ageGroups[6] = "60 to 69 Years"
ageGroups[7] = "70 to 79 Years"
ageGroups[8] = "80 to 89 Years"

for ageGroup in ageGroups:

    positiveCount = df[(df["Age group"] == ageGroup)]["Age group"].count()
    deathCount = df[(df["Age group"] == ageGroup) & (df["Death"] == 1)]["Age group"].count()

    print(ageGroups[ageGroup], "Mortality", (deathCount / positiveCount) * 100)

    if(ageGroup == 4): 
        print()


