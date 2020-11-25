# This is the main file that does the stuff
import pandas as pd
import numpy as np

mental_health = pd.read_csv('VA-OHE-NVHER-FY13-Diagnoses-Mental-Illness.csv')  # import file as a dataframe

print(mental_health.columns) # determine the header columns. I am interested in the "mental health" categorization and would like to break this down by gender, race, service connection, encounters (e.g., outpatient visits, primary care visits, etc.), health conditions. column names are: ['Vulnerable_population', 'Section', 'Long_title', 'Short_title', 'Group', 'Group1', 'Subgroup', 'Mental Illness', 'Value'].

mental_health = mental_health.fillna("X") # filled all blank columns with "X" to avoid condcatenating NaN object 

mental_health["ID"] = mental_health["Long_title"] + mental_health["Short_title"] + mental_health["Group"] + mental_health["Group1"] + mental_health["Subgroup"] # this column will act as an identifier when I want to join other tables for future analysis. Long_title + Short_title + Group + Group1 + Subgroup 

# with pd.option_context('display.max_colwidth', -1):
# 	print(mental_health["ID"]) # this was used to print entire length of the column so I can double check the ID contanied all columns

mental_unique = mental_health["Mental Illness"].value_counts() # how many unique mental illness groups are there? - there are five groups: PTSD, Other, Mood/Anxiety, Serious Mental Illness, Substance Abuse, No Mental Health

# next step is to understand how each of these break down by gender, age, race, geography, encounters. after that, I'd like to understand if any health conditions correlate with certain mental illnesses.
