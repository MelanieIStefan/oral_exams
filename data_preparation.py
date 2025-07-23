
import pandas as pd

# import .csv files (change file path as appropriat)
medizin = pd.read_csv("/home/melanie/Documents/oral_exams/medizin.csv")
medizinstudium = pd.read_csv("/home/melanie/Documents/oral_exams/medizinstudium.csv")


# create shared data frame
combined_data = pd.concat([medizin,medizinstudium])


# create shared data frame
print(str(len(medizin.index))+" + "+str(len(medizinstudium.index))+" = "+str(len(combined_data.index)))

print(combined_data.head())




# get rid of NAs in the Body
combined_data_not_na =  combined_data[(combined_data.Body.notna())]

# filter comments by keyword list

keywords = "M1|M3|Physikum|mündlich|mündliche|Prüfung|Staatsexamen|Prüfer|Prüferin"


# mask =   combined_data_not_na["Body"].str.contains("M1")
mask =   combined_data_not_na["Body"].str.contains(keywords)
filtered_data = combined_data_not_na[mask]


print(filtered_data.head())



print(str(len(filtered_data.index)))

# save shared and filtered data frame

filename = "./data_combined_prefiltered.csv"

filtered_data.to_csv(filename)



# Helpful resources:
# https://pandas.pydata.org/pandas-docs/stable/index.html
# https://www.statology.org/pandas-select-rows-based-on-column-values/
# https://stackoverflow.com/questions/50397644/pandas-find-rows-where-a-particular-column-is-not-na-but-all-other-columns-are
# https://stackoverflow.com/questions/47937697/scalable-solution-for-str-contains-with-list-of-strings-in-pandas