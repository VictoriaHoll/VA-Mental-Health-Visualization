# This is the main file that does the stuff
import pandas as pd
import numpy as np

mental_health = pd.read_csv('VA-OHE-NVHER-FY13-Diagnoses-Mental-Illness.csv')  # import file as a dataframe

# print(mental_health.columns) # determine the header columns. I am interested in the "mental health" categorization and would like to break this down by gender, race, service connection, encounters (e.g., outpatient visits, primary care visits, etc.), health conditions. column names are: ['


mental_health["Mental Illness"] = mental_health["Mental Illness"].str.replace(".", " ")
mental_health["Mental Illness"] = mental_health["Mental Illness"].str.replace("Other Mental Health", "Other")

mental_health["Value"] = mental_health["Value"].dropna()

# print(mental_health["Value"].isnull().sum())

mental_health = mental_health.fillna("X") # filled all blank columns with "X" to avoid condcatenating NaN object 

# print(mental_health.shape)

mental_health["ID"] = mental_health["Long_title"] + mental_health["Short_title"] + mental_health["Group"] + mental_health["Group1"] + mental_health["Subgroup"] # this column will act as an identifier when I want to join other tables for future analysis. Long_title + Short_title + Group + Group1 + Subgroup 

# with pd.option_context('display.max_colwidth', -1):
# 	print(mental_health["ID"]) # this was used to print entire length of the column so I can double check the ID contanied all columns

mental_unique = mental_health["Mental Illness"].value_counts() # how many unique mental illness groups are there? - there are five groups: PTSD, Other, Mood/Anxiety, Serious Mental Illness, Substance Abuse, No Mental Health

print(mental_unique)

# next step is to understand how each of these break down by gender, age, race, geography, encounters. after that, I'd like to understand if any health conditions correlate with certain mental illnesses.

mental_grouplist = ["PTSD", "Other", "Mood.Anxiety", "Serious Mental Illness", "Substance Abuse", "No Mental Health"]
bool_ptsd  = (mental_health["Mental Illness"] == "PTSD") & (mental_health["Subgroup"] == "Overall")
ptsd_overall = mental_health[bool_ptsd]
print(ptsd_overall)
other_overall = mental_health[(mental_health["Mental Illness"] == "Other") & (mental_health["Subgroup"] == "Overall")]
mood_overall = mental_health[(mental_health["Mental Illness"] == "Mood Anxiety") & (mental_health["Subgroup"] == "Overall")]
serious_overall = mental_health[(mental_health["Mental Illness"] == "Serious Mental Illness") & (mental_health["Subgroup"] == "Overall")]
substance_overall = mental_health[(mental_health["Mental Illness"] == "Substance Abuse") & (mental_health["Subgroup"] == "Overall")]
none_overall = mental_health[(mental_health["Mental Illness"] == "No Mental Health") & (mental_health["Subgroup"] == "Overall")]

# mental_health["Value"] = mental_health["Value"].astype(float)

final_columns = ["ID", "Subgroup", "Mental Illness", "Value"]

mental_health = mental_health.loc[:, final_columns]

# print(mental_health.shape)
# print(mental_health.columns)

gender = ["F", "M"]
race = ["AI/AN", "Asian", "Black/African American", "NH/OPI", "White", "Hispanic", "Multi-race", "Unknown"]

import numpy as np
import matplotlib.pyplot as plt

# data to plot
n_groups = 6
ptsd_overall_value = ptsd_overall["Value"].astype(float)
print(ptsd_overall_value)
print(other_overall)
other_overall_value = float(other_overall["Value"])

mood_overall_value = float(mood_overall["Value"])
serious_overall_value = float(serious_overall["Value"])
substance_overall_value = float(substance_overall["Value"])
none_overall_value = float(none_overall["Value"])
overall_value = (ptsd_overall_value, other_overall_value, mood_overall_value, serious_overall_value, substance_overall_value, none_overall_value)

# create plot
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.35
opacity = 0.8

i  = 0
rects1 = plt.bar(index + bar_width*i, overall_value, bar_width,
alpha=opacity,
color='b',
label='Overall')
i += 1


# rects2 = plt.bar(index + bar_width*i, mood_overall_value, bar_width,
# alpha=opacity,
# color='g',
# label='Mood/Anxiety')
# i += 1

# rects3 = plt.bar(index + bar_width*i, serious_overall_value, bar_width,
# alpha=opacity,
# color='g',
# label='Serious Mental Illness')
# i += 1

# rects4 = plt.bar(index + bar_width*i, substance_overall_value, bar_width,
# alpha=opacity,
# color='g',
# label='Substance Abuse')
# i += 1

# rects5 = plt.bar(index + bar_width*1, other_overall_value, bar_width,
# alpha=opacity,
# color='g',
# label='Other')
# i += 1

# rects6 = plt.bar(index + bar_width*i, none_overall_value, bar_width,
# alpha=opacity,
# color='g',
# label='No Mental Illness')

plt.xlabel('Mental Illness')
plt.ylabel('Cases')
plt.title('Mental Illness cases by Type in 2013')
plt.xticks(index + bar_width, ("PTSD", "Other", "Mood/Anxiety", "Serious Mental Illness", "Substance Abuse", "No Mental Health"))
plt.legend()
plt.tight_layout()
plt.show()