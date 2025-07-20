
import pandas as pd

# import .csv files (change file path as appropriat)
medizin = pd.read_csv("/home/melanie/Documents/oral_exams/medizin.csv")
medizinstudium = pd.read_csv("/home/melanie/Documents/oral_exams/medizinstudium.csv")


# create shared data frame
combined_data = pd.concat([medizin,medizinstudium])


# create shared data frame
print(str(len(medizin.index))+" + "+str(len(medizinstudium.index))+" = "+str(len(combined_data.index)))

print(combined_data.head())


# filter comments by keyword list
# df.loc[df['col1'].isin([value1, value2, value3, ...])]


# save shared data frame



# Helpful resources:
# https://pandas.pydata.org/pandas-docs/stable/index.html
# https://www.statology.org/pandas-select-rows-based-on-column-values/